import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const require = createRequire(new URL('../web/package.json', import.meta.url));
const { chromium } = require('@playwright/test');
const root = path.dirname(fileURLToPath(import.meta.url));
const sites = [
  ['linear', 'https://linear.app'], ['stripe', 'https://stripe.com'],
  ['palantir', 'https://www.palantir.com'], ['anduril', 'https://www.anduril.com'],
  ['figure', 'https://www.figure.ai'], ['godly', 'https://godly.website'],
];
await mkdir(path.join(root, 'screenshots'), { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const reports = [];
try {
  for (const [name, url] of sites) {
    const page = await browser.newPage({ viewport: { width: 1440, height: 960 }, deviceScaleFactor: 1 });
    const report = { name, url, capturedAt: new Date().toISOString(), viewports: [] };
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 18000 });
      for (const width of [1440, 390]) {
        await page.setViewportSize({ width, height: width === 390 ? 844 : 960 });
        const style = await page.evaluate(async () => {
          await Promise.race([document.fonts.ready, new Promise(resolve => requestAnimationFrame(resolve))]);
          const selectors = ['body', 'h1', 'h2', 'nav', 'a', 'button'];
          const elements = selectors.map(selector => {
            const element = Array.from(document.querySelectorAll(selector)).find(item => item.getBoundingClientRect().width > 0);
            if (!element) return { selector, missing: true };
            const styles = getComputedStyle(element);
            return { selector, text: element.textContent?.trim().slice(0, 100), font: styles.fontFamily, size: styles.fontSize,
              lineHeight: styles.lineHeight, weight: styles.fontWeight, tracking: styles.letterSpacing, color: styles.color,
              background: styles.backgroundColor, padding: styles.padding, gap: styles.gap, easing: styles.transitionTimingFunction,
              duration: styles.transitionDuration, position: styles.position };
          });
          const rootStyle = getComputedStyle(document.documentElement);
          const tokens = Array.from(rootStyle).filter(name => name.startsWith('--')).slice(0, 60).map(name => [name, rootStyle.getPropertyValue(name).trim()]);
          return { title: document.title, url: location.href, elements, tokens, scrollBehavior: rootStyle.scrollBehavior };
        });
        await page.screenshot({ path: path.join(root, 'screenshots', `${name}-${width}.png`), animations: 'disabled', timeout: 10000 });
        report.viewports.push({ width, ...style });
      }
    } catch (error) { report.error = error.message.slice(0, 350); }
    reports.push(report);
    await writeFile(path.join(root, 'observations.json'), JSON.stringify(reports, null, 2));
    console.log(`${name}: ${report.viewports.length} captured widths${report.error ? `; ${report.error}` : ''}`);
    await page.close();
  }
} finally { await browser.close(); }
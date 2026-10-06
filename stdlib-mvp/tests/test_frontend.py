"""Frontend static audit (stdlib unittest, no deps).

Guards the console UI without a browser: no banned dashes, balanced CSS,
every JS element lookup resolves in its page, no duplicate ids, well
formed HTML, favicon + status pill present on all pages.

Run from the MVP folder:   python tests/test_frontend.py
"""

import os
import re
import unittest
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONT = os.path.join(BASE, "frontend")

PAGES = ("index.html", "evidence.html", "docs.html", "compliance.html")
PAGE_JS = {"index.html": "app.js", "evidence.html": "evidence.js",
           "docs.html": "docs.js", "compliance.html": "compliance.js"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}


def read(name):
    with open(os.path.join(FRONT, name), encoding="utf-8") as fh:
        return fh.read()


class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("stray </%s> at %s" % (tag, self.getpos()))
            return
        top, pos = self.stack.pop()
        if top != tag:
            self.errors.append("<%s> opened %s closed by </%s> at %s"
                               % (top, pos, tag, self.getpos()))


class TestDashes(unittest.TestCase):
    def test_no_em_or_en_dashes(self):
        bad = []
        for fn in os.listdir(FRONT):
            if not fn.endswith((".html", ".js", ".css")):
                continue
            for i, line in enumerate(read(fn).splitlines(), 1):
                if "\u2013" in line or "\u2014" in line:
                    bad.append("%s:%d" % (fn, i))
        self.assertEqual(bad, [])


class TestCss(unittest.TestCase):
    def test_braces_balanced(self):
        css = read("styles.css")
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        self.assertEqual(css.count("{"), css.count("}"))
        self.assertGreater(css.count("{"), 60)

    def test_key_components_present(self):
        css = read("styles.css")
        for sel in (".envpill", ".statstrip", ".verdict", ".side-nav",
                    "canvas#evPlot", "@media print", ":focus-visible"):
            self.assertIn(sel, css, sel)


class TestIds(unittest.TestCase):
    def test_js_lookups_resolve(self):
        for page, js in PAGE_JS.items():
            html = read(page)
            ids = set(re.findall(r'id="([^"]+)"', html))
            lookups = set(re.findall(r'getElementById\("([^"]+)"', read(js)))
            lookups |= set(re.findall(r'\$\("([^"]+)"', read(js)))
            for lid in sorted(lookups):
                with self.subTest(page=page, lookup=lid):
                    self.assertIn(lid, ids)

    def test_data_out_targets_exist(self):
        html = read("docs.html")
        ids = set(re.findall(r'id="([^"]+)"', html))
        for target in set(re.findall(r'data-out="([^"]+)"', html)):
            self.assertIn(target, ids, target)

    def test_no_duplicate_ids(self):
        for page in PAGES:
            found = re.findall(r'id="([^"]+)"', read(page))
            dupes = sorted({i for i in found if found.count(i) > 1})
            self.assertEqual(dupes, [], page)


class TestHtml(unittest.TestCase):
    def test_tags_balanced(self):
        for page in PAGES:
            with self.subTest(page):
                p = TagBalance()
                p.feed(read(page))
                self.assertEqual(p.errors, [])
                self.assertEqual(p.stack, [])

    def test_chrome_present(self):
        for page in PAGES:
            html = read(page)
            with self.subTest(page):
                self.assertIn('rel="icon"', html)
                self.assertIn('id="envPill"', html)
                self.assertIn("console v1.0", html)
                self.assertIn("/evidence", html)


if __name__ == "__main__":
    unittest.main(verbosity=2)

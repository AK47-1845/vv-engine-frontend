'use client';

import { useEffect } from 'react';

export default function SmoothMotion() {
  useEffect(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    let stopped = false;
    let cleanup = () => {};
    Promise.all([import('lenis'), import('gsap'), import('gsap/ScrollTrigger')]).then(([{ default: Lenis }, { gsap }, { ScrollTrigger }]) => {
      if (stopped) return;
      gsap.registerPlugin(ScrollTrigger);
      const lenis = new Lenis({ duration: .9, smoothWheel: true, anchors: true });
      const tick = (time: number) => lenis.raf(time * 1000);
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(tick);
      cleanup = () => { gsap.ticker.remove(tick); lenis.destroy(); };
    });
    return () => { stopped = true; cleanup(); };
  }, []);
  return null;
}
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: process.env.GENUITY_STATIC_EXPORT === "1" ? "export" : undefined,
  distDir: process.env.GENUITY_STATIC_EXPORT === "1" ? ".next-transfer" : ".next",
};

export default nextConfig;

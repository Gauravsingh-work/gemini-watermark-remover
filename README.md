# Clearframe Studio – SEO & Vercel Edition

A free, browser-based image and video watermark processing workspace. Includes dedicated informational landing pages for Gemini, Google Flow, Nano Banana and Veo.

## Deploy to Vercel
1. Upload the **contents** of this folder to a new GitHub repository.
2. Import the repository into Vercel. Select **Other** as framework, with no build command and no output directory.
3. Deploy and copy the assigned `https://your-project.vercel.app` address.
4. **Important SEO step:** Run `python3 configure-domain.py https://your-project.vercel.app` on your local copy. Commit and push the updated HTML, `robots.txt` and `sitemap.xml`. This prevents publishing fake placeholder sitemap URLs.
5. Verify your domain in Google Search Console and Bing Webmaster Tools, submit `/sitemap.xml`, and request indexing of the homepage and relevant guides.

## SEO implementation
- Descriptive home title, meta description, Open Graph and JSON-LD WebApplication markup.
- Five original topic-focused landing pages and a guide hub.
- Crawlable internal links and XML sitemap.
- Canonical URLs updated after domain configuration.
- No promise of rankings or instant indexing.

## Important
The existing browser-based processing engine was carried forward from the provided source. End-to-end processing, video export and browser compatibility have **not** been fully verified. Image quality depends on the watermark mask and source compression. Do not claim universally lossless results. Review and replace any legal/contact placeholders before public launch. The original MIT LICENSE and notices remain included. Not affiliated with Google.

# NIIB Lucknow — Complete SEO + Ads landing-page project

## Upload to GitHub, deploy to Vercel
Upload **all files and the assets folder from this directory to the repository root** (not only index.html). Import that repository in Vercel with Framework Preset "Other", no build command, output directory left at default. Keep your actual deployed root path in mind.

## SEO launch requirement: domain matching
The current canonical, structured-data IDs, `sitemap.xml`, `robots.txt`, Open Graph/Twitter previews and llms documents use **https://niiblucknow.com/** as an example based on the reference site.
**If you deploy to a different Vercel address or separate custom domain, change all those URLs first.** Run from the downloaded folder:

`python configure_seo.py https://YOUR-ACTUAL-DOMAIN.com`

Then commit and redeploy. **Only claim a canonical URL that represents this landing page.** If the original site is already served at niiblucknow.com, do not replace its existing homepage unless intended; use your actual final page URL and adjust the path if not deploying at the root.

## Important files
- `index.html`: actual landing page; page title, description, canonical, Open Graph/Twitter and EducationalOrganization/WebSite/WebPage/FAQ JSON-LD schema are in `<head>`.
- `sitemap.xml`: submit the complete deployed `https://YOUR-DOMAIN/sitemap.xml` URL in Google Search Console.
- `robots.txt`: crawl instructions and sitemap reference; must resolve at domain root.
- `llms.txt`: optional brief machine-readable business summary, not an SEO ranking factor guaranteed by Google.
- `llms-full.txt`: optional longer machine-readable profile.
- `assets/niib-logo.png`: referenced by schema/social cards on the deployed site.
- `vercel.json`: static URL behavior.
- `configure_seo.py`: updates domain strings throughout the project.

## Critical production checks
- Lead form **IS NOT LIVE**; add a server-side lead endpoint or CRM integration. Never route real private lead submissions to unknown public URLs.
- Verify the call and WhatsApp number actually belongs to the admissions desk.
- Replace illustrative course and hero imagery with licensed NIIB assets.
- Replace provisional Privacy Notice with NIIB's approved privacy policy before ad traffic.
- The supplied testimonial graphics contain salary/earnings claims; use claim-free approved variants for Meta and Google Ads unless appropriately substantiated and permitted.
- Verify recognition/association logos and dates (including "Since 2004") before publication.
- Validate markup, site crawlability, working links, mobile performance, image load, and Google Search Console indexing after deployment. A file-based implementation does not guarantee rankings.

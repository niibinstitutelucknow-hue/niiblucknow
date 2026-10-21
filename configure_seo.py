"""Set this website's actual live URL after you deploy to Vercel.
Usage: python configure_seo.py https://your-actual-domain.com
Run from the root of this folder. It updates URLs in HTML, sitemap, robots and llms files.
"""
from pathlib import Path
from urllib.parse import urlparse
import sys
if len(sys.argv) != 2: raise SystemExit("Usage: python configure_seo.py https://your-domain.com")
url=sys.argv[1].strip().rstrip('/')
p=urlparse(url)
if p.scheme != 'https' or not p.netloc or p.path or p.query or p.fragment:
    raise SystemExit('Enter an HTTPS origin only, such as https://www.example.com')
for filename in ['index.html','robots.txt','sitemap.xml','llms.txt','llms-full.txt']:
    path=Path(__file__).parent/filename
    path.write_text(path.read_text(encoding='utf-8').replace('https://niiblucknow.com',url),encoding='utf-8')
print('Updated SEO URLs to',url)

#!/usr/bin/env python3
"""Run after receiving your Vercel domain: python3 configure-domain.py https://your-project.vercel.app"""
import sys,pathlib,re

root=pathlib.Path(__file__).parent
if len(sys.argv)!=2 or not re.fullmatch(r'https://[a-zA-Z0-9.-]+',sys.argv[1]): raise SystemExit('Usage: python3 configure-domain.py https://your-project.vercel.app')
base=sys.argv[1].rstrip('/')
for file in [root/'index.html',root/'guides/index.html',*root.glob('*/index.html')]:
 content=file.read_text()
 content=re.sub(r'(rel="canonical" href=")(/[^"]*)',lambda m:m.group(1)+base+m.group(2),content)
 content=re.sub(r'(href=")(/[^"]*)(" rel="canonical")',lambda m:m.group(1)+base+m.group(2)+m.group(3),content)
 file.write_text(content)
(root/'sitemap.xml').write_text((root/'sitemap.xml').read_text().replace('https://REPLACE_WITH_YOUR_VERCEL_DOMAIN',base))
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'/sitemap.xml\n')
print('Domain configured:',base)

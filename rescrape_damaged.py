import json
import re
import requests
from bs4 import BeautifulSoup
import time

ARTICLE_URLS = {
    '51061': 'https://www.artinsight.co.kr/news/view.php?no=51061',
    '47268': 'https://www.artinsight.co.kr/news/view.php?no=47268',
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def scrape_body_html(url):
    resp = requests.get(url, headers=headers, timeout=20)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    # ArtInsight content area
    content_div = (soup.select_one('.view_content') or 
                   soup.select_one('#view_content') or 
                   soup.select_one('.news_text') or
                   soup.select_one('.read_body'))
    if not content_div:
        print(f"Could not find content in {url}")
        return None
    for tag in content_div.find_all(['script', 'style']):
        tag.decompose()
    return content_div.decode_contents()

# Load current data
with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    if a['id'] in ARTICLE_URLS:
        url = ARTICLE_URLS[a['id']]
        print(f"Scraping [{a['id']}] from {url}...")
        ko_html = scrape_body_html(url)
        if ko_html:
            print(f"  Got {len(ko_html)} chars of Korean HTML")
            a['body_ko'] = ko_html
            # Write to temp file so we can translate separately
            with open(f'body_ko_{a["id"]}.html', 'w', encoding='utf-8') as f2:
                f2.write(ko_html)
        time.sleep(2)

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Korean content saved. Now need to translate and update body_en.")

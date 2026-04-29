import json
import re
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import time

DAMAGED_IDS = ['51061', '47268']
ARTICLE_URLS = {
    '66504': 'https://www.artinsight.co.kr/news/view.php?no=66504',
    '65617': 'https://www.artinsight.co.kr/news/view.php?no=65617',
    '65427': 'https://www.artinsight.co.kr/news/view.php?no=65427',
    '64006': 'https://www.artinsight.co.kr/news/view.php?no=64006',
    '63259': 'https://www.artinsight.co.kr/news/view.php?no=63259',
    '60586': 'https://www.artinsight.co.kr/news/view.php?no=60586',
    '58579': 'https://www.artinsight.co.kr/news/view.php?no=58579',
    '58119': 'https://www.artinsight.co.kr/news/view.php?no=58119',
    '56148': 'https://www.artinsight.co.kr/news/view.php?no=56148',
    '54710': 'https://www.artinsight.co.kr/news/view.php?no=54710',
    '54170': 'https://www.artinsight.co.kr/news/view.php?no=54170',
    '53074': 'https://www.artinsight.co.kr/news/view.php?no=53074',
    '52537': 'https://www.artinsight.co.kr/news/view.php?no=52537',
    '51061': 'https://www.artinsight.co.kr/news/view.php?no=51061',
    '50529': 'https://www.artinsight.co.kr/news/view.php?no=50529',
    '50044': 'https://www.artinsight.co.kr/news/view.php?no=50044',
    '50043': 'https://www.artinsight.co.kr/news/view.php?no=50043',
    '47268': 'https://www.artinsight.co.kr/news/view.php?no=47268',
}

translator = Translator()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def scrape_article(url):
    resp = requests.get(url, headers=headers, timeout=20)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    content_div = soup.select_one('.view_content') or soup.select_one('#view_content') or soup.select_one('.news_text')
    if not content_div:
        print(f"Could not find content in {url}")
        return None, None
    # Remove script/style
    for tag in content_div.find_all(['script', 'style']):
        tag.decompose()
    ko_html = str(content_div)
    # Translate
    try:
        text = content_div.get_text(separator='\n')
        translated = translator.translate(text, src='ko', dest='en')
        en_text = translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        en_text = None
    return ko_html, en_text

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    if a['id'] in DAMAGED_IDS:
        url = ARTICLE_URLS[a['id']]
        print(f"Re-scraping {a['id']} from {url}...")
        ko_html, en_text = scrape_article(url)
        if ko_html:
            a['body_ko'] = ko_html
            print(f"  Korean content restored ({len(ko_html)} chars)")
        if en_text:
            a['body_en'] = en_text
            print(f"  English translation restored ({len(en_text)} chars)")
        time.sleep(2)

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done.")

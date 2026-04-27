import urllib.request
import json
import time
import subprocess
import sys
import re

def install_deps():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4", "requests", "googletrans==4.0.0-rc1"])

try:
    from bs4 import BeautifulSoup
    import requests
    from googletrans import Translator
except ImportError:
    install_deps()
    from bs4 import BeautifulSoup
    import requests
    from googletrans import Translator

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
    "https://www.artinsight.co.kr/news/view.php?no=66504",
    "https://www.artinsight.co.kr/news/view.php?no=65617",
    "https://www.artinsight.co.kr/news/view.php?no=65427",
    "https://www.artinsight.co.kr/news/view.php?no=64006",
    "https://www.artinsight.co.kr/news/view.php?no=63259",
    "https://www.artinsight.co.kr/news/view.php?no=60586",
    "https://www.artinsight.co.kr/news/view.php?no=58579",
    "https://www.artinsight.co.kr/news/view.php?no=58119",
    "https://www.artinsight.co.kr/news/view.php?no=56148",
    "https://www.artinsight.co.kr/news/view.php?no=54710",
    "https://www.artinsight.co.kr/news/view.php?no=54170",
    "https://www.artinsight.co.kr/news/view.php?no=53074",
    "https://www.artinsight.co.kr/news/view.php?no=52537",
    "https://www.artinsight.co.kr/news/view.php?no=51061",
    "https://www.artinsight.co.kr/news/view.php?no=50529",
    "https://www.artinsight.co.kr/news/view.php?no=50044",
    "https://www.artinsight.co.kr/news/view.php?no=50043",
    "https://www.artinsight.co.kr/news/view.php?no=47268"
]

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def chunk_text(text, max_len=4000):
    chunks = []
    current = ""
    for sentence in text.split('. '):
        if len(current) + len(sentence) < max_len:
            current += sentence + '. '
        else:
            chunks.append(current.strip())
            current = sentence + '. '
    if current:
        chunks.append(current.strip())
    return chunks

def main():
    translator = Translator()
    articles = []
    
    for i, url in enumerate(urls):
        print(f"Processing {i+1}/{len(urls)}: {url}")
        try:
            req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
            req.encoding = 'utf-8'
            soup = BeautifulSoup(req.text, 'html.parser')
            
            # Title
            title_el = soup.select_one('.sub_top_txt h2')
            ko_title = clean_text(title_el.text) if title_el else ""
            if not ko_title:
                h3 = soup.find('h3')
                ko_title = h3.text if h3 else "Article"
            
            # Date
            date_el = soup.select_one('.top_date span')
            date = clean_text(date_el.text).split(' ')[0] if date_el else "Unknown Date"
            
            # Body
            body_el = soup.find('div', class_='view_content')
            
            if body_el:
                # Remove scripts and styles
                for s in body_el(['script', 'style']):
                    s.extract()
                ko_body = clean_text(body_el.get_text(separator='\n'))
            else:
                ko_body = "Content not found."

            print(f"  Title: {ko_title}")
            print(f"  Length: {len(ko_body)}")
            
            # Translate Title
            try:
                en_title = translator.translate(ko_title, src='ko', dest='en').text
            except Exception as e:
                print("  Title translation error:", e)
                en_title = ko_title
            
            # Translate Body in chunks
            en_body = ""
            chunks = chunk_text(ko_body, 3000)
            for chunk in chunks:
                if not chunk: continue
                try:
                    translated = translator.translate(chunk, src='ko', dest='en')
                    en_body += translated.text + "\n\n"
                    time.sleep(0.5)
                except Exception as e:
                    print("  Chunk translation error:", e)
                    en_body += chunk + "\n\n"
                    
            article_id = url.split('no=')[-1]
            
            # Make a short excerpt
            excerpt = en_body[:200] + "..." if len(en_body) > 200 else en_body
            
            articles.append({
                "id": article_id,
                "url": url,
                "date": date,
                "title_ko": ko_title,
                "title_en": en_title,
                "excerpt": excerpt,
                "body_en": en_body.strip(),
                "body_ko": ko_body.strip()
            })
            
        except Exception as e:
            print(f"  Error processing {url}: {e}")
            
    with open('articles_data.js', 'w', encoding='utf-8') as f:
        f.write("const articlesData = ")
        json.dump(articles, f, ensure_ascii=False, indent=2)
        f.write(";")
    print("Done writing articles_data.js")

if __name__ == "__main__":
    main()

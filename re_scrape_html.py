import json
import urllib3
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import time
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
translator = Translator()

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for i, a in enumerate(articles):
    url = a['url']
    print(f"Processing {i+1}/{len(articles)}: {url}")
    try:
        req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, 'html.parser')
        
        body_el = soup.find('div', class_='view_content')
        if not body_el:
            print(f"  Failed to find view_content")
            continue
            
        # Clean scripts and styles
        for s in body_el(['script', 'style', 'iframe']):
            s.extract()
            
        # Fix relative image URLs
        for img in body_el.find_all('img'):
            if img.has_attr('src'):
                src = img['src']
                if src.startswith('/'):
                    img['src'] = 'https://www.artinsight.co.kr' + src
                    
        children_html = []
        for child in body_el.children:
            child_str = str(child).strip()
            if not child_str: continue
            if child_str in ['<p>&nbsp;</p>', '<p></p>', '<br>', '<br/>']: continue
            # Also skip any empty spans or divs that just have whitespace
            if re.match(r'^<[^>]+>\s*</[^>]+>$', child_str): continue
            
            children_html.append(child_str)
            
        ko_html = "\n".join(children_html)
        
        translated_children = []
        chunk = ""
        for child_str in children_html:
            if len(chunk) + len(child_str) > 2000:
                try:
                    res = translator.translate(chunk, src='ko', dest='en').text
                    translated_children.append(res)
                except Exception as e:
                    print("  Trans err:", e)
                    translated_children.append(chunk)
                chunk = child_str
                time.sleep(0.5)
            else:
                chunk += "\n" + child_str if chunk else child_str
                
        if chunk:
            try:
                res = translator.translate(chunk, src='ko', dest='en').text
                translated_children.append(res)
            except Exception as e:
                print("  Trans err:", e)
                translated_children.append(chunk)
                
        en_html = "\n".join(translated_children)
        
        # Fix spacing after periods in the english html
        en_html = re.sub(r'\.([A-Z])', r'. \1', en_html)
        
        a['body_ko'] = ko_html
        a['body_en'] = en_html
        
    except Exception as e:
        print(f"  Error: {e}")

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML Re-scrape completed")

import re
import requests
import json
import urllib3
from googletrans import Translator

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
translator = Translator()

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract json
json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for i, a in enumerate(articles):
    url = a['url']
    print(f"Processing {i+1}/18: {url}")
    res = requests.get(url, verify=False)
    text = res.text
    
    # Extract title
    title_match = re.search(r"\$\('\.sub_top_txt h2'\)\.text\('([^']+)'\)", text)
    if title_match:
        ko_title = title_match.group(1).replace('[칼럼]', '').replace('[에세이]', '').strip()
    else:
        # Fallback to <title>
        t_match = re.search(r"<title>(.*?)</title>", text)
        ko_title = t_match.group(1).replace('[칼럼]', '').replace('[에세이]', '').strip() if t_match else a['title_ko']
    
    # Extract date
    date_match = re.search(r'<div class="top_date"><span>([^<]+)</span>', text)
    if date_match:
        date_str = date_match.group(1).split(' ')[0] # e.g. "2023.09.01"
    else:
        date_str = a['date']
    
    # Translate title
    try:
        en_title = translator.translate(ko_title, src='ko', dest='en').text
    except Exception as e:
        en_title = ko_title
        print("Translation failed", e)
    
    a['title_ko'] = ko_title
    a['title_en'] = en_title
    a['date'] = date_str

# Write back
new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Done!")

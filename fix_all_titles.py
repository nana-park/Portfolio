import json
import re
from googletrans import Translator
import time

translator = Translator()

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    # Clean Korean Title
    original_ko = a['title_ko']
    cleaned_ko = re.sub(r'\[.*?\]', '', original_ko).strip()
    a['title_ko'] = cleaned_ko
    
    # Clean English Title
    original_en = a['title_en']
    cleaned_en = re.sub(r'\[.*?\]', '', original_en).strip()
    
    # Check if we need to retranslate
    needs_translation = False
    if re.search(r'[가-힣]', cleaned_en):
        needs_translation = True
    elif original_ko == original_en:
        needs_translation = True
        
    if needs_translation:
        # Time sleep to avoid rate limits
        time.sleep(1)
        try:
            trans = translator.translate(cleaned_ko, src='ko', dest='en').text
            cleaned_en = re.sub(r'\[.*?\]', '', trans).strip()
        except Exception as e:
            pass # fallback to whatever it was
            
    a['title_en'] = cleaned_en

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Title cleanup finished")

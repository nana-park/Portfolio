import json
import re
import os

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

def get_size(url):
    filename = f"temp_imgs/{url.split('/')[-1]}"
    if os.path.exists(filename):
        return os.path.getsize(filename)
    return 0

for a in articles:
    # find all images in body_ko
    imgs = re.findall(r'<img[^>]+src=[\"\'](.*?)[\"\'][^>]*>', a['body_ko'])
    for url in imgs:
        if get_size(url) == 37374:
            print(f"Removing business card from {a['id']}: {url}")
            escaped_url = re.escape(url)
            
            # Remove <p><img ...></p>
            pattern_p = rf'<p[^>]*>\s*<img[^>]+src=[\"\']{escaped_url}[\"\'][^>]*>\s*</p>'
            a['body_ko'] = re.sub(pattern_p, '', a['body_ko'])
            a['body_en'] = re.sub(pattern_p, '', a['body_en'])
            
            # Remove <div><img ...></div>
            pattern_div = rf'<div[^>]*>\s*<img[^>]+src=[\"\']{escaped_url}[\"\'][^>]*>\s*</div>'
            a['body_ko'] = re.sub(pattern_div, '', a['body_ko'])
            a['body_en'] = re.sub(pattern_div, '', a['body_en'])
            
            # Fallback to just img
            pattern_img = rf'<img[^>]+src=[\"\']{escaped_url}[\"\'][^>]*>'
            a['body_ko'] = re.sub(pattern_img, '', a['body_ko'])
            a['body_en'] = re.sub(pattern_img, '', a['body_en'])

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Business cards removed.")

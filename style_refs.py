import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

# Regex to find <p> tags containing the reference keywords
pattern_en = re.compile(r'(<p[^>]*>)\s*(Photo source|Reference|Source|Image source|Photography|Ref)\s*[:\-].*?</p>', re.IGNORECASE | re.DOTALL)
pattern_ko = re.compile(r'(<p[^>]*>)\s*(출처|참고|사진 출처|자료 출처|이미지 출처|사진|참조)\s*[:\-].*?</p>', re.IGNORECASE | re.DOTALL)

def add_class(match):
    # If the <p> already has a class, we would append to it, but it's simpler to just replace the tag
    # Let's just wrap the inner text in a span if we can't easily modify the <p> tag, 
    # OR replace <p> with <p class="article-reference">.
    tag = match.group(1)
    if 'class="' in tag:
        new_tag = tag.replace('class="', 'class="article-reference ')
    else:
        new_tag = tag.replace('<p', '<p class="article-reference"')
    return match.group(0).replace(tag, new_tag)

for a in articles:
    a['body_en'] = pattern_en.sub(add_class, a['body_en'])
    a['body_ko'] = pattern_ko.sub(add_class, a['body_ko'])

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Classes added to references.")

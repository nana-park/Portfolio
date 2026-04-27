import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

def replace_color(match):
    color_val = match.group(1).lower().replace(' ', '')
    if color_val in ['#000', '#000000', '#111', '#111111', '#222', '#222222', '#333', '#333333', 'rgb(0,0,0)', 'black']:
        return match.group(0)
    return 'color: #d97706'

def fix_punctuation_spacing(text):
    # Fix missing spaces after punctuation, being careful to ignore HTML tags
    # We only want to add a space if a punctuation mark is directly followed by an uppercase letter,
    # OR if it's followed by a closing HTML tag and then an uppercase letter?
    # e.g., `well?</span>First` -> we can just run a regex that looks for `>` or punctuation, but simpler:
    # let's just do it broadly but safely.
    # First, fix `well?First`
    text = re.sub(r'([.?!])([A-Z])', r'\1 \2', text)
    # What if it's `well?</span>First`?
    text = re.sub(r'([.?!])(</[a-zA-Z]+>)([A-Z])', r'\1\2 \3', text)
    # What if it's `well?</p><p>First`? That's fine, it's block level.
    # What if it's `well? <span...`? That's fine.
    # Also fix `difficult\r\nThere` -> `difficult There` just in case, though HTML handles it.
    text = text.replace('\r\n', ' ').replace('\n', ' ')
    # Clean up multiple spaces
    text = re.sub(r' {2,}', ' ', text)
    return text

for a in articles:
    # 1. Fix colors
    a['body_en'] = re.sub(r'color:\s*([^;\"\']+)', replace_color, a['body_en'])
    a['body_ko'] = re.sub(r'color:\s*([^;\"\']+)', replace_color, a['body_ko'])
    
    # 2. Fix spacing
    a['body_en'] = fix_punctuation_spacing(a['body_en'])

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Spacing and colors fixed.")

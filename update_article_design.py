import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

# Regex to match empty leading paragraphs (can run multiple times or use +)
empty_p_pattern = re.compile(r'^(\s*<p[^>]*>\s*(?:<br\s*/?>|&nbsp;|\s|<i>\s*</i>)*\s*</p>\s*)+', re.IGNORECASE)

# Regex to match hr
hr_pattern = re.compile(r'<hr[^>]*>', re.IGNORECASE)

# Regex to find heading paragraphs
heading_pattern = re.compile(r'(<p[^>]*>)(\s*(?:<b[^>]*>|<strong[^>]*>)?\s*<span[^>]*font-size:\s*(?:1[6-9]|[2-9][0-9])(?:px|pt)[^>]*>.*?</p>)', re.IGNORECASE)
# Another pattern just in case font-size is on the p tag or b tag
heading_pattern_2 = re.compile(r'(<p[^>]*font-size:\s*(?:1[6-9]|[2-9][0-9])(?:px|pt)[^>]*>)(\s*(?:<b[^>]*>|<strong[^>]*>)?.*?</p>)', re.IGNORECASE)

def fix_headings(text):
    text = empty_p_pattern.sub('', text.lstrip())
    # remove hr
    text = hr_pattern.sub('', text)
    
    # Add class to heading paragraphs
    def add_class(match):
        p_tag = match.group(1)
        if 'class="' in p_tag:
            new_p = p_tag.replace('class="', 'class="article-subheading ')
        else:
            new_p = p_tag.replace('<p', '<p class="article-subheading"')
        return new_p + match.group(2)
        
    text = heading_pattern.sub(add_class, text)
    text = heading_pattern_2.sub(add_class, text)
    
    # Also, some headings might just be `<p><b>Some Text</b></p>` followed by `<hr>`.
    # Wait, we already removed <hr>. If there are standalone <b> headings without font-size, they might be missed.
    # But usually, authors increase font size for headings. Let's stick to font-size for now.
    
    # Clean up empty spaces again just in case
    text = empty_p_pattern.sub('', text.lstrip())
    
    return text

for a in articles:
    a['body_en'] = fix_headings(a['body_en'])
    a['body_ko'] = fix_headings(a['body_ko'])

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Article HTML cleaned and structured.")

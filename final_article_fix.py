import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

# 1. Fix leading paragraphs with dots or empty space
# Match <p> containing whitespace, &nbsp;, <br>, <i>, or a single dot like · ㆍ .
empty_p_pattern = re.compile(r'^(\s*<p[^>]*>\s*(?:<br\s*/?>|&nbsp;|\s|<i>\s*</i>|[·ㆍ\.])*\s*</p>\s*)+', re.IGNORECASE)

# 2. Fix the "Source" followed by another <p>
# Match <p>Source</p> (or 출처, 참고, Reference) followed by another <p>
source_multi_pattern = re.compile(r'(<p[^>]*>\s*(?:Source|출처|참고|Reference|Photo source|Images|Photography|Ref)\s*</p>)\s*(<p[^>]*>)', re.IGNORECASE)

# 3. Fix headings that are just <p><b>...</b></p> or <p><strong>...</strong></p> without font-size
# A heading is a <p> tag whose ENTIRE text content is inside a <b> or <strong> tag, and it's short (e.g., < 100 chars), and doesn't have an image inside.
heading_only_b_pattern = re.compile(r'<p[^>]*>\s*(?:<b>|<strong>)([^<]{2,100})(?:</b>|</strong>)\s*</p>', re.IGNORECASE)
# Actually, it's safer to just find <p><b>...</b></p> where ... doesn't have tags.
def fix_heading_b(match):
    text_inside = match.group(1)
    if 'class="article-subheading"' in match.group(0):
        return match.group(0)
    # Add the class
    return f'<p class="article-subheading"><b>{text_inside}</b></p>'

for a in articles:
    # Fix leading empty paragraphs
    a['body_en'] = empty_p_pattern.sub('', a['body_en'].lstrip())
    a['body_ko'] = empty_p_pattern.sub('', a['body_ko'].lstrip())
    
    # Fix multi-line source
    # If we find <p>Source</p> <p>..., we make the first one class="article-reference" and the second one too.
    def style_multi_source(m):
        p1 = m.group(1)
        p2 = m.group(2)
        if 'class=' not in p1:
            p1 = p1.replace('<p', '<p class="article-reference"')
        if 'class=' not in p2:
            p2 = p2.replace('<p', '<p class="article-reference"')
        return p1 + '\n' + p2
        
    a['body_en'] = source_multi_pattern.sub(style_multi_source, a['body_en'])
    a['body_ko'] = source_multi_pattern.sub(style_multi_source, a['body_ko'])
    
    # Fix just <b> headings
    a['body_en'] = heading_only_b_pattern.sub(fix_heading_b, a['body_en'])
    a['body_ko'] = heading_only_b_pattern.sub(fix_heading_b, a['body_ko'])
    
    # Also find if there are any <p>Source: ...</p> that were missed because they didn't have : or -
    # e.g., <p>Source Hyung Lee...</p>
    source_single_pattern = re.compile(r'<p[^>]*>\s*(?:Source|출처|참고|Reference)\s+[^<]+</p>', re.IGNORECASE)
    def style_single_source(m):
        p = m.group(0)
        if 'class=' not in p:
            p = p.replace('<p', '<p class="article-reference"')
        return p
    a['body_en'] = source_single_pattern.sub(style_single_source, a['body_en'])
    a['body_ko'] = source_single_pattern.sub(style_single_source, a['body_ko'])

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Final article fixes applied.")

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old = r'''                .product-item {
                    border: 1px solid #e5e7eb;
                    background: #fff;
                    padding: 8px;
                    min-height: 90px;
                    display: flex;
                    flex-direction: column;
                }
                .product-img {
                    height: 42px;
                    background: #f0f1f3;
                    margin-bottom: 8px;
                }'''

css_new = r'''                .product-item {
                    border: 1px solid #e5e7eb;
                    background: #fff;
                    padding: 10px;
                    min-height: 90px;
                    display: flex;
                    flex-direction: column;
                    border-radius: 12px;
                }
                .product-img {
                    height: 52px;
                    background: #f0f1f3;
                    margin-bottom: 10px;
                    border-radius: 6px;
                }'''

content = content.replace(css_old, css_new)

# 2. Add Buy buttons
button_html = '<div style="margin-top: 10px; background: #111827; color: white; text-align: center; font-size: 11px; font-weight: 600; padding: 6px 0; border-radius: 6px; cursor: pointer;">Buy</div>'

def add_button(match):
    return match.group(1) + match.group(2) + match.group(3) + match.group(4) + (' ' * len(match.group(5))) + button_html + '\n' + match.group(5) + '</div>'

# Regex to match the product-item block regardless of exact indentation
pattern = r'(<div class="product-item">)(.*?)(<div class="product-meta">.*?</div>)(\s*)(</div>)'
content = re.sub(pattern, add_button, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifications complete.")

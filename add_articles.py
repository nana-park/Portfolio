import re
import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update routing array
        content = content.replace('{home:1, about:1, life:1, projects:1, research:1, awards:1, contact:1}', '{home:1, about:1, life:1, projects:1, research:1, articles:1, awards:1, contact:1}')
        content = content.replace("'research': ['research', 'contact'],", "'research': ['research', 'contact'],\n                'articles': ['articles', 'contact'],")
        content = content.replace("routes['research'], routes['awards']", "routes['research'], routes['articles'], routes['awards']")

        # 2. Update GNB LNB height and add Articles link
        # The dropdown container has class like: absolute top-[70px] left-1/2 -translate-x-1/2 w-[200px] h-[80px]
        # We need to change h-[80px] to h-[120px] to fit 3 items
        gnb_pattern = r'(absolute top-\[70px\] left-1/2 -translate-x-1/2 w-\[200px\] )h-\[80px\]( opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 flex flex-col justify-center items-center gap-1\.5 z-\[999\]\">\s*<a href=\"#projects\" class=\"text-\[13px\] font-sans font-medium text-white/90 hover:text-\[#d97706\] transition-colors flex items-center justify-center w-full lnb-link\">\s*Products\s*</a>\s*<a href=\"#research\" class=\"text-\[13px\] font-sans font-medium text-white/90 hover:text-\[#d97706\] transition-colors flex items-center justify-center w-full lnb-link\">\s*Research\s*</a>)'
        
        replacement = r'\1h-[120px]\2\n                        <a href="#articles" class="text-[13px] font-sans font-medium text-white/90 hover:text-[#d97706] transition-colors flex items-center justify-center w-full lnb-link">\n                            Articles\n                        </a>'
        
        content = re.sub(gnb_pattern, replacement, content)

        # 3. Duplicate research section to create articles section
        # Extract research section
        match = re.search(r'<!-- Research Section -->(.*?)<!-- Toolkit Grid \(Runway Style\) -->', content, re.DOTALL)
        if match:
            research_sec = match.group(0)
            # Modify research_sec for articles
            articles_sec = research_sec.replace('id="research"', 'id="articles"')
            articles_sec = articles_sec.replace('<!-- Research Section -->', '<!-- Articles Section -->')
            articles_sec = articles_sec.replace('Research from Nahyun', 'Articles from Nahyun')
            articles_sec = articles_sec.replace('Pioneering user-centric AI experiences<br>through deep academic inquiry and behavioral science.', 'Sharing insights and thoughts<br>on AI product management and user experience.')
            articles_sec = articles_sec.replace('Bridging the gap between human psychology and software engineering.', 'Exploring the intersection of business, technology, and design.')
            articles_sec = articles_sec.replace('Grounded in Interaction Science, Psychology, and Multimedia.', 'Practical perspectives from the field.')
            articles_sec = articles_sec.replace('Applying empirical research methodologies to orchestrate meaningful digital transformation.', 'Documenting lessons learned, product strategies, and industry trends.')
            
            # Insert articles section after research section
            content = content.replace(research_sec, research_sec + '\n    ' + articles_sec)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

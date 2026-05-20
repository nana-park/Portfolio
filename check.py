import html.parser
import sys

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'link', 'meta', 'source', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'area', 'col', 'command', 'embed', 'keygen', 'param', 'track', 'wbr', 'svg']:
            self.tags.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if tag in ['img', 'br', 'hr', 'input', 'link', 'meta', 'source', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'area', 'col', 'command', 'embed', 'keygen', 'param', 'track', 'wbr', 'svg']: return
        if not self.tags:
            self.errors.append(f'Unmatched end tag </{tag}> at {self.getpos()}')
            return
        last_tag, pos = self.tags.pop()
        if last_tag != tag:
            self.errors.append(f'Mismatched end tag: Expected </{last_tag}>, got </{tag}> at {self.getpos()}. Started at {pos}')
            # self.tags.append((last_tag, pos))

p = MyHTMLParser()
with open('index.html', 'r', encoding='utf-8') as f:
    p.feed(f.read())
for e in p.errors:
    print(e)
if p.tags:
    print('Unclosed tags:', [(t, pos) for t, pos in p.tags[-5:]])

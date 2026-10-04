"""Check local links, image accessibility and the shared case-study structure."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.errors = path, set(), [], []
        self.headings = 0
        self.sections = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append('Duplicate ID: ' + attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.headings += 1
        if tag == 'section' and 'case-section' in attrs.get('class', '').split():
            self.sections.append(attrs.get('id'))
        if tag == 'img' and not attrs.get('alt'):
            self.errors.append('Missing image description')
        for key in ('src', 'href'):
            if attrs.get(key):
                self.links.append(attrs[key])

pages = {p.name: Page(p) for p in ROOT.glob('*.html')}
errors = []
expected = ['overview', 'contribution', 'approach', 'results', 'gallery', 'resources']
for name, page in pages.items():
    errors.extend(f'{name}: {error}' for error in page.errors)
    if page.headings != 1:
        errors.append(f'{name}: expected one h1')
    if name != 'index.html' and page.sections != expected:
        errors.append(f'{name}: inconsistent case-study structure')
    for url in page.links:
        u = urlsplit(url)
        if u.scheme or u.netloc:
            continue
        target = ROOT / unquote(u.path) if u.path else page.path
        if not target.exists():
            errors.append(f'{name}: missing file {url}')
        if u.fragment and target.suffix == '.html' and u.fragment not in pages[target.name].ids:
            errors.append(f'{name}: missing anchor {url}')
print(f'Checked {len(pages)} pages: {len(errors)} errors.')
for error in errors:
    print(error)
raise SystemExit(bool(errors))

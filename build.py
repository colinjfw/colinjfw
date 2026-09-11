import os
import markdown
import shutil
import jinja2

robots = """
User-agent: *
Disallow:
"""

with open('./template.html', 'r', encoding='utf-8') as f:
    template = f.read()

def render(title, path, links=None):
    uri = path.replace(" ", "-").replace("–", "").replace("’", "").replace("'", "").replace("&", "").replace(".md", ".html").replace('---', '-').replace('--', '-').lower()
    dst = os.path.join("./dist", uri)

    data = {
        'links': links
    }

    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    text = jinja2.Template(text).render(**data)
    body = markdown.markdown(text, extensions=['footnotes'])
    html = template.replace("TITLE", title).replace("CONTENT", body)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w') as f:
        f.write(html)
    return uri


shutil.rmtree("./dist/", ignore_errors=True)
os.makedirs("./dist/", exist_ok=True)

shutil.copytree("./assets", "./dist/assets")

with open("./dist/robots.txt", 'w') as f:
    f.write(robots)

links = {}

for root, dirs, files in os.walk('posts/'):
    for file in files:
        theme = root.replace("posts/", "")
        if theme not in links:
            links[theme] = {'title': theme, 'path': None, 'children': [] }

        date = file.split('_')[0]
        path = os.path.join(root, file)
        with open(path, 'r') as f:
            title = date + " - " + f.readline().replace("#", "").strip()
        uri = render(title, path)

        links[theme]['children'].append({ 'title': title, 'path': uri })
        links[theme]['children'].sort(key=lambda item: item['title'])

sorted_links = sorted(links.values(), key=lambda item: item['title'])

render("Colin Walker", "./index.md", sorted_links)

import frontmatter
import markdown
import pdfkit


def process(path: str, output: str):
    with open(path) as f:
        metadata, content = frontmatter.parse(f.read())

        content = markdown.markdown(content)

        html = ""
        with open("document.html") as document:
            html = document.read()

        html = html.replace("%level%", metadata['level']) \
            .replace("%title%", metadata['title']) \
            .replace("%content%", content)

        pdfkit.from_string(html, output)


process("../src/decapeur_thermique.md", "./decapeur_thermique.pdf")

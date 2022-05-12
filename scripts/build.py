import os
import re
import shutil
import mistletoe
from mistletoe import HTMLRenderer
from pygments import highlight
from pygments.lexers import get_lexer_by_name as get_lexer
from pygments.formatters.html import HtmlFormatter
from .parser import ChimeraLexer


class PygmentsRenderer(HTMLRenderer):
    formatter = HtmlFormatter()

    def __init__(self, *extras, style='default'):
        super().__init__(*extras)
        self.formatter.encoding = "utf-8"

    def render_inline_code(self, token):
        res = highlight(token.children[0].content, ChimeraLexer(), self.formatter).decode("utf-8")
        return "<span class=\"highlight\">"+res[28:-13].rstrip()+"</span>"

    def render_block_code(self, token):
        lexer = get_lexer(token.language) if token.language else ChimeraLexer()
        return highlight(token.children[0].content, lexer, self.formatter).decode("utf-8")


STATIC_ASSETS = ["Logo.png", "style.css"]

HTML_BEFORE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet"> 
    <link href="https://trashbyte.io/fonts/Cambria.css" rel="stylesheet">
  </head>
  <body>
    <main class="page-content" aria-label="Content">
      <div id="main">
"""
HTML_AFTER = """
      </div>
    </main>
  </body>
</html>
"""

hierarchy = {
    "name": "root",
    "items": []
}
current_path = ["root","","","","",""]


def add_item_to_hierarchy(heading, depth):
    #print("  add_item_to_hierarchy depth {} heading '{}' current_path '{}'".format(depth, heading, "/".join(current_path)))
    ref = hierarchy
    built_path = "root"
    for i in range(0, depth):
        #print("    finding depth {} - {}".format(depth+i, current_path[i]))
        ref = next(filter(lambda item: item["name"] == current_path[i], ref["items"]))
        built_path += "/"+current_path[i]
    ref["items"].append({
            "name": heading,
            "path": built_path[5:],
            "items": []
        })
    #print("appended '{}/{}' to item '{}' at depth {}".format(built_path, heading, ref["name"], depth+1))

built_md = []
def process_file(fname, depth):
    text = open(fname, "rt", encoding="utf-8").read()
    for line in text.split("\n"):
        if line.startswith(r"%INCLUDE%"):
            #print("include line - "+line)
            line = line[9:].strip()
            split = line.split("/")
            (lpath, heading) = (split[0], split[1])
            #print("  {} / {}".format(lpath, heading))
            built_md.append(r"%%NUM%%"+"{}\n".format(heading))
            current_path[depth+1] = heading
            #print("  updated current_path[{}]: '{}'".format(depth+1, "/".join(current_path)))
            add_item_to_hierarchy(heading, depth+1)
            process_file("{}/{}.md".format(lpath, heading), depth+1)
        elif line.startswith("#"):
            #print("heading line - "+line)
            hdepth = len(re.match('#+', line.strip()).group(0))
            #print("  hdepth "+str(hdepth))
            heading = line[hdepth+1:].strip()
            current_path[hdepth-1] = heading
            #print("  updated current_path[{}]: '{}'".format(hdepth, "/".join(current_path)))
            add_item_to_hierarchy(heading, hdepth-1)
            built_md.append(r"%%NUM%%" + heading)
        else:
            built_md.append(line)

def build_main():
    print("building...")
    process_file("index.md", 0)

    def build_toc_html(item, depth, depths, line_idx):
        depths[depth] += 1
        html = ""
        numstr = ""
        href = "#"
        for i in range(0,depth+1):
            numstr += "{}.".format(depths[i])
        if len(item["path"]) > 0:
            html += '<li><a href="#{}/{}">{} {}</a></li>'.format(item["path"], item["name"], numstr, item["name"])
        else:
            html += '<li><a href="#{}">{} {}</a></li>'.format(item["name"], numstr, item["name"])

        replaced = False
        while line_idx < len(built_md):
            if built_md[line_idx].startswith(r"%%NUM%%"):
                line = built_md[line_idx][7:]
                hstr = ""
                if len(item["path"]) > 0:
                    hstr = '<h{} id="{}/{}">{} {}</h{}>'.format(depth+1, item["path"], item["name"], numstr, line, depth+1)
                else:
                    hstr = '<h{} id="{}">{} {}</h{}>'.format(depth+1, item["name"], numstr, line, depth+1)
                built_md[line_idx] = hstr
                replaced = True
                break
            line_idx += 1

        if not replaced:
            raise Exception("Failed to find line to replace for heading '{} {}'".format(numstr, line))

        depths[depth+1] = 0
        for i in item["items"]:
            html += '<ul>'
            html += build_toc_html(i, depth+1, depths, line_idx)
            html += '</ul>'
        return html

    toc_html = '<div id="toc"><ul>'
    depths = [0,0,0,0,0]
    for item in hierarchy["items"]:
        toc_html += build_toc_html(item, 0, depths, 0)
    toc_html += '</ul></div>'

    with open("_build/index.html", "wt", encoding="utf-8") as f:
        rendered = mistletoe.markdown("\n".join(built_md), PygmentsRenderer)
        html = HTML_BEFORE+rendered+HTML_AFTER
        print("writing _build/index.html...")
        f.write(html.replace(r"%%TOC%%", toc_html))

    for fname in STATIC_ASSETS:
        print("copying _build/{}...".format(fname))
        shutil.copyfile(fname, "_build/{}".format(fname))
import unittest
from markdown_to_html_node import *
from htmlnode import *

class testMarkdownTo(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )


    def test_codeblock(self):
        # remember, doesn't mess with inline  shit
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",

        )
    def test_quote_block(self):
        md="""
> This is a quote
> spanning multiple lines
> with **bold** and _italic_ text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,"<div><blockquote>This is a quote spanning multiple lines with <b>bold</b> and <i>italic</i> text</blockquote></div>")


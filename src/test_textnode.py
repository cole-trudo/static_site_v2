import unittest
from textnode import TextNode, TextType,text_node_to_html_node, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node= TextNode("This is plain text", TextType.PLAIN)
        node2 = TextNode("This is a  BOLD text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_link(self):
        node= TextNode("This is a node with a link", TextType.LINK, "link.com")
        self.assertEqual(node.url,"link.com")
    def test_nolink(self):
        node=TextNode("This is your momma", TextType.BOLD)
        self.assertEqual(node.url,None)

        #configure node 1, then return node1.link text and check it equals the input?
    def test_not_type(self):
        with self.assertRaises(Exception) as cm:
            node= TextNode(2,TextType.BIG_LETTA,2)
            html_node= text_node_to_html_node(node)
    def test_text_PLAIN(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_IMAGE(self):
        node= TextNode("this guys pooping!",TextType.IMAGE,url="poop.com")
        html_node=text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.props,{"src":"poop.com","alt":"this guys pooping!"})
    def test_LINK(self):
        node= TextNode("this guy is linking!",TextType.LINK,url="link.com")
        html_node=text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.props,{"href":"link.com"})
        self.assertEqual(html_node.value,"this guy is linking!")
    def test_CODE(self):
        node= TextNode("rolling and coding",TextType.CODE)
        html_node=text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value,"rolling and coding")
    def test_ITALIC(self):
        node=TextNode("italics are fancy", TextType.ITALIC)
        html_node=text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value,"italics are fancy")
    def test_BOLD(self):
        node=TextNode("bold and brash", TextType.BOLD)
        html_node=text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value,"bold and brash")

    def test_Markdown_Links(self):
        result=extract_markdown_links("I am a link text[to the moon](moon.com)")
        self.assertListEqual(result,[("to the moon","moon.com")])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_two_links(self):
        matches=extract_markdown_links("this is text with [one](link.com) and a [second](link.org)")
        self.assertListEqual(matches,[("one","link.com"),("second","link.org")])
    def test_two_images(self):
        matches= extract_markdown_images("enjoy the site: ![image of dog](dogs.com) we also have other animals ![image of a cat](cats.com)")
        self.assertListEqual(matches,[("image of dog","dogs.com"),("image of a cat","cats.com")])
    
      
    
        


if __name__ == "__main__":
    unittest.main()
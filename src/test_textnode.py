import unittest
from textnode import TextNode, TextType


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
        with self.assertRaises(ValueError) as cm:
            node= TextNode(2,"cracker",2)
      
    
        


if __name__ == "__main__":
    unittest.main()
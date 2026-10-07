import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node= HTMLNode("<head>","text_inside",["child","kids"],{
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
    def test_only_value(self):
        #should return just a value
        node= HTMLNode(value="Howdy")
        self.assertEqual(node.tag,None)
        self.assertEqual(node.value,"Howdy")

        
    def test_no_props(self):
        node= HTMLNode("<head>","text_inside",["child","kids"])
        self.assertEqual(node.props,None)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_not_type(self):
            with self.assertRaises(ValueError) as cm:
                node= LeafNode("p",None)
                node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    

    




        



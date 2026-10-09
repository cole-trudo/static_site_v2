import unittest
from textnode import TextNode, TextType
from NodeDelimeter import split_nodes_delimiter


class TestNodeDelimeter(unittest.TestCase):

    def test_TwoLine(self):
        nodes = [
    TextNode("This is text with a **bolded phrase** in the middle", TextType.PLAIN),
    TextNode("already bold", TextType.BOLD),
    ]
        result=split_nodes_delimiter(nodes,"**",TextType.BOLD)
        list2=[TextNode("This is text with a " , TextType.PLAIN, None), TextNode("bolded phrase", TextType.BOLD, None), TextNode(" in the middle", TextType.PLAIN, None), TextNode("already bold", TextType.BOLD, None)]
        self.assertEqual(result,list2)
    def test_singleDelim(self):
         with self.assertRaises(ValueError) as cm:
             nodes=[TextNode("this is **kinda bold",TextType.PLAIN)]
             split_nodes_delimiter(nodes,"**",TextType.BOLD)


        

import unittest
from textnode import TextNode, TextType
from NodeDelimeter import split_nodes_delimiter,split_nodes_image, split_nodes_link


class TestNodeDelimeter(unittest.TestCase):

    def test_TwoLine(self):
        nodes = [
    TextNode("This is.PLAIN with a **bolded phrase** in the middle", TextType.PLAIN),
    TextNode("already bold", TextType.BOLD),
    ]
        result=split_nodes_delimiter(nodes,"**",TextType.BOLD)
        list2=[TextNode("This is.PLAIN with a " , TextType.PLAIN, None), TextNode("bolded phrase", TextType.BOLD, None), TextNode(" in the middle", TextType.PLAIN, None), TextNode("already bold", TextType.BOLD, None)]
        self.assertEqual(result,list2)
    def test_singleDelim(self):
         with self.assertRaises(ValueError) as cm:
             nodes=[TextNode("this is **kinda bold",TextType.PLAIN)]
             split_nodes_delimiter(nodes,"**",TextType.BOLD)
    def test_SplitNodesImage(self):
        mrkdown=[TextNode("check out my ![dog](dog.com) and my cat ![meow](kitty.org)",TextType.PLAIN)]
        extracted=split_nodes_image(mrkdown)
        self.assertListEqual(extracted,[TextNode("check out my ",TextType.PLAIN),TextNode("dog",TextType.IMAGE,"dog.com"),TextNode(" and my cat ",TextType.PLAIN),TextNode("meow",TextType.IMAGE,"kitty.org")])


    def test_SplitNodesLink(self):
        #also catches the no empty nodes added
        mrkdown=[TextNode(
        "This is plain text with a link [to boot dev](https://www.boot.dev)",
        TextType.PLAIN,
        )]

        extracted=split_nodes_link(mrkdown)

        self.assertListEqual(extracted,[TextNode("This is plain text with a link ", TextType.PLAIN),TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),])

    def test_onlyLink(self):
        mrkdown=[TextNode("[only a link](toyou.com)",TextType.PLAIN)]
        extracted=split_nodes_link(mrkdown)
        self.assertListEqual(extracted,[TextNode("only a link",TextType.LINK,"toyou.com")])


        



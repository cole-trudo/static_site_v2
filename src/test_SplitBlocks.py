import unittest
from SplitBlocks import markdown_to_blocks, block_to_block_type,BlockType


class TestSplitBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



    def test_markdown_to_blocks_NewLine(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
\n
\n
\n
"""
            blocks = markdown_to_blocks(md)
            self.assertListEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )


    def test_code_block(self):

        md="""```
function test() {
console.log("notice the blank line before this function?");
}
```"""
        result=block_to_block_type(md)
        self.assertEqual(result,BlockType.CODE)
    def test_code_header(self):
    #uses three headers to test the range.

        md="""
### I am a header
 """
        self.assertEqual(block_to_block_type(md.strip()),BlockType.HEADING)
    def test_code_header_toomany(self):
    #also test default case for normal paragraph if no other condtions matched

        md="""
########### I am a header, but am I?
 """
        self.assertEqual(block_to_block_type(md.strip()),BlockType.PARAGRAPH)
    def test_header_nospace(self):
        md="""
##see how there's no space?"""
        self.assertEqual(block_to_block_type(md.strip()),BlockType.PARAGRAPH)
    def test_quote_block(self):
        md="""
>Georgewashington was a player"""
        self.assertEqual(block_to_block_type(md.strip()),BlockType.QUOTE)


    def test_unordered_list_block(self):
        md="""
- this is a list
- that goes on
- and on
"""
        self.assertEqual(block_to_block_type(md.strip()),BlockType.UNORDERED_LIST)


    def test_unordered_list_block(self):
        md="""
-this is a list
-that goes on
-and on
-usr forgot to do a space
"""
        self.assertEqual(block_to_block_type(md.strip()),BlockType.PARAGRAPH)
    def test_ordered_list_block(self):
        md="""
1. the first rule of fight club
2. is that you have to
3. increment your lines"""
        self.assertEqual(block_to_block_type(md.strip()),BlockType.ORDERED_LIST)
    def test_ordered_list_2firstline_block(self):
        md="""

2. is that you have to
3. increment your lines"""
        self.assertEqual(block_to_block_type(md.strip()),BlockType.PARAGRAPH)
    def test_ordered_list_not_increment_block(self):
        md="""
1. the first rule of fight club
2. is that you have to
4. increment your lines"""
        self.assertEqual(block_to_block_type(md.strip()),BlockType.PARAGRAPH)
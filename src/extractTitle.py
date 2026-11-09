from SplitBlocks import block_to_block_type,markdown_to_blocks
import re


def extract_title(markdown):

    match = re.search(r'^#\s+(.+)$', markdown, re.MULTILINE)

    if match:
        h1_header=match.group(1).strip(" #\n\t")
        return (h1_header)
    else:
        raise Exception("no h1 header")

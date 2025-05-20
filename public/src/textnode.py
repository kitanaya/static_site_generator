from enum import Enum

class TextType(Enum):
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "anchor_url"
    IMAGES = "alt_text_url"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

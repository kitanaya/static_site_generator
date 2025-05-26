from textnode import TextType, TextNode

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for old_node in old_nodes:
#         if old_node.text_type == TextType.TEXT:
#             pieces = old_node.text.split(delimiter)
#             if len(pieces) % 2 == 0:
#                 raise Exception("Invalid Markdown. Might be missing a matching(closing) delimiter.")
#             for i in range(len(pieces)):
#                 if i % 2 == 0:
#                    new_nodes.append(TextNode(pieces[i], TextType.TEXT))
#                 else:
#                     new_nodes.append(TextNode(pieces[i], text_type))
#         else:
#             new_nodes.append(old_node)
                
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            split_nodes = []
            pieces = old_node.text.split(delimiter)
            if len(pieces) % 2 == 0:
                raise Exception("Invalid Markdown. Might be missing a matching(closing) delimiter.")
            for i in range(len(pieces)):
                if i % 2 == 0:
                   split_nodes.append(TextNode(pieces[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(pieces[i], text_type))

            new_nodes.extend(split_nodes)
        else:
            new_nodes.append(old_node)
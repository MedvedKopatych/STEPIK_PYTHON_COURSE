from xml.etree import ElementTree

tree = ElementTree.parse('XML_test.xml')
root = tree.getroot()
colors = {'red': 0, 'blue': 0, 'green': 0}
print(root.tag, root.attrib)
print(type(root.tag), type(root.attrib))


def get_children(root, level=1):
    if root.attrib['color'] in colors.keys():
        colors[root.attrib['color']] += level
        level += 1
        for child in root:
            get_children(child, level=level)


get_children(root, level=1)

print(colors['red'], colors['green'], colors['blue'])

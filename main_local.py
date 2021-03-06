import bs4
from bs4 import BeautifulSoup
# import lxml

try:
    with open(
            "website.html"
            , encoding="utf-8"
    ) as fp:
        contents = fp.read()
except FileNotFoundError as fnfe:
    print(f"ERROR| {fnfe}\nexiting...")
    exit(1)
except UnicodeDecodeError as ude:
    print(f"ERROR| {ude}\nexiting...")
    exit(2)
else:
    # print(contents)
    pass

# soup = BeautifulSoup(contents, "lxml")
soup = BeautifulSoup(contents, "html.parser")
#
#   print all html
#
# print(soup)
print(soup.prettify())
#
#   print some tags
#
print(soup.title)
print(soup.title.name)
#
print(soup.a)                           # get the first a tag
print(soup.li)                          # get the first li tag
#
#   get collection of tags
#
a_tags = soup.find_all(name="a")        # get all of the anchor tags
print(a_tags)
#
p_tags = soup.find_all(name="p")        # get all of the paragraph tags
print(p_tags)
#
#   print tag attributes
#
tag: bs4.element.Tag = None
for tag in a_tags:
    print(tag.getText())                # get the text inside the tag
    print(tag.get("href"))              # get the content of the href attribute
#
#   find a specific tag
#
h1_name: bs4.element.Tag = soup.find(name="h1", id="name")
print(h1_name)
#
section_heading: bs4.element.Tag = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))
#
#   find a nested tag with CSS selectors
#
nested_a = soup.select_one(selector="p a")          # tag
print(nested_a)

id_name = soup.select_one(selector="#name")         # id
print(id_name)

class_heading = soup.select(selector=".heading")    # class
print(class_heading)

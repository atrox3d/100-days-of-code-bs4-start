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
print(soup.title)
print(soup.title.name)

# print(soup)
print(soup.prettify())

print(soup.a)   # get the first a tag
print(soup.li)  # get the first li tag



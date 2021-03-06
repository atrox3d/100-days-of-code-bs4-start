import bs4
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

anchors = soup.find_all(name="a", class_="storylink")
a: bs4.Tag
article_texts = []
article_links = []
for a in anchors:
    text = a.getText()
    article_texts.append(text)

    link = a.get("href")
    article_links.append(link)

spans = soup.find_all(name="span", class_="score")
score: bs4.Tag
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

index = article_upvotes.index(max(article_upvotes))

print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])

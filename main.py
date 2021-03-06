import bs4
from bs4 import BeautifulSoup
import requests

# this url does not work due to react
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "http://web.archive.org/web/20200322005914/https://www.empireonline.com/movies/features/best-movies-2/"
INPUT_FILENAME = "movies.html"
OUTPUT_FILENAME = "movies.txt"


def get_webpage(url):
    #
    #   get webpage as text
    #
    response = requests.get(url)
    webpage = response.text
    return webpage


def save_webpage(filename, webpage):
    #
    #   save webpage to file
    #
    with open(filename, "w") as fp:
        fp.write(webpage)


def load_webpage(filename):
    #
    #   load webpage from file
    #
    with open(filename) as fp:
        webpage = fp.read()
        return webpage


try:
    #
    #   if file exist, already downloaded, goto else:
    #
    with open(INPUT_FILENAME) as fp:
        pass
except FileNotFoundError:
    print(f"{INPUT_FILENAME} does not exists")
    print(f"downloading {URL}...")
    webpage = get_webpage(URL)
    print(f"saving {URL} to {INPUT_FILENAME}...")
    save_webpage(INPUT_FILENAME, webpage)
else:
    print(f"{INPUT_FILENAME} exists")
    print(f"loading {URL} from {INPUT_FILENAME}...")
    webpage = load_webpage(INPUT_FILENAME)
finally:
    pass
    # print(webpage)


soup = BeautifulSoup(webpage, "html.parser")

h3s = soup.find_all(name="h3", class_="title")
h3s.reverse()

h3: bs4.Tag
movies = [h3.getText() for h3 in h3s]

print(f"Creating {OUTPUT_FILENAME}")
with open(OUTPUT_FILENAME, "w", encoding="utf-8") as fp:
    fp.write("\n".join(movies))

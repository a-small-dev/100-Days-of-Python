import requests, bs4
from bs4 import BeautifulSoup

movie_list = []

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
html_data = BeautifulSoup(response.text, "html.parser")

movies = html_data.find_all(name="h3", class_="title")
for movie in movies:
    movie_list.append(movie.get_text())

with open("Top 100 Movies.txt", "w") as file:
    for movie in movie_list[::-1]:
        try:
            file.write(f"{movie}\n")
        except UnicodeEncodeError:
            pass
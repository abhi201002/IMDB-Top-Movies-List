from bs4 import BeautifulSoup
import time
from csv import writer
import requests

def Top_movies():
    movie = requests.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm').text

    soup = BeautifulSoup(movie,'lxml')
    List = soup.find('tbody',class_= 'lister-list')
    items = List.find_all('tr')
    with open('IMBD_Most_popular_movies/Top Movies.csv','w',encoding='utf8',newline='') as f:
        Write = writer(f)
        Write.writerow(['S no.','Name','Link','Year',"Directors","Actors",'IMDB rating'])
        for i,item in enumerate(items):
            title = item.find('td',class_='titleColumn')
            Title = title.a.text
            Directed = title.a['title'].split('(dir.)')
            director = Directed[0]
            actors = Directed[1][2:]
            about = f"https://www.imdb.com{title.a['href']}"
            year = title.find('span',class_='secondaryInfo').text[1:-1]
            rating = item.find('td',class_= 'ratingColumn imdbRating').strong
            if rating == None:
                rating = "NA"
            else:
                rating = float(rating.text)
            Write.writerow([i+1,Title,about,year,director,actors,rating])
            # print(actors)

if __name__ == '__main__':
    while True:
        Top_movies()
        print("List will be updated in 10 minutes....")
        time.sleep(6000)
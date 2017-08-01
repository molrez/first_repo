#!/Anaconda3/python
# compadre-toolkit

'''
description
'''

#----------------------------------------------------------------------#

from bs4 import BeautifulSoup
import requests

def main():
    counter = 1
    root_url = "https://www.netflix.com/browse/genre/"
    while counter < 100:
        str_counter = str(counter)
        url = root_url + str_counter
        f = requests.get(url)
        soup = BeautifulSoup(f.content, 'html.parser')
        genre_title = soup.find( "span", { 'class' : 'genreTitle' } )
        print( str_counter, genre_title, url )
        counter +=1


#----------------------------------------------------------------------#
if __name__ == "__main__" :
    main( )

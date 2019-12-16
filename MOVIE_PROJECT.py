import imdb
hr=imdb.IMDb()
movie_name=input("enter the movie name")
movies=hr.search_movie(str(movie_name))
index=movies[0].getID()
movie=hr.get_movie(index)
title=movie['title']
year=movie['year']
cast=movie['cast']
l=','.join(map(str,cast))
print("Movie Title is:  ",title)
print("Released year:  ",year)
print("Movie Cast:  ",l)

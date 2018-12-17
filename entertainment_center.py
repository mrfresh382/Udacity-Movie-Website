import media
import fresh_tomatoes

bladeRunner = media.Movie("Blade Runner", "Look at a dystopian Los Angeles in 2015 following a Police Officer whose jobs is to hunt down rogue androids", "https://m.media-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,671,1000_AL_.jpg","https://www.youtube.com/watch?v=eogpIG53Cis")
starWars5= media.Movie("Star Wars: The Empire Strikes Back","The Rebel Alliance is on the run and Luke Skywalker trains to become a Jedi Knight", "https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,641,1000_AL_.jpg","https://www.youtube.com/watch?v=JNwNXF9Y6kY")
rocketeer=media.Movie("The Rocketeer","Story of a jetpack that falls into the wrong hands of a race pilot and his mechanic", "https://m.media-amazon.com/images/M/MV5BN2ZiMjkwNWYtZWRjNy00YTYxLWI1ZWYtODI0NTA5YTg4ZDIxXkEyXkFqcGdeQXVyNDA5ODIzMDk@._V1_SY1000_CR0,0,674,1000_AL_.jpg","https://www.youtube.com/watch?v=Gi0Et31E7s4")
tombstone= media.Movie("Tombstone","Western Lawman Wyatt Earp and his brother Morgan move into Tombstone, Arizona and are at odds with Cowboys Johny Ringo and Curly Bill","https://m.media-amazon.com/images/M/MV5BODRkYzA4MGItODE2MC00ZjkwLWI2NDEtYzU1NzFiZGU1YzA0XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg","https://www.youtube.com/watch?v=XTWYKf5hXIg")
tLnDnLA=media.Movie("To Live and Die in LA","2 Secret Service agents track down a counterfeiter, teaches a valuable lesson about the consequences of too much self-rightousness", "https://m.media-amazon.com/images/M/MV5BMTQzOGQwMDktYWE3ZS00MTUzLTkxNDctN2I1NTlmYWI2NDBiL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_SX680_AL_.jpg", "https://www.youtube.com/watch?v=I5JI_RclmIg")
oBWAT=media.Movie("O Brother Where Art Thou?","Story of escapees from a 1930 chaingang stumble into becoming a one-hit wonder", "https://m.media-amazon.com/images/M/MV5BMjZkOTdmMWItOTkyNy00MDdjLTlhNTQtYzU3MzdhZjA0ZDEyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

movies = [bladeRunner, starWars5, rocketeer,tombstone, tLnDnLA, oBWAT]
fresh_tomatoes.open_movies_page(movies)
# this calls the open_movies_page function in the fresh_tomatoes file
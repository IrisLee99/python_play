current_movies = {
    "Inception": "7:00 PM",
    "The Dark Knight": "8:00 PM",
    "Interstellar": "9:00 PM"
}

print('we are showing the current movie schedule:')
for movie, showtime in current_movies.items():
    print(f"{movie}: {showtime}")


movie_name = input("Enter the movie name would you like to watch: ")
if movie_name in current_movies:
    print(f"The showtime for {movie_name} is {current_movies[movie_name]}.")
    print('showtime is', current_movies[movie_name])
else:
      print("Movie not found.")
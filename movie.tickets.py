class Movie:
    def __init__(self, title, showtime, seatsavailable, price):
        self.title = title
        self.showtime = showtime
        self.seatsavailable = seatsavailable
        self.price = price

class BookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        for i, movie in enumerate(self.movies):
            print(f"{i + 1}. {movie.title} ({movie.showtime}) - ${movie.price} | Seats Available: {movie.seatsavailable}")

    def book_ticket(self, movie_index, num_tickets):
        movie = self.movies[movie_index]
        if movie.seatsavailable >= num_tickets:
            movie.seatsavailable -= num_tickets
            print(f"Successfully booked {num_tickets} tickets for {movie.title} ({movie.showtime})")
            print(f"Total Amount: ${num_tickets * movie.price}")
        else:
            print("Sorry,enough seats are not available.")

bookingsystem = BookingSystem()

bookingsystem.add_movie(Movie("Moneyheist", "10:00 AM", 100, 50))
bookingsystem.add_movie(Movie("Avengers", "1:00 PM", 80, 80))
bookingsystem.add_movie(Movie("The Jungle Book", "4:00 PM", 120, 10))

bookingsystem.display_movies()

movie_index = int(input("Enter the movie number to book tickets: ")) - 1
num_tickets = int(input("Enter the number of tickets to book: "))
bookingsystem.book_ticket(movie_index, num_tickets)
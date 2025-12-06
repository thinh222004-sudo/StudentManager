class Movie:
    def __init__(self, movie_id, title, duration):
        self.movie_id = movie_id
        self.title = title
        self.duration = duration 

    def show_info(self):
        print(f"Movie: {self.title} - Duration: {self.duration} minutes")
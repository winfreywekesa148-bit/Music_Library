class Song:
    count = 0 #class atribute
    genres = []
    artist = []
    genre_count = 0
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres +=1
        Song.artist +=1
        Song.genre_count +=1
        Song.artist_count +=1

    @classmethod
    def add_song_to_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
    
    def add_to_genres(cls, genre):
        if genre in not cls.genre:
            cls.genre.append(genre)
        return Song.genre_count + 1
        

    def add_to_artists(cls, artist):
        if artist is not cls.artist:
            cls.artist.append(artist)
            return Song.artist_count + 1
        

    def add_to_genre_count(cls):
        return Song.genre_count + 1

    def add_to_artists_count(cls):
        return Song.artist_count + 1

    

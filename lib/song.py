class Song:
    count = 0 #class atribute
    genres = []
    artists = []
    genre_count = {}
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
    def add_song_to_count(cls, count):
        return count + 1 #class method
    
    def add_to_genres(cls, genre):
        if genre not in cls.genre:
            cls.genre.append(genre)
        return Song.genre_count + 1
        

    def add_to_artists(cls, artist):
        if artist not is cls.artist:
            cls.artist.append(artist)
            return Song.artist_count + 1
        

    def add_to_genre_count(cls):
        return Song.genre_count + 1

    def add_to_artists_count(cls):
        return Song.artist_count + 1

    

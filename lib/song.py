class Song:
     
    count = 0
    songs = []
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        
        Song.songs.append(name)


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in Song.genre_count.keys():
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in Song.artist_count.keys():
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1

            
               


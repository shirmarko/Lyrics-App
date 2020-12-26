import lyricsgenius
from flask import Flask
from flask import jsonify
from flask import request
from wordsAnalyzer import WordsAnalyzer
from placesExtractor import PlacesExtractor
from placesCreator import PlacesCreator
from nltk.tokenize import word_tokenize
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
wordsAnalyzer = WordsAnalyzer()
placesExtractor = PlacesExtractor()
placesCreator = PlacesCreator()

# params: artist, k
# The function creates a wordcloud of the k best songs of the artist
# example: http://127.0.0.1:5000/wordsCloud?artist=BRITNEY SPEARS&k=3
@app.route('/wordsCloud', methods=['GET'])
def wordsCloud():
    try:
        print("wordsCloud....")
        artist_name = request.args['artist']
        num_of_songs = int(request.args['k'])
        tup = get_songs_lyrics(artist_name, num_of_songs)
        lyrics = tup[0] # lyrics the best num_of_songs of the artist  
        songs = tup[1] # list of details of each song
        names= []
        for song in songs:
            names.append(song.title)
        wordsAnalyzer.create_word_cloud(lyrics, names)
        return "ok",200
    except ValueError:
        return "We Couldn't find songs for you" ,500
    except:
        return "internal error",500

# params: artist
# The function creates a graph of statistics of the lyrics of the best artist's song
# example: http://127.0.0.1:5000/wordsStatistics?artist=BRITNEY SPEARS
@app.route('/wordsStatistics', methods=['GET'])
def wordsStatistics():
    try:
        print("wordsStatistics....")
        artist_name = request.args['artist']
        tup = get_songs_lyrics(artist_name, 1)
        lyrics = tup[0] # lyrics the best num_of_songs of the artist 
        songs = tup[1] # list of details of each song
        wordsAnalyzer.create_statistics(lyrics, songs[0].title)
        return "ok", 200
    except ValueError:
        return "We Couldn't find songs for you" ,500
    except:
        return "internal error",500

# params: artist, k
# returns: list of places that appear in the k best songs of the artist
# example: http://127.0.0.1:5000/places?artist=BRITNEY SPEARS&k=3
@app.route('/places', methods=['GET'])
def places():
    try:
        print("places....")
        artist_name = request.args['artist']
        num_of_songs = int(request.args['k'])
        tup = get_songs_lyrics(artist_name, num_of_songs)
        lyrics = tup[0] # lyrics the best num_of_songs of the artist 
        places_from_songs = placesExtractor.find_places_in_lyrics(lyrics) # list of the places that appear in the songs
        songs = tup[1] # list of details of each song
        places= []
        # create list of locations with details to the map
        for song in songs:
            places = placesCreator.create_places_list(places, places_from_songs, song)

        json_places = []
        for p in places:
            place_dict = p.to_json()
            json_places.append(place_dict)
        return jsonify(json_places)
    except ValueError:
        return "We Couldn't find songs for you" ,500
    except:
        return "internal error",500

# returns one string of all the lyrics songs
def get_songs_lyrics(artist_name, num_of_songs):
    genius = lyricsgenius.Genius('ifAv5R1fL3F6sMRXubPSueXJ3AlOe_gUu7MftBKJYR5dK8xMvw2_JCmgMc4ltmmi')
    artist = genius.search_artist(artist_name, max_songs= num_of_songs)
    lyrics= ""
    if artist is not None:
        for song in artist.songs:
            lyrics += song.lyrics
    if lyrics== "" or artist is None:
        raise ValueError
    return (lyrics,artist.songs)


        
if __name__=='__main__':
    app.run(debug=True)


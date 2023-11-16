import random

cart = []

def welcome():
    print("Welcome to Spotify!")

def skipSong(currentSong, songs):
    i = 0
    for song in songs:
        if currentSong == song:
            break
        else:
            i += 1
    return songs[i+1]

def addToCart(song, cart):
    cart.append(song)

def calcCart():
    total = 0.00
    for song in cart:
        total += song.cost 
    return total

class Song():
    def __init__(self, name = "", artist = "", duration = "", timesplayed = "", releasedate = "", cost = 0.00):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.timesplayed = timesplayed
        self.releasedate = releasedate
        self.cost = cost


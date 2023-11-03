import parent

class Song():
    def __init__(self, name = "", artist = "", duration = "", timesplayed = "", releasedate = "", cost = 0.00):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.timesplayed = timesplayed
        self.releasedate = releasedate
        self.cost = cost

def main():
    despacito = Song("Despacito”, "Luis Fonsi ft. Daddy Yankee", "'3:47'", 1.9 Billion, "2017", 1.00)
    songs = []
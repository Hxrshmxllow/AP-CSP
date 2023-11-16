from parent import *

def main():
    despacito = Song("Despacito", "Luis Fonsi ft. Daddy Yankee", "3:47", "1.9 Billion", "2017", 1.00)
    chammakchallo = Song("Chammak Challo", "Akon", "4:11", "33.9 Million", "2011", 1.00)
    godsplan = Song("God's Plan", "Drake", "3:18", "2.0 Billion", "2018", 1.00)
    closer = Song("Closer", "The Chainsmokers ft. Halsey", "4:07", "2.3 Billion", "2018", 1.00)
    onedance = Song("One Dance", "Drake", "2:55", "2 Billion", "2.8 Billion", 1.00)
    songs = [despacito, chammakchallo, godsplan, closer, onedance]
    welcome()
    currentsong = skipSong(despacito, songs)
    addToCart(closer, cart)
    total = calcCart()
    print("Current Song: " + currentsong.name)
    print("Cart Total: $" + str(total))
    
    songs = {"Despacito": "despacito", 
             "Chammak Challo": "chammakchallo", 
             "God's Plan": "godsplan", 
             "Closer": "closer", 
             "One Dance": "onedance"}
    i = 0
    for key in songs:
        print(str(i+1) + ": " + songs[key])
        i += 1
    
    choice = int(input("Pick a song: "))
    print(songs["One Dance"])


main()
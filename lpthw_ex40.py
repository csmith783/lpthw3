# Exercise 40
# Modules, Classes, and Objects 

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
song1 = ["Happy birthday to you",
                    "I don't want to get sues",
                    "So i'll stop right here."]

happy_bday = Song(song1)

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells."])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


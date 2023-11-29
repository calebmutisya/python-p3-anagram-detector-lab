# your code goes here!
class Anagram():
    def __init__(self, word):
        self.word=word 
    
    def match(self,list):
        return [w for w in list if sorted(w.lower())== sorted(self.word.lower()) and w.lower() != self.word.lower()]
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
import json
import random

class Game:
    level = 4
    dictionary = {}
    winner_word = ""
    winner_set = set()
    posible_words = set()

    def __init__(self, level):
        self.level = level
        self.winner_set = set()
        self._loadDictionary()
        self._selectRandomWord()

    def _loadDictionary(self):
        f = open("./data.json", "r")
        self.dictionary = json.load(f)
        f.close()

    def _selectRandomWord(self):
        self.winner_word = random.choice(self.dictionary[str(self.level)])
        print(self.winner_word)
        for i in self.winner_word:
            self.winner_set.add(i)
        self.posible_words = set(self.dictionary[str(self.level)])

    def check(self, word):
        ans = []
        for i in range(len(word)):
            if (word[i] == self.winner_word[i]):
                ans.append('right')
            elif (word[i] in self.winner_set):
                ans.append('medium')
            else:
                ans.append('wrong')
        return ans

    def exists(self, word):
        return (word in self.posible_words)

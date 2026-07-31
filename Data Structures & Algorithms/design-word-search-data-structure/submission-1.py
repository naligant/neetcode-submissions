class WordDictionary:

    def __init__(self):
        self.word_dict = []

    def addWord(self, word: str) -> None:
        self.word_dict.append(word)
    def search(self, word: str) -> bool:
        temp = list(word)
        if '.' not in temp:
            if word not in self.word_dict:
                return False
            else:
                return True
        else:
            for i in range(len(self.word_dict)):
                if len(word) == len(self.word_dict[i]):
                    for j in range(len(word)):
                        if word[j] != '.':
                            if word[j] != self.word_dict[i][j]:
                                break
                        if j == len(word)-1:
                            if word[j] == self.word_dict[i][j] or word[j] == '.':
                                return True
            return False



class TextAnalyzer(object):
    def __init__(self, text):
        self.text = text
        self.text= self.text.lower()
        self.text = self.text.replace('.', '').replace('!','').replace('?','').replace(',','').replace(';','')

    def freqAll(self) -> dict[str,int]: 
        wordList = self.text.split(' ')
        freqMap = {}
        for word in wordList:
            freqMap[word] = wordList.count(word)
        return freqMap
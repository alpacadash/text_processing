from pathlib import Path
import sys

class TokenList:
    def __init__(self):
        self.tokens = []
#The runtime complexity of split_by_non_alpha is O(n^3) because self.tokens.append() which has O(1) complexity is nested with
#two nested for loops and is in "if" which has search_content which has O(n) complexity as its condition. Therefore,
#O(n)*O(n)*O(n)*O(1) = O(n^3)
    def tokenize(self, path):
        file = None
        try:
            file =open(path, mode='r', encoding='utf8')
            for line in file:
                line = line.strip()
                arr = self.split_by_non_alpha(line)
                for content in arr:
                    if not(self.search_content(content.lower())):
                        self.tokens.append((content.lower(),1))

        except(FileNotFoundError,IOError):
            return 'Invalid File'
            exit()

        finally:
            file.close()
#The runtime complexity of split_by_non_alpha is O(n) because this function iterates through each character in the string once
    def split_by_non_alpha(self, string):
        list = []
        temp = ''
        for ch in string:
            if ch.isalpha() or ch.isdigit():
                temp += ch
            else:
                if temp:
                    list.append(temp)
                    temp = ''
        if temp:
            list.append(temp)
        return list
#The runtime complexity of search_content is O(n) because this function iterates through each token in the list of tokens
    def search_content(self, content):
        for name, _ in self.tokens:
            if name == content:
                return True
        return False

if __name__ == '__main__':
    token1 = TokenList()
    token2 = TokenList()
    path1 = Path(sys.argv[1])
    path2 = Path(sys.argv[2])
    token1.tokenize(path1)
    token2.tokenize(path2)
    num = 0
    for name, _ in token1.tokens:
        for content, _ in token2.tokens:
            if(name == content):
                num += 1
    print(num)

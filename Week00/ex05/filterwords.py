import sys
import string

def count_non_punc(word):

    count = 0
    for c in word:
        if c not in string.punctuation:
            count += 1
    return count


def clear_word(word):

    new_word = ""
    for c in word:
        if c not in string.punctuation:
            new_word += c
    return new_word


def filterwords():

    if len(sys.argv) == 3:
        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            print("ERROR")
            return
        
        if isinstance(s, str) and isinstance(n, int):
            words = s.split(" ")
            result = [clear_word(word) for word in words if count_non_punc(word) > n]
            print(result)
        else:
            print("ERROR")
    else:
        print("ERROR")

if __name__ == "__main__":
    filterwords()

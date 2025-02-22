import string


def text_analyzer(text=None):

    if text is None:
        text = input("What is the text to analyze?\n")
    if isinstance(text, str):
        lower = 0
        upper = 0
        punctuation = 0
        spaces = text.count(" ")
        printable = len(text)
        for c in text:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c in string.punctuation:
                punctuation += 1
        print(f"The text contains {printable} character(s):")
        print(f"- {upper} upper letter(s)")
        print(f"- {lower} lower letter(s)")
        print(f"- {punctuation} punctuation mark(s)")
        print(f"- {spaces} space(s)")
    else:
        print("AssertionError: argument is not a string")


if __name__ == "__main__":
    text_analyzer()

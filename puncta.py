def collapse_spaces(text):
    result = []
    for char in text:
        if char == " ":
            if len(result) > 0 and result[-1] == " ":
                continue
        result.append(char)
    return "".join(result)


def fix_punctuation_space(text):
    result = []
    punctuations = ".,!?:;/"
    for i in range(len(text)):
        char = text[i]
        if char in punctuations:
            while len(result) > 0 and result[-1] == " ":
                result.pop()
            result.append(char)
            if i + 1 < len(text):
                next_char = text[i+1]
                if next_char != " " and next_char != "\n" and next_char not in  punctuations:
                    result.append(" ")
        else:
            result.append(char)
    return "".join(result)
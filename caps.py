
def capitalize(text):
    result = list(text)
    capitalize_next = True

    for i in range(len(text)):
        char = result[i]

        if char == "\n":
            capitalize_next = True
            continue

        if char.isspace():
            continue
        
        if capitalize_next and char.isalpha():
            result[i] = char.upper()
            capitalize_next = False
        elif not char.isspace():
            capitalize_next = False

        if char == "." or char == "!" or char == "?":
             capitalize_next = True

    return "".join(result)

def fix_quotes(text):
    result = []
    double_open = True
    single_open = True

    i = 0 
    while i < len(text):
        char = text[i]

        if char == '"' or char ==  "'":
            is_double = (char == '"')
            is_open = (is_double and double_open) or ( not is_double and single_open)
            if is_open:
                result.append(char)
                i += 1
                while i < len(text) and text[i] == " ":
                    i += 1

                if is_double:
                    double_open = not double_open
                else:
                    single_open = not single_open
                continue

            else:
                while len(result) > 0 and result[-1] == " ":
                    result.pop()
                result.append(char)

                if is_double:
                    double_open = not double_open
                else:
                    single_open = not single_open

        else:
            result.append(char)

        i += 1
        
    return "".join(result)
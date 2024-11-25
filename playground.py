def read_file(file_string):
    file = open(file_string, "r")
    read_file = file.read()
    clean_string = "".join(char for char in read_file if char.isalnum() or char == " ")
    return clean_string

def text_analysis(text):
    clean_string = text.lower().split()
    accum = {}
    for word in clean_string:
        if word not in accum:
            accum[word] = 1
        else:
            accum[word] += 1
    sorted_dict = dict(sorted(accum.items(), key=lambda item: item[1], reverse = True))
    return sorted_dict




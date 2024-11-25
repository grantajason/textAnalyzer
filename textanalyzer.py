def read_file(file_string):
    file = open(file_string, "r")
    read_file = file.read()
    clean_string = "".join(char for char in read_file if char.isalnum() or char == " ")
    return clean_string

def load_exclusions():
    file = open("Exclusions.txt", "r")
    exclusions = file.read()
    return exclusions

def text_analysis(text):
    clean_string = text.lower().split()
    exclusions = load_exclusions()
    accum = {}
    for word in clean_string:
        if word not in accum and word not in exclusions:
            accum[word] = 1
        elif word not in exclusions:
            accum[word] += 1
    sorted_dict = dict(sorted(accum.items(), key=lambda item: item[1], reverse = True))
    return sorted_dict

file_string = "RIVNQ3Letter.txt"
output = read_file(file_string)
result = text_analysis(output)
print(result)

file_string = "TSLAQ3Letter.txt"
output = read_file(file_string)
result = text_analysis(output)
print(result)


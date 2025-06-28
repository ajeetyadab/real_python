import string

import fitz

def clean_text(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation))

def pdf_to_text(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Example usage

text = pdf_to_text("C:/Users/hp/Desktop/hdb.pdf")

def word_frequency_counter(word):
    # word = clean_text(word)
    word_list = word.split()
    word_frequency_dict = {}

    for word in word_list:
        if word in word_frequency_dict:
            word_frequency_dict[word] +=1

        else:
            word_frequency_dict[word] = 1

    return word_frequency_dict

# print(word_frequency_counter(text))

# sorting this dictionary to see which word is most frequent

result = dict(sorted(word_frequency_counter(text).items() ,key = lambda item:item[1],reverse= True))

print(len(result))
# print(result)
with open("output.txt", "w",encoding="utf-8") as f:
    for key, value in result.items():
        f.write(f"{key}: {value}\n")

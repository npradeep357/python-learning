import json
from difflib import get_close_matches

data_file_path = "files/data.json"
data = json.load(open(data_file_path))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.78)) > 0:
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(
            get_close_matches(w, data.keys(), cutoff=0.78)[0]))
        if yn == 'Y':
            return data[get_close_matches(w, data.keys(), cutoff=0.78)[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your input."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
res = translate(word)
if isinstance(res, list):
    for i in res:
        print(i)
else:
    print(res)

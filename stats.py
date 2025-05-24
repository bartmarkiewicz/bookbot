def number_of_words(text):
    return len(text.split());

def char_count(text):
    fullTextLower = text.lower()
    characterCountDict = {}
    for char in fullTextLower:
        if char in characterCountDict:
            characterCountDict[char] += 1
        else:
            characterCountDict[char] = 1
    return characterCountDict

def get_sorted_dict_list(charDict):
    sortedDictList = []
    for key in charDict:
        sortedDictList.append({ "char": key, "num": charDict[key] })


    return sorted(sortedDictList, key=lambda x: x["num"], reverse=True)
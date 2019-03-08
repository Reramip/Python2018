import re

def checkio(text):
    text = "".join(re.findall("[A-Za-z]+" ,text)).lower()
    textDict = {}
    for letter in text:
        if textDict.__contains__(letter):
            textDict[letter] += 1
        else:
            textDict[letter] = 0
    maxNum = max(textDict.values())
    subList = zip(textDict.keys(), textDict.values())
    ansList = []
    for key in textDict.keys():
        if textDict[key] == maxNum:
            ansList.append(key)
    return sorted(ansList)[0]

"""

import string


def checkio(text):

    """

    We iterate through latyn alphabet and count each letter in the text.

    Then 'max' selects the most frequent letter.

    For the case when we have several equal letter,

    'max' selects the first from they.

    """

    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)


"""
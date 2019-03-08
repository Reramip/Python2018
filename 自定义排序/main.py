def lastCharachter(word):
    return word[-1]

def numberOfVowels(word):
    vowels=['a','e','i','o','u']
    total=0
    for vowel in vowels:
        total+=word.count(vowel)
    return total


def main():
    list1=["democratic","suquoia","equals","brrrrrrrr","break","two"]
    
    list1.sort(key=len)
    print("Sorded by length(ascending):")
    print(list1,'\n')

    list1.sort(key=lastCharachter)
    print("Sorted by last character(ascending):")
    print(list1,'\n')
    #equals list1.sort(key=lambda x:x[-1])

    list1.sort(key=numberOfVowels,reverse=True)
    print("Sorted by number of vowels(descending):")
    print(list1,'\n')


main()
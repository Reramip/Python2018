##Translate a word into Pig Latin
word=input("Enter word to translate:  ")
word=word.lower()
if word[0] in ['a','e','i','o','u']:
	trans=word+'w'
else:
	poia=poie=poii=poio=poiu=10000
	if 'a' in word:
		poia=word.find('a')
	if 'e' in word:
		poie=word.find('e')
	if 'i' in word:
		poii=word.find('i')
	if 'o' in word:
		poio=word.find('o')
	if 'u' in word:
		poiu=word.find('u')
	poi=min(poia,poie,poii,poio,poiu)
	trans=word[poi:]+word[:poi]
pig=trans+"ay"
print("The word in Pig Latin is "+pig)
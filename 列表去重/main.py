list1=["qwq","qwq","233","23333"]

##equals list2=list(set(list1)) 
#remove the repeated elements
#not use the function set()

list2=[]
for word in list1:
    if word not in list2:
        list2.append(word)

print(list2)
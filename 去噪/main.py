def checkio(data):
    while(True):
        length = len(data)
        for i in range(length):
            if data.count(data[i]) == 1:
                data.remove(data[i])
                i -= 1
                break
        if length ==0 or i == length - 1:
            break
    return data
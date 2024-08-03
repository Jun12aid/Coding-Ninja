def fav_count(n,inputt):
    sing_count = {}
    for i in inputt:
        if i in sing_count:
            sing_count[i]+=1
        else:
            sing_count[i] = 1
    
    max_count = max(sing_count.values())
    favorite_singers_count = sum(1 for count in sing_count.values() if  count == max_count)
    return favorite_singers_count

n = 5
inputt = [1, 1, 2, 2, 4]
print(fav_count(n, inputt))

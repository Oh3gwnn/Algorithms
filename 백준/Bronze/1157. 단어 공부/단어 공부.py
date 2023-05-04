s = map(str, input())
arr = [i.upper() for i in s]
if len(arr) == 1:
    print(arr[0])
else:
    arr2 = list(set(arr))
    dic = {arr2[i] : 0 for i in range(len(arr2))}
    for i in arr:
        if i in dic:
            dic[i] += 1
    dic = sorted(dic.items(), key = lambda x : -x[1])

    print("?" if dic[0][1] == dic[1][1] else dic[0][0])
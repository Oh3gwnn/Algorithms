def solution(my_string, indices):
    indices.sort(reverse = True)
    lst = list(my_string)
    for i in range(len(indices)):
        lst.pop(indices[i])
    return "".join(lst)
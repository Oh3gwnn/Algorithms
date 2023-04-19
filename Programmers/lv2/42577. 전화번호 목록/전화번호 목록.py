def solution(phone_book):
    dic = {}
    
    for n in phone_book:
        dic[n] = 1
        
    for n in phone_book:
        temp = ''
        for i in n:
            temp += i
            if temp in dic and temp != n:
                return False
    
    return True
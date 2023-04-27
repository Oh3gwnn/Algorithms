''' 메모리초과
n = int(input())
bin_num = ['1']

for i in range(0, n-1):
    for i in range(0, len(bin_num)):
        if bin_num[i] == '0' :
            bin_num[i] = '10'
        elif bin_num[i] == '1' :
            bin_num[i] = '01'

    bin_num = (list(''.join(bin_num)))

bin_num = ''.join(bin_num)
cnt = bin_num.count('01')
print (cnt)
'''

n = int(input())
dp = [0]
for i in range(1, n):
    dp.append(2**(i - 1) - dp[i - 1])
print(dp[n - 1])
alp = [chr(ord('A') + i) for i in range(26)]
flag = False

if (num:=int(input())) % 26 == 0:
    last = 26
    dat = (num - 1) // 26
    flag = True
else:
    last = num % 26
    dat = num // 26

count = 0
wate, test = num, num
ans = []

while wate > 0:
    count += 1
    wate = (wate - 1)// 26

for i in range(count, 0, -1):
    if flag:
        ans.append('Z')
        test = (test - 1) // 26
    else:
        ans.append(alp[test % 26 - 1])
        test //= 26

print(''.join(reversed(ans)))
a, b = min((ansss:=[int(input()), int(input())])), max(ansss)
ba, bb = bin(a)[2:][::-1], bin(b)[2:][::-1]
count = 0
ano = []
result = 0
real = ba

for i in range(b - a):
    ba = str(bin(a + count)[2:])
    for j in range(len(real)):
        ano.append(str(int(ba[j]) & int(real[j])))
    if len(ba) != len(bb):
        for k in range(len(real) + 1, len(ba) + 1):
            if ba[k - 1] == '1':
                ano.append('0')
            else:
                ano.append('1')

    real = ''.join(ano)
    ano = []
    count += 1


print(int(real, 2))

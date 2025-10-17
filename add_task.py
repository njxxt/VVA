import re

f = open(r'C:\Users\Vladi\Downloads\forTEST.txt', 'r+')


zum = re.findall(r'\d+', f.read())
may_count = int(zum[-1]) if zum else 0


def deco(func):
    def wrap(x, y):
        global may_count
        may_count += 1

        f.seek(0)
        f.truncate()

        f.write(str(may_count))
        return print(f"res is {func(x, y)}")

    return wrap

@deco
def teso(x, y):
    return x + y


if input("enter the code for satrt the nuclear war: ") != 'hare emae':
    x = int(input("x = "))
    y = int(input("y = "))
    teso(x, y)
else:
    f.seek(0)
    f.truncate()

print(f"total strats: {may_count}")


f.close()

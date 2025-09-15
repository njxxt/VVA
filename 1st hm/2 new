while True:
    def excel(n):
        res = []

        while n > 0:
            n -= 1
            res.append(chr(ord('A') + n % 26))
            n //= 26

        return ''.join(reversed(res))

    print(excel(int(input())))

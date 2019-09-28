# func 1
def fi1(n):
    if n <= 2:
        return 1
    else:
        return fi1(n-1) + fi1(n-2)


n = 1
while True:
    res = fi1(n)
    if res <= 100:
        print(res)
    else:
        break

    n += 1


# fuc2
def fi2(n):
    fi = list()
    m = 1
    while m <= n:
        if m <= 2:
            fi.append(1)
        else:
            fi.append(fi[-1] + fi[-2])

        m += 1

    return fi


n = 1
while True:
    res = fi2(n)
    if res[-1] >= 100:
        print(res[:-1])
        break

    n += 1

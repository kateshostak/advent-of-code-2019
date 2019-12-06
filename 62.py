import pdb


def count_passwrd(start):
    count = 1
    n = start
    prev = n % 10
    n //= 10
   # pdb.set_trace()
    dupes = False
    while n > 0:
        curr = n % 10
        if curr == prev:
            count += 1
        elif prev < curr:
            return False
        else:
            if count == 2:
                dupes = True
            count = 1
        n //= 10
        prev = curr
    if count == 2:
        return True
    return dupes

def main():
    count = 0
    start, end = 347312, 805915
    for i in range(start, end + 1):
        if count_passwrd(i):
            count += 1
    print(count)

if __name__ == '__main__':
    main()


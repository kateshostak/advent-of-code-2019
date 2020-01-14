def count_passwords(start, end):
    count = 0
    for k in range(start, end + 1):
        passwrd = str(k)
        if is_non_decreasing(passwrd):
            for i in range(10):
                if find_substr(i, passwrd) == 2:
                    count += 1
                    break
    return count

def find_substr(i, passwrd):
    for j in range(6, 1, -1):
        substr = str(i)*j
        if substr in passwrd:
            return j
    return 0

def is_non_decreasing(passwrd):
    for i in range(len(passwrd) - 1):
        if passwrd[i] > passwrd[i+1]:
            return False
    return True


def main():
    start, end = 347312, 805915
    #start, end = 372037, 905157
    print(count_passwords(start, end))

if __name__ == '__main__':
    main()

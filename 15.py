def count_elem(hay, needle):
    counter = 0
    for elem in hay:
        if elem == needle:
            counter += 1
    return counter

def get_input():
    arr = []
    with open('15.txt') as f:
        for elem in f.read().strip():
            arr.append(int(elem))

    return arr

def find_min_layer(arr):
    min_count = 25*6
    min_layer = []
    for i in range(0, len(arr), 25*6):
        layer = arr[i:i+25*6]
        count = count_elem(layer, 0)
        if count < min_count:
            min_count, min_layer = count, layer
    return min_layer

def main():
    arr = get_input()
    min_layer = find_min_layer(arr)
    ones = count_elem(min_layer, 1)
    twos = count_elem(min_layer, 2)
    print(ones*twos)


if __name__ == '__main__':
    main()

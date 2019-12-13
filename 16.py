def count_elem(hay, needle):
    counter = 0
    for elem in hay:
        if elem == needle:
            counter += 1
    return counter

def get_input():
    with open('15.txt') as f:
        arr = [int(elem) for elem in f.read().strip()]
        return arr

def build_layers(arr, l, w):
    return [arr[i:i+l*w] for i in range(0, len(arr), l*w)]

def build_image(layers, l, w):
    image = []
    for i in range(w):
        row = []
        for j in range(l):
            for layer in layers:
                pixel = layer[l*i + j]
                if pixel == 0 or pixel == 1:
                    row.append(pixel)
                    break
        image.append(row)
    return image

def print_image(image, l, w):
    for i in range(w):
        for j in range(l):
            pixel = image[i][j]
            if j != l-1:
                if pixel == 1:
                    print('#', end='')
                else:
                    print(' ', end='')
            else:
                if pixel == 1:
                    print('#')
                else:
                    print(' ')

def main():
    arr = get_input()
    l = 25
    w = 6
    layers = build_layers(arr, l, w)
    image = build_image(layers, l, w)
    print_image(image, l, w)
if __name__ == '__main__':
    main()

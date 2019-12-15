import pdb
from collections import namedtuple

def block(arr2, point, step_i, step_j, length, width):
    i = point.x + step_i*2
    j = point.y + step_j*2
    while i < length and j < width:
        arr2[i][j] = 0
        i += step_i
        j += step_j

def fourth_quarter(arr, point, length, width):
    asteroids = 0
    i = 1
    j = 1
    while i < width:
        j = 1
        while j < length:
            if arr[point.x + i][point.y + j] == '#':
                asteroids += 1
                block(arr, point, i, j, length, width)
            j += 1
        i += 1
    return asteroids

def  main():
    point = namedtuple('Point', ['x', 'y'])
    a = point(0, 0)
    arr = [
            ['#', '1', '2', '3'],
            ['4', '#', '#', '#'],
            ['8', '9', '10', '11'],
            ['12', '13', '14', '15']
            ]
    arr2 = arr.copy()
    print(fourth_quarter(arr, a, 4, 4))
    for row in arr2:
        print(*row)

if __name__ == '__main__':
    main()

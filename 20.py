import pdb
from collections import namedtuple


def block(arr2, point, step_j, step_i, columns, rows):
    i = point.row + step_i
    j = point.column + step_j
    if step_i > 0 and step_j > 0:
        while i < rows and j < columns:
            arr2[i][j] = 'o'
            i += step_i
            j += step_j
    elif step_i < 0 and step_j > 0:
        while i > rows and j < columns:
            arr2[i][j] = 'o'
            i += step_i
            j += step_j
    elif step_i > 0 and step_j < 0:
        while i < rows and j > columns:
            arr2[i][j] = 'o'
            i += step_i
            j += step_j
    else:
        while i > rows and j > columns:
            arr2[i][j] = 'o'
            i += step_i
            j += step_j


def count_asteroids(arr, point):
    as1 = count_quarter(arr, point, 1, -1, len(arr[0]), -1)
    as2 = count_quarter(arr, point, -1, -1, -1, -1)
    as3 = count_quarter(arr, point, -1, 1, -1, len(arr))
    as4 = count_quarter(arr, point, 1, 1, len(arr[0]), len(arr))
    as5 = count_cross(arr, point)
    return as1 + as2 + as3 + as4 + as5


def count_cross(arr, point):
    asteroids = 0
    for j in range(point.column + 1, len(arr[0])):
        if arr[point.row][j] == '#':
            asteroids += 1
            break

    for j in range(point.column - 1, -1, -1):
        if arr[point.row][j] == '#':
            asteroids += 1
            break

    for i in range(point.row+ 1, len(arr)):
        if arr[i][point.column] == '#':
            asteroids += 1
            break

    for i in range(point.row - 1, -1, -1):
        if arr[i][point.column] == '#':
            asteroids += 1
            break

    return asteroids


def count_quarter(arr, point, step_column, step_row, columns, rows):
    asteroids = 0
    row = point.row + step_row
    while row != rows:
        column = point.column + step_column
        while column != columns:
            if arr[row][column] == '#':
                asteroids += 1
                step_i = row - point.row
                step_j = column - point.column
                block(arr, point, step_j, step_i, columns, rows)
            column  += step_column
        row += step_row
    return asteroids


def find_best_asteroid(arr):
    point = namedtuple('Point', ['row', 'column'])
    asteroids = {}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '#':
                arr1 = []
                for row in arr:
                    arr1.append(row.copy())
                ast = point(i,j)
                asteroids[ast] = count_asteroids(arr1, ast)
    #return max(asteroids, key=lambda elem: asteroids[elem])
    return asteroids


def main():
    #point = namedtuple('Point', ['row', 'column'])
    #a = point(0, 3)
    arr = [
            ['#', 'x', 'x', 'x'],
            ['x', '#', '#', '#'],
            ['x', '#', '#', 'x'],
            ['x', 'x', 'x', 'x']
            ]
    arr = [
            ['.', '#', '.', '.', '#'],
            ['.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#'],
            ['.', '.', '.', '.', '#'],
            ['.', '.', '.', '#', '#']
            ]

    #arr[a.row][a.column] = '*'
    #as4 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))
    #as1 = count_quarter(arr, a, 1, -1, len(arr[0]), -1)
    #as2 = count_quarter(arr, a, -1, -1, -1, -1)
    #as3 = count_quarter(arr, a, -1, 1, -1, len(arr))

    #for row in arr:
        #print(*row) # noqa

    astr = find_best_asteroid(arr)
    for key, value in astr.items():
        a = key
        arr[a.row][a.column] = value

    for row in arr:
        print(*row)

if __name__ == '__main__':
    main()

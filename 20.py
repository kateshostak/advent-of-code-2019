import pdb
from collections import namedtuple


def block(arr2, point, step_j, step_i, columns, rows):
    i = point.row + step_i
    j = point.column + step_j
    #pdb.set_trace()
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
    as1 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))


def count_quarter(arr, point, step_column, step_row, columns, rows):
    asteroids = 0
    row = point.row + step_row
    #pdb.set_trace()
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


def main():
    point = namedtuple('Point', ['row', 'column'])
    a = point(0, 3)
    arr = [
            ['#', 'x', 'x', 'x'],
            ['x', '#', '#', '#'],
            ['x', '#', '#', 'x'],
            ['x', 'x', 'x', 'x']
            ]
    arr[a.row][a.column] = '*'
    #as4 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))
    #as1 = count_quarter(arr, a, 1, -1, len(arr[0]), -1)
    #as2 = count_quarter(arr, a, -1, -1, -1, -1)
    as3 = count_quarter(arr, a, -1, 1, -1, len(arr))

    for row in arr:
        print(*row) # noqa


if __name__ == '__main__':
    main()

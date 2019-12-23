import pdb
from collections import namedtuple


def block(arr2, point, step_i, step_j, columns, rows):
    i = point.row + step_i
    j = point.column + step_j
    #pdb.set_trace()
    while i < rows and j < columns:
        arr2[i][j] = 0
        i += step_i
        j += step_j


def count_asteroids(arr, point):
    as1 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))


def count_quarter(arr, point, step_row, step_column, columns, rows):
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
                block(arr, point, step_i, step_j, columns, rows)
            column  += step_column
        row += step_row
    return asteroids


def main():
    point = namedtuple('Point', ['row', 'column'])
    a = point(0, 0)
    a = point(0, 1)
    a = point(0, 2)
    a = point(0, 3)
    a = point(1, 1)
    a = point(2, 2)

    arr = [
            ['#', 'x', 'x', 'x'],
            ['x', '#', '#', '#'],
            ['x', 'x', '#', 'x'],
            ['x', 'x', 'x', 'x']
            ]
    arr[a.row][a.column] = '*'
    as1 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))
    as1 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))
    as1 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))
    as1 = count_quarter(arr, a, 1, 1, len(arr[0]), len(arr))

    for row in arr:
        print(*row) # noqa


if __name__ == '__main__':
    main()

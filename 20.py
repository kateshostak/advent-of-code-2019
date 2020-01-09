from collections import namedtuple


def block2(arr, point, dx, dy):
    y = point.y + dy//abs(dy)

    if dy > 0 and dx > 0:
        while y < len(arr):
            x = point.x + dx//abs(dx)
            while x < len(arr[0]):
                dx2 = x - point.x
                dy2 = y - point.y
                if dx2*dy == dy2*dx:
                    arr[y][x] = 'o'
                x += dx//abs(dx)
            y += dy//abs(dy)
    elif dy < 0 and dx > 0:
        while y > -1:
            x = point.x + dx//abs(dx)
            while x < len(arr[0]):
                dx2 = x - point.x
                dy2 = y - point.y
                if dx2*dy == dy2*dx:
                    arr[y][x] = 'o'
                x += dx//abs(dx)
            y += dy//abs(dy)
    elif dy > 0 and dx < 0:
        while y < len(arr):
            x = point.x + dx//abs(dx)
            while x > -1:
                dx2 = x - point.x
                dy2 = y - point.y
                if dx2*dy == dy2*dx:
                    arr[y][x] = 'o'
                x += dx//abs(dx)
            y += dy//abs(dy)
    else:
        while y > -1:
            x = point.x + dx//abs(dx)
            while x > -1:
                dx2 = x - point.x
                dy2 = y - point.y
                if dx2*dy == dy2*dx:
                    arr[y][x] = 'o'
                x += dx//abs(dx)
            y += dy//abs(dy)


def count_asteroids(arr, point):
    upper_right = count_quarter(arr, point, 1, -1, len(arr[0]), -1)
    upper_left = count_quarter(arr, point, -1, -1, -1, -1)
    lower_left = count_quarter(arr, point, -1, 1, -1, len(arr))
    lower_right = count_quarter(arr, point, 1, 1, len(arr[0]), len(arr))
    cross = count_cross(arr, point)
    return upper_right + upper_left + lower_right + lower_left + cross


def count_cross(arr, point):
    asteroids = 0
    for j in range(point.x + 1, len(arr[0])):
        if arr[point.y][j] == '#':
            asteroids += 1
            for k in range(j + 1, len(arr[0])):
                arr[point.y][k] = '0'

    for j in range(point.x - 1, -1, -1):
        if arr[point.y][j] == '#':
            asteroids += 1
            for k in range(j - 1, -1, -1):
                arr[point.y][k] = '0'

    for i in range(point.y + 1, len(arr)):
        if arr[i][point.x] == '#':
            asteroids += 1
            for k in range(i + 1, len(arr)):
                arr[k][point.x] = '0'

    for i in range(point.y - 1, -1, -1):
        if arr[i][point.x] == '#':
            asteroids += 1
            for k in range(i - 1, -1, -1):
                arr[k][point.x] = '0'

    return asteroids


def count_quarter(arr, point, step_x, step_y, columns, rows):
    asteroids = 0
    y = point.y + step_y
    while y != rows:
        x = point.x + step_x
        while x != columns:
            if arr[y][x] == '#':
                asteroids += 1
                dy = y - point.y
                dx = x - point.x
                block2(arr, point, dx, dy)
            x += step_x
        y += step_y
    return asteroids


def find_best_asteroid(arr):
    point = namedtuple('Point', ['y', 'x'])
    asteroids = {}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '#':
                arr1 = []
                for row in arr:
                    arr1.append(row.copy())
                ast = point(i, j)
                asteroids[ast] = count_asteroids(arr1, ast)
    return asteroids


def main():
    arr = []
    with open('20.txt', 'r') as f:
        for line in f.readlines():
            row = []
            for elem in line.strip():
                row.append(elem)
            arr.append(row)

    astr = find_best_asteroid(arr)
    max_astr = max(astr, key=lambda elem: astr[elem])
    print(max_astr, astr[max_astr])

    # point = namedtuple('Point', ['x', 'y'])
    # a = point(0, 4)
    # arr[4][0] = 'X'
    # print(count_asteroids(arr, a))


if __name__ == '__main__':
    main()

class Wire():
    def __init__(self, arr):
        self.directions = {
                'D': self.go_down,
                'U': self.go_up,
                'L': self.go_left,
                'R': self.go_right
                }
        self.wire = self.make_wire(arr)

    def cross(self, wire):
        cross_points = []
        for point in self.wire:
            if point in wire.wire:
                cross_points.append(point)
        return cross_points

    def make_wire(self, arr):
        wire = [[0,0]]
        position = [0,0]
        for elem in arr:
            direction = elem[0]
            value = int(elem[1:])
            position = self.directions[direction](wire, position, value)
        return wire

    def go_down(self, wire, position, value):
        for i in range (1, value + 1):
            position[1] -= 1
            tmp_pos = [position[0], position[1]]
            wire.append(tmp_pos)
        return position

    def go_up(self, wire, position, value):
        for i in range (1, value + 1):
            position[1] += 1
            tmp_pos = [position[0], position[1]]
            wire.append(tmp_pos)
        return position

    def go_left(self, wire, position, value):
        for i in range (1, value + 1):
            position[0] -= 1
            tmp_pos = [position[0], position[1]]
            wire.append(tmp_pos)
        return position

    def go_right(self, wire, position, value):
        for i in range (1, value + 1):
            position[0] += 1
            tmp_pos = [position[0], position[1]]
            wire.append(tmp_pos)
        return position

    def __getitem__(self, position):
        return self.wire[position]

    def __len__(self):
        return len(self.wire)

def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[0])

def main():
    paths = []
    with open('5.txt') as f:
        for i in range(2):
            path = []
            tmp = f.readline().strip().split(',')
            for elem in tmp:
                path.append(elem)
            paths.append(path)

    wire1 = Wire(paths[0])
    wire2 = Wire(paths[1])
    cross_points = wire1.cross(wire2)
    centr_port = [0, 0]
    manh_dist = []
    for point in cross_points:
        manh_dist.append(manhattan_distance(centr_port, point))
    print(min(manh_dist))

if __name__ == '__main__':
    main()

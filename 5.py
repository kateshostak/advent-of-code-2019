import pdb


class Wire():
    def __init__(self, arr):
        self.directions = {
                'D': self.go_down,
                'U': self.go_up,
                'L': self.go_left,
                'R': self.go_right
                }
        self.wire = self.make_wire(arr)

    def count_steps(self, point):
        position = [0, 0]
        steps = 0
        for i in range(len(self.wire) - 1):
            line = [self.wire[i], self.wire[i + 1]]
            if self.point_in_line(line, point):
                #pdb.set_trace()
                tmp_steps = manhattan_distance(position, point)
                steps += tmp_steps
                return steps
            old_position, position = position, self.wire[i+1]
            steps += manhattan_distance(old_position, position)
        return None

    def point_in_line(self, line, point):
        x_start = min(line[0][0], line[1][0])
        x_end = max(line[0][0], line[1][0])
        y_start = min(line[0][1], line[1][1])
        y_end = max(line[0][1], line[1][1])
        if point[0] >= x_start and point[0] <= x_end:
            if point[1] >= y_start and point[1] <= y_end:
                return True
        return False

    def cross(self, wire):
        cross_points = []
        for i in range(len(self.wire) - 1):
            line1 = [self.wire[i], self.wire[i+1]]
            for j in range(len(wire) - 1):
                line2 = [wire[j], wire[j+1]]
                line_position = self.check_line_position(line1, line2)
                if line_position == 1:
                    self.cross_lines(line1, line2, cross_points)
                elif line_position == 2:
                    self.cross_lines(line2, line1, cross_points)
        return cross_points

    def check_line_position(self, line1, line2):
        if line1[0][1] == line1[1][1] and line2[0][0] == line2[1][0]:
            return 1
        elif line2[0][1] == line2[1][1] and line1[0][0] == line1[1][0]:
            return 2
        else:
            return 0

    def cross_lines(self, line1, line2, cross_points):
        line1_start_x = min(line1[0][0], line1[1][0])
        line1_end_x = max(line1[0][0], line1[1][0])
        line1_y = line1[0][1]

        line2_x = line2[0][0]
        line2_start_y = min(line2[0][1], line2[1][1])
        line2_end_y = max(line2[0][1], line2[1][1])

        if line2_x in range(line1_start_x, line1_end_x + 1) and line1_y in range(line2_start_y, line2_end_y):
            point = [line2_x, line1_y]
            cross_points.append(point)

    def make_wire(self, arr):
        wire = [[0, 0]]
        position = [0, 0]
        for elem in arr:
            direction = elem[0]
            value = int(elem[1:])
            position = self.directions[direction](wire, position, value)
        return wire

    def go_down(self, wire, position, value):
        position[1] -= value
        tmp_pos = [position[0], position[1]]
        wire.append(tmp_pos)
        return position

    def go_up(self, wire, position, value):
        position[1] += value
        tmp_pos = [position[0], position[1]]
        wire.append(tmp_pos)
        return position

    def go_left(self, wire, position, value):
        position[0] -= value
        tmp_pos = [position[0], position[1]]
        wire.append(tmp_pos)
        return position

    def go_right(self, wire, position, value):
        position[0] += value
        tmp_pos = [position[0], position[1]]
        wire.append(tmp_pos)
        return position

    def __getitem__(self, position):
        return self.wire[position]

    def __len__(self):
        return len(self.wire)


def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

def minimize_signal(steps1, steps2):
    step_sum = []
    for elem in zip(steps1, steps2):
        tmp_sum = elem[0] + elem[1]
        step_sum.append(tmp_sum)
    return min(step_sum)


def count_steps(wire, points):
    steps = []
    for point in points:
        res = wire.count_steps(point)
        steps.append(res)
    return steps


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
    wires = [wire1, wire2]

    cross_points = wire1.cross(wire2)
    centr_port = [0, 0]
    manh_dist = []
    for point in cross_points:
        manh_dist.append(manhattan_distance(centr_port, point))
    print(min(manh_dist))

    steps = []
    for i in range(2):
        tmp_steps = count_steps(wires[i], cross_points)
        steps.append(tmp_steps)

    print(steps[0])
    print(steps[1])
    res = minimize_signal(steps[0], steps[1])
    print(res)


if __name__ == '__main__':
    main()

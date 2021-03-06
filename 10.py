import pdb


class Memmory():
    OPCODE_TO_STEP = {
            99: 1,
            1: 4,
            2: 4,
            3: 2,
            4: 2,
            5: 0,
            6: 0,
            7: 4,
            8: 4
            }

    OPCODE_TO_FUNC = {
            99: 'halt_',
            1: 'add_',
            2: 'mult_',
            3: 'store_input',
            4: 'print_output',
            5: 'jump_if_true',
            6: 'jump_if_false',
            7: 'less_than',
            8: 'equals'
            }

    def compute(self, arr):
        self.position = 0
        self.prog = arr.copy()
        to_exit = False
        while not to_exit:
            params = self.prog[self.position]
            modes = params//100
            opcode = params%100
            to_exit = self.execute(opcode, modes)
            self.position += self.step(opcode)
        return self.prog

    def execute(self, opcode, modes):
        func = Memmory.OPCODE_TO_FUNC[opcode]
        return self.__getattribute__(func)(modes)

    def step(self, opcode):
        return Memmory.OPCODE_TO_STEP[opcode]

    def get_value(self, i, mode):
        if mode == 0:
            ind = self.prog[i]
            return self.prog[ind]
        else:
            return self.prog[i]

    def halt_(self, modes):
        return True

    def add_(self, modes):
        i = self.get_value(self.position + 1, modes%10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        self.prog[k] = i + j
        return False

    def mult_(self, modes):
        i = self.get_value(self.position + 1, modes%10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        self.prog[k] = i*j
        return False

    def store_input(self, modes):
        inpt = input('Type input here: ')
        ind = self.prog[self.position + 1]
        self.prog[ind] = int(inpt)
        return False

    def print_output(self, modes):
        ind = self.prog[self.position + 1]
        print(self.prog[ind])
        return False

    def jump_if_true(self, modes):
        i = self.get_value(self.position + 1, modes%10)
        j = self.get_value(self.position + 2, modes//10)
        if i:
            self.position = j
        else:
            self.position += 3
        return False

    def jump_if_false(self, modes):
        i = self.get_value(self.position + 1, modes%10)
        j = self.get_value(self.position + 2, modes//10)
        if not i:
            self.position = j
        else:
            self.position += 3
        return False

    def less_than(self, modes):
        i = self.get_value(self.position + 1, modes%10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        if i < j:
            self.prog[k] = 1
        else:
            self.prog[k] = 0

    def equals(self, modes):
        i = self.get_value(self.position + 1, modes%10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        if i == j:
            self.prog[k] = 1
        else:
            self.prog[k] = 0


def find_res(n, arr, comp):
    for i in range(100):
        for j in range(100):
            arr[1] = i
            arr[2] = j
            res = comp.compute(arr)[0]
            if res == n:
                return i, j
    return -1, -1

def main():
    arr = []
    with open('9.txt') as f:
        prog = f.read().strip().split(',')
        for elem in prog:
            arr.append(int(elem))
    #arr = [3,0,4,0,99]
    #arr = [1002,4,3,4,33]
    #arr = [1101,100,-1,4,0]
    mycomp = Memmory()
    #pdb.set_trace()
    #answer 11193703
    mycomp.compute(arr)


if __name__ == '__main__':
    main()

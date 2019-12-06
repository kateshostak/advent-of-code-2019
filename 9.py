import pdb


class Memmory():
    OPCODE_TO_STEP = {
            99: 1,
            1: 4,
            2: 4,
            3: 2,
            4: 2
            }

    OPCODE_TO_FUNC = {
            99: 'halt_',
            1: 'add_',
            2: 'mult_',
            3: 'store_input',
            4: 'print_output'
            }

    def compute(self, arr):
        self.position = 0
        self.prog = arr.copy()
        to_exit = False
        while not to_exit:
            opcode = self.prog[self.position]
            to_exit = self.execute(opcode)
            self.step(opcode)
        return self.prog

    def execute(self, opcode):
        func = Memmory.OPCODE_TO_FUNC[opcode]
        return self.__getattribute__(func)()

    def step(self, opcode):
        self.position += Memmory.OPCODE_TO_STEP[opcode]

    def halt_(self):
        return True

    def add_(self):
        ind_1 = self.prog[self.position + 1]
        ind_2 = self.prog[self.position + 2]
        ind_3 = self.prog[self.position + 3]
        self.prog[ind_3] = self.prog[ind_1] + self.prog[ind_2]
        return False

    def mult_(self):
        ind_1 = self.prog[self.position + 1]
        ind_2 = self.prog[self.position + 2]
        ind_3 = self.prog[self.position + 3]
        self.prog[ind_3] = self.prog[ind_1]*self.prog[ind_2]
        return False
    def store_input(self):
        inpt = input('Type input here: ')
        self.prog[self.position + 1] = int(inpt)
        return False

    def print_output(self):
        print(self.prog[self.position + 1])
        return False

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
    with open('3.txt') as f:
        prog = f.read().split(',')
        for elem in prog:
            arr.append(int(elem))
    mycomp = Memmory()
    i, j  = find_res(19690720, arr, mycomp)
    print(100*i + j)

if __name__ == '__main__':
    main()

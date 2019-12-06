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
            params = self.prog[self.position]
            modes = params//100
            opcode = params%100
            to_exit = self.execute(opcode, modes)
            self.step(opcode)
        return self.prog

    def execute(self, opcode, modes):
        func = Memmory.OPCODE_TO_FUNC[opcode]
        return self.__getattribute__(func)(modes)

    def step(self, opcode):
        self.position += Memmory.OPCODE_TO_STEP[opcode]

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
        prog = f.read().split(',')
        for elem in prog:
            arr.append(int(elem))
    mycomp = Memmory()
    #pdb.set_trace()
    mycomp.compute(arr)

if __name__ == '__main__':
    main()

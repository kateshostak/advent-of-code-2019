class MyComputer():
    def __init__(self):
        self.opcodes = {
                99: self.halt_,
                1: self.add_,
                2: self.mult_
                }

    def compute(self, arr):
        position = 0
        to_exit = False
        while not to_exit:
            opcode = arr[position]
            to_exit = self.opcodes[opcode](arr, position)
            position += 4
        return arr

    def halt_(self, arr, position):
        return True

    def add_(self, arr, position):
        ind_1 = arr[position + 1]
        ind_2 = arr[position + 2]
        ind_3 = arr[position + 3]
        arr[ind_3] = arr[ind_1] + arr[ind_2]
        return False

    def mult_(self, arr, position):
        ind_1 = arr[position + 1]
        ind_2 = arr[position + 2]
        ind_3 = arr[position + 3]
        arr[ind_3] = arr[ind_1]*arr[ind_2]
        return False

def main():
    arr = []
    with open('3.txt') as f:
        prog = f.read().split(',')
        for elem in prog:
            arr.append(int(elem))
    arr[1] = 12
    arr[2] = 2
    mycomp = MyComputer()
    print(mycomp.compute(arr)[0])

if __name__ == '__main__':
    main()

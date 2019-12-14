def store_input(INPUTS):
    return INPUTS.pop(0)


def print_output(i, OUTPUTS):
    OUTPUTS.append(i)


class Memmory():
    OPCODE_TO_FUNC = {
            99: 'halt_',
            1: 'add_',
            2: 'mult_', 3: 'store_input',
            4: 'print_output',
            5: 'jump_if_true',
            6: 'jump_if_false',
            7: 'less_than',
            8: 'equals',
            9: 'change_base'
            }

    def __init__(self, prog, inpt, outpt, inputs, outputs):
        self.position = 0
        self.base = 0
        self.prog = prog
        self.print_ = outpt
        self.input_ = inpt
        self.inputs = inputs
        self.outputs = outputs

    def compute(self):
        to_exit = False
        while not to_exit:
            params = self.prog.get_value(self.position)
            modes = params//100
            opcode = params % 100
            to_exit = self.execute(opcode, modes)

    def execute(self, opcode, modes):
        func = Memmory.OPCODE_TO_FUNC[opcode]
        return getattr(self, func)(modes)


    def get_value(self, i, mode):
        if mode == 0:
            ind = self.prog.get_value(i)
            #return self.prog.get_value(ind)
            return ind
        elif mode == 1:
            #return self.prog.get_value(i)
            return i
        elif mode == 2:
            ind = self.prog.get_value(i) + self.base
            #return self.prog.get_value(ind)
            return ind

    def halt_(self, modes):
        return True

    def add_(self, modes):
        i = self.get_value(self.position + 1, self.get_mode(modes, 0))
        j = self.get_value(self.position + 2, self.get_mode(modes, 1))
        #k = self.prog.get_value(self.position + 3)
        k = self.get_value(self.position + 3, self.get_mode(modes, 2))
        a = self.prog.get_value(i)
        b = self.prog.get_value(j)
        self.prog.set_value(k, a+b)
        self.position += 4
        return False

    def get_mode(self, modes, i):
        while i:
            modes //= 10
            i -= 1
        return modes%10

    def mult_(self, modes):
        i = self.get_value(self.position + 1, self.get_mode(modes, 0))
        j = self.get_value(self.position + 2,self.get_mode(modes, 1))
        #k = self.prog.get_value(self.position + 3)
        k = self.get_value(self.position + 3, self.get_mode(modes, 2))
        a = self.prog.get_value(i)
        b = self.prog.get_value(j)
        self.prog.set_value(k, a*b)
        self.position += 4
        return False

    def store_input(self, modes):
        inpt = self.input_()
        ind = self.get_value(self.position + 1, self.get_mode(modes, 0))
        self.prog.set_value(ind, int(inpt))
        self.position += 2
        return False

    def print_output(self, modes):
        i = self.get_value(self.position + 1,self.get_mode(modes, 0) )
        a = self.prog.get_value(i)
        self.print_(a)
        self.position += 2
        return False

    def jump_if_true(self, modes):
        i = self.get_value(self.position + 1, self.get_mode(modes, 0))
        j = self.get_value(self.position + 2,self.get_mode(modes, 1))
        a = self.prog.get_value(i)
        b = self.prog.get_value(j)
        if a:
            self.position = b
        else:
            self.position += 3
        return False

    def jump_if_false(self, modes):
        i = self.get_value(self.position + 1, self.get_mode(modes, 0))
        j = self.get_value(self.position + 2, self.get_mode(modes, 1))
        a = self.prog.get_value(i)
        b = self.prog.get_value(j)
        if not a:
            self.position = b
        else:
            self.position += 3
        return False

    def less_than(self, modes):
        i = self.get_value(self.position + 1, self.get_mode(modes, 0))
        j = self.get_value(self.position + 2, self.get_mode(modes, 1))
        #k = self.prog.get_value(self.position + 3)
        a = self.prog.get_value(i)
        b = self.prog.get_value(j)
        k = self.get_value(self.position + 3, self.get_mode(modes, 2))
        self.position += 4
        if a < b:
            self.prog.set_value(k, 1)
        else:
            self.prog.set_value(k, 0)
        return False

    def equals(self, modes):
        i = self.get_value(self.position + 1, self.get_mode(modes, 0))
        j = self.get_value(self.position + 2, self.get_mode(modes, 1))
        #k = self.prog.get_value(self.position + 3)
        a = self.prog.get_value(i)
        b = self.prog.get_value(j)
        k = self.get_value(self.position + 3, self.get_mode(modes, 2))
        self.position += 4
        if a == b:
            self.prog.set_value(k, 1)
        else:
            self.prog.set_value(k, 0)
        return False

    def change_base(self, modes):
        i = self.get_value(self.position + 1, self.get_mode(modes, 0))
        a = self.prog.get_value(i)
        self.base += a
        self.position += 2
        return False


def get_input_prog():
    with open('17.txt') as f:
        prog = f.read().strip().split(',')
        arr = [int(elem) for elem in prog]
    return arr

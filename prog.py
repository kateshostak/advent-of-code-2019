class Prog():
    def __init__(self, arr):
        self.prog = self.build_dict(arr)

    def build_dict(self, arr):
        prog = dict()
        for i, elem in enumerate(arr):
            prog[i] = elem
        return prog

    def set_value(self, key, value):
        self.prog[key] = value

    def get_value(self, key):
        if key in self.prog:
            return self.prog[key]
        else:
            return 0

    def get_prog_arr(self):
        arr = []
        for key, value in self.prog.items:
            arr.append(value)
        return arr

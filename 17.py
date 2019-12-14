import pdb
import Comp
import prog

INPUTS = []
OUTPUTS = []


def store_input():
    return INPUTS.pop(0)


def print_output(i, OUTPUTS):
    OUTPUTS.append(i)


def get_input_prog():
    with open('17.txt') as f:
        prog = f.read().strip().split(',')
        arr = [int(elem) for elem in prog]
    return arr


def main():
    #arr = [104,1125899906842624,99]
   # arr = [1102,34915192,34915192,7,4,7,99,0]
   # arr = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    arr = get_input_prog()
    inpt = input
    outpt = print
    myprog = prog.Prog(arr)
    mycomp = Comp.Memmory(myprog, inpt, outpt, INPUTS, OUTPUTS)
    #pdb.set_trace()
    mycomp.compute()


if __name__ == '__main__':
    main()

class Atom:
    def __init__(self, name, chain, pos, seq_num):
        self.name = name
        self.chain = chain
        self.pos = pos
        self.seq_num = seq_num


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        


def amino_acid(input):
    for line in open(input):
        list = line.split()
        if (list[0]=='ATOM' and list[2]=='CA'):
            pos_list = Position(list[6], list[7], list[8])
            atom_list = Atom(list[3], list[4], pos_list, list[5])
            lst.append(atom_list)
    return lst

def print_list(lst):
    count = 0
    for i in lst:
        print("atom list: ", i.name, i.chain, i.pos.x, i.pos.y, i.pos.z, i.seq_num)
        count+=1
    return count

def euclidean_dis(arg1, arg2):
    return ((float(arg1.pos.x)-float(arg2.pos.x))**2 + (float(arg1.pos.y)-float(arg2.pos.y))**2 + (float(arg1.pos.z)-float(arg2.pos.z))**2)**0.5


def s_condition(arg1, arg2):
    return (abs(int(arg1.seq_num)) - abs(int(arg2.seq_num)))


def printF(list1, list2):
    print("Chain: " + list1.chain + " --> " + list1.name+"("+list1.seq_num+")"+" - "+list2.name+"("+list2.seq_num+")"+" : "+ str(euclidean_dis(list1,list2)) +" Angstroms")


def printFormat(inp_name, d, s):
    print("Output for "+str(inp_name)+" with D="+str(d)+" and S="+str(s)+":")

################################################################################################
lst = []
x = input()
t = x.split()
inp = t[0]
d = float(t[1])
s = float(t[2])
pair = amino_acid(inp)


printed_atom_list = []
printFormat(inp, d, s)
for i in lst:
    for j in lst:
        if(i != j and i.chain == j.chain):
            euc_dis = euclidean_dis(i, j)
            s_dis = s_condition(i, j)
            if(euc_dis <= d and s_dis >= s):
                printF(i, j)
def amino_acid_pair1(input):
    pair_1 = []
    for line in open(input):
        list = line.split()
        if (list[0]=='ATOM' and list[4]=='A'):
            list[6]=float (list[6])
            list[7]=float (list[7])
            list[8]=float (list[8])
            if (list[2]=='CB' or (list[2]=='CA')):
                pair_1.append(list)
    return pair_1


def amino_acid_pair2(input):
    pair_2 = []
    for line in open(input):
        list = line.split()
        if (list[0]=='ATOM' and list[4]=='B'):
            list[6]=float (list[6])
            list[7]=float (list[7])
            list[8]=float (list[8])
            if (list[2]=='CB' or (list[2]=='CA')):
                pair_2.append(list)
    return pair_2


def euclidean_dis(arg1, arg2):
    return ((arg1[6]-arg2[6])**2 + (arg1[7]-arg2[7])**2 + (arg1[8]-arg2[8])**2)**0.5


def s_condition(arg1, arg2):
    return (abs(int(arg1[5])) - abs(int(arg2[5])))


def printF(list1, list2):
    print "Chain: " + list1[4] + " --> " + list1[3]+"("+list1[5]+")"+" - "+list2[3]+"("+list2[5]+")"+" : "+ str(euclidean_dis(list1,list2)) +" Angstroms"

################################################################################################

inp = '3r0a.pdb'
pair1 = amino_acid_pair1(inp)
pair2 = amino_acid_pair2(inp)
rec = 0


for i in range(0, len(pair1)):
    for j in range(0, len(pair2)):
        if (euclidean_dis(pair1[i], pair2[j]) <= 5.0 and pair1[i][1] != pair2[j][1]):
            if(s_condition(pair1[i], pair2[j]) >= 40):
                rec+=1

print("There are "+str(rec)+" interacting pairs.")
for i in range(0, len(pair1)):
    for j in range(0, len(pair2)):
        if (euclidean_dis(pair1[i], pair2[j]) <= 5.0 and pair1[i][1] != pair2[j][1]):
            if(s_condition(pair1[i], pair2[j]) >= 40):
                printF(pair1[i], pair2[j])

import argparse
import csv


class Node:
    def __init__(self, chara=None, number=None, child_1=None, child_2=None, child_3=None):
        self.chara = chara
        self.number = number
        self.child_1 = child_1
        self.child_2 = child_2
        self.child_3 = child_3

    def is_leaf(self):
        return self.child_1 == self.child_2 == self.child_3 == None


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', default=None,
                        action='store_true', help='Decoding.')
    parser.add_argument('input', help='The input file.')
    parser.add_argument('output', help='The output file.')
    parser.add_argument('huffman', help='The huffman file.')
    args = parser.parse_args()
    return args.d, args.input, args.output, args.huffman


def makeList(tree):
    paths = []
    if not (tree.child_1 or tree.child_2 or tree.child_3):
        return [[tree.chara]]
    if tree.child_1:
        paths.extend([["0"] + child for child in makeList(tree.child_1)])
    if tree.child_2:
        paths.extend([["1"] + child for child in makeList(tree.child_2)])
    if tree.child_3:
        paths.extend([["2"] + child for child in makeList(tree.child_3)])
    return paths


decoding, inputfile, outputfile, huffman = parse_args()
if decoding == None:
    info = ""
    with open(inputfile, 'r') as myfile:
        info = myfile.read()
    char = []
    freq = []
    for i in info:
        if i in char:
            index = char.index(i)
            freq[index] = freq[index] + 1
        else:
            char.append(i)
            freq.append(1)
    if (len(char) % 2 == 0):
        char.append("")
        freq.append(0)
    freq, char = zip(*sorted(zip(freq, char)))
    char2 = []
    freq2 = []
    for i in char:
        char2.append(i)
    for i in freq:
        freq2.append(i)
    nodes = []
    for i in range(len(char)):
        node = Node(chara=char2[i], number=freq2[i])
        nodes.append(node)
    nodes2 = []
    for i in nodes:
        nodes2.append(i)
    while(len(nodes2) > 0):
        if(len(nodes2) >= 3):
            summ = nodes2[0].number + nodes2[1].number + nodes2[2].number
            new_node = Node(
                number=summ, child_1=nodes2[0], child_2=nodes2[1], child_3=nodes2[2])
            nodes2.pop(0)
            nodes2.pop(0)
            nodes2.pop(0)
            nodes.append(new_node)

            nodes2.append(new_node)
            nodes2 = sorted(nodes2, key=lambda x: (x.number, x.chara))
        if(len(nodes2) == 1):
            break
    nodes = sorted(nodes, key=lambda x: (x.number, x.chara), reverse=True)
    root = nodes[0]
    list1 = []

    list1 = makeList(root)
    list2 = []
    list3 = []
    for i in list1:
        list2.append(i[len(i) - 1])
        toadd = ""
        print i
        for j in range(len(i) - 1):
            toadd = toadd + str(i[j])
        list3.append(toadd)

    with open(huffman, 'wb') as csvfile:
        fieldnames = ['character', 'tri']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for i in range(len(list1)):
            writer.writerow({'character': list2[i], 'tri': list3[i]})

    trihuffman = ""
    for i in info:
        for j in range(len(list2)):
            if(i == list2[j]):
                trihuffman = trihuffman + list3[j]
    currentdna = "A"
    result = ""
    for t in trihuffman:
        if (currentdna == "A"):
            if(t == "0"):
                currentdna = "C"
                result = result + "C"
            elif(t == "1"):
                currentdna = "G"
                result = result + "G"
            elif(t == "2"):
                currentdna = "T"
                result = result + "T"
        elif (currentdna == "C"):
            if(t == "0"):
                currentdna = "G"
                result = result + "G"
            elif(t == "1"):
                currentdna = "T"
                result = result + "T"
            elif(t == "2"):
                currentdna = "A"
                result = result + "A"
        elif (currentdna == "G"):
            if(t == "0"):
                currentdna = "T"
                result = result + "T"
            elif(t == "1"):
                currentdna = "A"
                result = result + "A"
            elif(t == "2"):
                currentdna = "C"
                result = result + "C"
        elif (currentdna == "T"):
            if(t == "0"):
                currentdna = "A"
                result = result + "A"
            elif(t == "1"):
                currentdna = "C"
                result = result + "C"
            elif(t == "2"):
                currentdna = "G"
                result = result + "G"
    f = open(outputfile, 'w')
    f.write(result)
else:
    info = ""
    with open(inputfile, 'r') as myfile:
        info = myfile.read()
    currentdna = "A"
    result = ""
    for t in info:
        if (currentdna == "A"):
            if(t == "C"):
                currentdna = "C"
                result = result + "0"
            elif(t == "G"):
                currentdna = "G"
                result = result + "1"
            elif(t == "T"):
                currentdna = "T"
                result = result + "2"
        elif (currentdna == "C"):
            if(t == "G"):
                currentdna = "G"
                result = result + "0"
            elif(t == "T"):
                currentdna = "T"
                result = result + "1"
            elif(t == "A"):
                currentdna = "A"
                result = result + "2"
        elif (currentdna == "G"):
            if(t == "T"):
                currentdna = "T"
                result = result + "0"
            elif(t == "A"):
                currentdna = "A"
                result = result + "1"
            elif(t == "C"):
                currentdna = "C"
                result = result + "2"
        elif (currentdna == "T"):
            if(t == "A"):
                currentdna = "A"
                result = result + "0"
            elif(t == "C"):
                currentdna = "C"
                result = result + "1"
            elif(t == "G"):
                currentdna = "G"
                result = result + "2"
    huffmandict = {}
    with open(huffman, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            huffmandict[row[0]] = row[1]
    check = ""
    finalresult = ""
    for i in result:
        check = check + i
        try:
            finalresult = finalresult + \
                list(huffmandict.keys())[
                    list(huffmandict.values()).index(check)]
            check = ""
        except ValueError:
            aaaa = 1
    f = open(outputfile, 'w')
    f.write(finalresult)

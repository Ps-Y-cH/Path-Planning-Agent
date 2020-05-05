"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

from tkinter import *
import time
import sys
sys.path.append('./BFS')
sys.path.append('./IDS')


from BFS.BfsDriver import *
from IdsDriver import *
from BfsNode import *
from DirtGenerator import *
from IdsNode import *
from State import *


def completeAnalysis(dirtlist, BFSanslist, IDSanslist, bfsTime, idsTime, vc_x, vc_y):
    root = Tk()
    root.geometry("2000x1000")

    left = Frame(root, borderwidth=1, relief="solid", bg='yellow', width=20)
    right = Frame(root, borderwidth=1, relief="solid")
    box1 = Frame(right, borderwidth=2, relief="solid", width=600, height=350, padx=10, pady=10)
    box2 = Frame(right, borderwidth=2, relief="solid", width=600, height=350, padx=10, pady=10)
    lablebfs = Label(box1, text='G1 -- BFS')
    lableids = Label(box2, text='G2 -- IDS')
    left.pack(side="left")#, fill="both")
    right.pack(side="right", expand=True, fill="both")
    box1.place(x=0, y=0)
    box2.place(x=0, y=405)
    lablebfs.grid(rowspan=10, column=10)
    lableids.grid(rowspan=10, column=10)

    lbfs = []
    for x in range(0, 100):
        lbfs.append(Label(box1, width=4, height=2, borderwidth=2, relief='solid'))

    temp = 0
    for p in range(0, 10):
        for q in range(0, 10):
            lbfs[temp].grid(row=p, column=q)
            temp += 1

    for x in dirtlist:
        lbfs[x - 1].config(bg='yellow')

    lids = []
    for x in range(0, 100):
        lids.append(Label(box2, width=4, height=2, borderwidth=2, relief='solid'))

    temp = 0
    for p in range(0, 10):
        for q in range(0, 10):
            lids[temp].grid(row=p, column=q)
            temp += 1

    for x in dirtlist:
        lids[x - 1].config(bg='yellow')

    #Size of one node
    obj1 = BfsNode(State([1, 1], [[1, 1], [2, 2]]), None, 'N', 0)
    bfsSize = obj1.__sizeof__()
    obj2 = IdsNode(State([1, 1], [[1, 1], [2, 2]]), None, 'N', 0, 0)
    idsSize = obj2.__sizeof__()

    #Memory allocated
    bfsMem = (BFSanslist[2] + BFSanslist[3]) * bfsSize
    idsMem = (IDSanslist[2] + IDSanslist[3]) * idsSize
    diff = bfsMem - idsMem

    #R12 analysis
    # bfscost =[]
    # bfsav = 0
    # for x in range(10):
    #     initialDirtTuple = list_to_xy_coord(dirt_gen(2))
    #     print('------------------------BFS running 10 times---------------------------')
    #     print('Initial Dirt List --', initialDirtTuple)
    #     finalDirtTuple = []
    #     initalState = State([vc_x, vc_y], initialDirtTuple)
    #     finalState = State([9, 9], finalDirtTuple)
    #     bfsanswers =bfs(initalState, finalState)
    #     print('Action Sequence --', bfsanswers[0], '\nPath Cost --', bfsanswers[1])
    #     bfscost.append(bfsanswers[1])
    # for p in bfscost:
    #     bfsav = bfsav + p
    # bfsav = bfsav/10

    # idscost = []
    # idsav = 0
    # for x in range(10):
    #     initialDirtTuple = list_to_xy_coord(dirt_gen(2))
    #     print('------------------------IDS running 10 times---------------------------')
    #     print('Initial Dirt List --', initialDirtTuple)
    #     finalDirtTuple = []
    #     initalState = State([vc_x, vc_y], initialDirtTuple)
    #     finalState = State([9, 9], finalDirtTuple)
    #     idsanswers = ids(initalState, finalState)
    #     print('Action Sequence --', idsanswers[0], '\nPath Cost --', idsanswers[1])
    #     idscost.append(idsanswers[1])
    # for p in bfscost:
    #     idsav = idsav + p
    # idsav = idsav / 10



    r1 = Label(left, text='R1(Number of nodes generated in BFS):  ' + str(BFSanslist[2]), bd=1, width=82, anchor='w', pady=4, height=2)
    r2 = Label(left, text='R2(Memory allocated to One BFS Node in Bytes):  '+str(bfsSize), bd=1, width=82, anchor='w', pady=4, height=3)  # rem
    r3 = Label(left, text='R3(Size of queue generated in BFS):  ' + str(BFSanslist[3]), bd=1, width=82, anchor='w', pady=4,
               height=2)
    g1 = Label(left, text='G1(Action Sequence from BFS):  ' + str(BFSanslist[0]), bd=1, width=82, anchor='w', pady=4, height=4,
               wraplength=550, justify=LEFT)
    r4 = Label(left, text='R4(Path cost of BFS):  ' + str(BFSanslist[1]), bd=1, width=82, anchor='w', pady=4, height=2)
    r5 = Label(left, text='R5(Time for BFS in seconds):  ' + str(bfsTime), bd=1, width=82, anchor='w', pady=4, height=2)
    r6 = Label(left, text='R6(Number of nodes generated in IDS):  ' + str(IDSanslist[2]), bd=1, width=82, anchor='w', pady=4, height=2)
    r7 = Label(left, text='R7(Memory allocated to One IDS Node in Bytes):  '+str(idsSize), bd=1, width=82, anchor='w', pady=4, height=3)  # rem
    r8 = Label(left, text='R8(Size of queue generated in IDS):  ' + str(IDSanslist[3]), bd=1, width=82, anchor='w', pady=4,
               height=2)
    g2 = Label(left, text='G2(Action Sequence from IDS):  ' + str(IDSanslist[0]), bd=1, width=82, anchor='w', pady=4, height=4,
               wraplength=550, justify=LEFT)
    r9 = Label(left, text='R9(Path cost of IDS): ' + str(IDSanslist[1]), bd=1, width=82, anchor='w', pady=4, height=2)
    r10 = Label(left, text='R10(Time for BFS in seconds): ' + str(idsTime), bd=1, width=82, anchor='w', pady=4,
                height=2)
    r11 = Label(left, text='R11--- Memory for BFS: ' + str(bfsMem) + ' Bytes   Memory for IDS: ' + str(
        idsMem) + ' Bytes   Difference: ' + str(diff) + ' Bytes', bd=1, width=82, anchor='w', pady=4, height=2)
    # r12 = Label(left, text='R12(BFS and IDS running 10 times with p = 2)--- Average BFScost: '+str(bfsav)+' Average IDS cost: '+str(idsav), bd=1, width=82, anchor='w', pady=4, height=2)

    r1.pack()
    r2.pack()
    r3.pack()
    g1.pack()
    r4.pack()
    r5.pack()
    r6.pack()
    r7.pack()
    r8.pack()
    g2.pack()
    r9.pack()
    r10.pack()
    r11.pack()
    # r12.pack()

    global initialpos
    if vc_x == 0 and vc_y == 0:
        initialpos = 1
    if vc_x == 0 and vc_y == 9:
        initialpos = 10
    if vc_x == 9 and vc_y == 0:
        initialpos = 91
    if vc_x == 9 and vc_y == 9:
        initialpos = 100

    ####### BFS - ACTION #########
    bfsactionseq = BFSanslist[0]
    time.sleep(1)
    root.update()
    lbfs[initialpos - 1].config(bg='blue')
    time.sleep(4)
    root.update()
    lbfs[initialpos - 1].config(bg='red')
    pos1 = initialpos
    for x in bfsactionseq:
        if x == 'MU':
            pos1 = pos1 - 10
        if x == 'MD':
            pos1 = pos1 + 10
        if x == 'ML':
            pos1 = pos1 - 1
        if x == 'MR':
            pos1 = pos1 + 1
        lbfs[pos1 - 1].config(bg='blue')
        time.sleep(1)
        root.update()
        lbfs[pos1 - 1].config(bg='red')
    lbfs[pos1 - 1].config(bg='blue')

    time.sleep(2)

    ####### IDS - ACTION #########
    idsactionseq = IDSanslist[0]
    time.sleep(1)
    root.update()
    lids[initialpos - 1].config(bg='blue')
    time.sleep(1)
    root.update()
    lids[initialpos - 1].config(bg='red')
    pos2 = initialpos
    for x in idsactionseq:
        if x == 'MU':
            pos2 = pos2 - 10
        if x == 'MD':
            pos2 = pos2 + 10
        if x == 'ML':
            pos2 = pos2 - 1
        if x == 'MR':
            pos2 = pos2 + 1
        lids[pos2 - 1].config(bg='blue')
        time.sleep(1)
        root.update()
        lids[pos2 - 1].config(bg='red')
    lids[pos2 - 1].config(bg='blue')

    root.mainloop()

# completeAnalysis([1, 5, 8, 99], [['MR','MD','MR'],12,12,12], [['MR','MD','MR','MD','MD'],122,122,122],12,121,0,0)

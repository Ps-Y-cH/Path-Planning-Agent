"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import time
import sys
sys.path.append('./BFS')
sys.path.append('./IDS')


from tkinter import *
from AllAnalysisGUIWindow import completeAnalysis
from BfsDriver import *
from DirtGenerator import *
from IdsDriver import *
from State import *

def roomEnvGUI():
    x = int(e1.get())

    global vc_x, vc_y
    temp = e2.get()

    if temp == 'ul':
        vc_x = 0
        vc_y = 0
    elif temp == 'ur':
        vc_x = 0
        vc_y = 9
    elif temp == 'bl':
        vc_x = 9
        vc_y = 0
    elif temp == 'br':
        vc_x = 9
        vc_y = 9
    else:
        return None

    global dirtlist
    dirtlist = dirt_gen(x)
    # print(dirtlist)
    lable = []
    windowRoomEnvGUI = Tk()
    windowRoomEnvGUI.title('Initial Room Environment')

    for x in range(0, 100):
        lable.append(Label(windowRoomEnvGUI, width=4, height=2, borderwidth=2, relief='solid'))

    temp = 0
    for p in range(0, 10):
        for q in range(0, 10):
            lable[temp].grid(row=p, column=q)
            temp += 1

    for x in dirtlist:
        lable[x - 1].config(bg='yellow')

    windowRoomEnvGUI.mainloop()


def bfsCall():
    if dirtlist is None:
        return
    time_start = time.process_time()
    initialDirtTuple = list_to_xy_coord(dirtlist)
    print('------------------------BFS---------------------------')
    print('Initial Dirt List --', initialDirtTuple)
    finalDirtTuple = []
    initalState = State([vc_x, vc_y], initialDirtTuple)
    finalState = State([9, 9], finalDirtTuple)
    global BFSanslist
    BFSanslist = bfs(initalState, finalState)
    print('Action Sequence --', BFSanslist[0], '\nPath Cost --', BFSanslist[1], '\nTotal no of nodes created --',
          BFSanslist[2], '\nMax size of auxiliary queue generated--', BFSanslist[3])
    global BFStime_elapsed
    BFStime_elapsed = time.process_time() - time_start
    print('\nTime Elapsed for BFS --', BFStime_elapsed, 'seconds')
    print('---------------------------------------------------')


def idsCall():
    if dirtlist is None:
        return
    time_start = time.process_time()
    initialDirtTuple = list_to_xy_coord(dirtlist)
    print('-------------------------IDS--------------------------')
    print('Initial Dirt List --', initialDirtTuple)
    finalDirtTuple = []
    initalState = State([vc_x, vc_y], initialDirtTuple)
    finalState = State([9, 9], finalDirtTuple)
    global IDSanslist
    IDSanslist = ids(initalState, finalState)
    print('Action Sequence --', IDSanslist[0], '\nPath Cost --', IDSanslist[1], '\nTotal no of nodes created --',
          IDSanslist[2], '\nMax size of auxiliary queue generated--', IDSanslist[3])
    global IDStime_elapsed
    IDStime_elapsed = time.process_time() - time_start
    print('\nTime Elapsed for IDS --', IDStime_elapsed, 'seconds')
    print('---------------------------------------------------')


def allAnalysis():
    completeAnalysis(dirtlist, BFSanslist, IDSanslist, BFStime_elapsed, IDStime_elapsed,vc_x,vc_y)



############################### MAIN FUNCTION ################################

if __name__ == '__main__':
    window = Tk()
    window.title('AI Assignment 1 - SELECT OPTION ')
    window.geometry('900x900')

    b1 = Button(window, width=29, text='Option 1 - Room Environment', command=roomEnvGUI)
    b1.pack()
    b1.place(x=300, y=10)

    b2 = Button(window, width=29, text='Option 2 - BFS Path and Cost', command=bfsCall)
    b2.pack()
    b2.place(x=300, y=60)

    b3 = Button(window, width=29, text='Option 3 - IDS Path and Cost', command=idsCall)
    b3.pack()
    b3.place(x=300, y=110)

    b4 = Button(window, width=29, text='Option 4 - All Analysis', command=allAnalysis)
    b4.pack()
    b4.place(x=300, y=160)

    e1 = Entry(window, width=35)
    e1.insert(END, 'Erase it and enter integer P value')
    e1.pack()
    e1.place(x=300, y=210)

    e2 = Entry(window, width=35)
    e2.insert(END, 'Enter initial agent position - ul/ur/bl/br')
    e2.pack()
    e2.place(x=300, y=240)

    l1 = Label(window, relief=GROOVE, wraplength =900, justify =LEFT, text='***use p = 5 for results in few minutes***\n*****HOW TO USE******\n- Room size is fixed = 10x10\n- Enter the value of p in 1st box.\n- Enter where you want your vacuum cleaner to be initially - ul(upper left)/ur(upper right)/bl(bottom left)/br(bottom right).\n- Enter p as integer only and position as ul/ur/bl/br (lowercase) only for working.\n- Enter both values first, then click on Option 1 to see the initial room environment.\n- Next click on option 2/ option 3 (in any order, but both before option 4), check the console for print statements.\n  (you\'ll have to wait for many minutes for both option if p value is large)\n- FOR COMBINED ANALYSIS (both BFS/IDS) IN FEW MINUTES USE p = 5 or 6\n- Then click on option 4 for detailed and GUI path analysis of both option 2 and 3 for same initial room environment.\n- *R12* analysis is for both BFS/IDS running 10 times with p=2 (i.e. every time different room environment with dirt on 2 tiles only).\n\n---LIMITATIONS---\n- Independetly (can handle more on powerful machine).\n   BFS-> Room size handled - 10x10, p=10, time=42 minutes approx.\n	IDS-> Room size handled - 10x10, p=20, time=28 minutes approx.\n- Combined analysis\n	Use p not more than 5 or 6, for results in lesser minutes.\n\n################ WARNING ################\nOption 2 and 3 will take the latest room environment generated from Option 1\nSo if you have clicked 2/3 times on Option 1, close all the window generated form Option 1,\nthen freshly click on Option 1 and proceed.\nIf Option 1 is clicked in between of Option 2/3, the room environmet will change and\nOption 2 and 3 will produce different results and Option 4 may not work properly.\n########## PLEASE CLICK IN ORDER ########## ')
    l1.pack()
    l1.place(x=53,y=280)

    window.mainloop()

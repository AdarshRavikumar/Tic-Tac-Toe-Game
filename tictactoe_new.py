# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 01:05:07 2018

@author: Adarsh
"""


l1=[['','',''],['','',''],['','','']]
act=[[1,2,3],[4,5,6],[7,8,9]]
def display(a,c):
    
    for i in range(0,3):
        for j in range(0,3):
            
            if a in act[i]:
                if a==act[i][j]:
                    l1[i][j]=c
                
    print('\n',l1[0],'\n',l1[1],'\n',l1[2],'\n')

    

       
    


print('Welcome to tic tac toe' )
print('Instructions\n Since there are 9 squares where you can mark any box using its respective nummber (1-9)\n The boxes are numbered as\n1 2 3\n4 5 6\n7 8 9\n'
      ,'Ex1. suppose u want to mark a box in second row and second column u choose number 5\n','Ex2: suppose u want to mark box in first row and third column, then use number 3\n','Its a 2 player game where each player gets a turn alternatively\n')

u1=[]
u2=[]
win_mov=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

i=0
f=0
fl=0
ze=0
fl1=0
k2=0
u11=[]
u22=[]

print('\n',l1[0],'\n',l1[1],'\n',l1[2],'\n')
while True:
   
    f=0
    if k2==0:
       
        a1=int(input("user1, move"))
        # checking if the number is already used by user1 or user2
        if a1 not in u1 and a1 not in u2 and a1 in [1,2,3,4,5,6,7,8,9]:
            u1.append(a1)
            
            print('The matrix of Tic-Tac-Toe')
            display(a1,'*')
            for j in range(0,8):
                fl=0
                for k in range(0,3):
                    
                    if(win_mov[j][k] not in u1):
                        fl=1
                        break;
                if fl==0:
                    print('\nUSER 1 winner')
                    
                    ze=1
                    break;
            
                    
            
        else:
            print('already used block')
            f=1
            continue
    if f==0 and ze==0 and (len(u1)+len(u2)<9):
        k2=0
        
        a2=int(input("user2, move"))
        if a2 not in u1 and a2 not in u2 and a2 in [1,2,3,4,5,6,7,8,9]:
            u2.append(a2)
            
            print('The matrix of Tic-Tac-Toe')
            display(a2,'$')
            for j in range(0,8):
               fl1=0
               for k in range(0,3):
                 if(win_mov[j][k] not in u2):
                    fl1=1
                    break;
               if fl1==0:
                 print('\nUSER 2 winner')
                 
                 ze=1
                 break
        
        else:
            print('already used block')
            k2=1
            continue
            
    if ze==1:
        break;
    if(len(u1)+len(u2)>=9):
        break;
        
if fl==1 and fl1==1:
    print("DRAW MATCH")
    

ch=input("Press Enter to exit")
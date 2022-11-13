# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 11:26:44 2022

@author: shash
"""
b=[" "]*9
def board():
 r="|{} |{} |{} |\n|{} |{} |{} |\n|{} |{} |{} |".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8])
 print(r)
#while True:
 #print(r)
def move(icon):
 if icon=='X':
     num='{}'.format(p1)
 elif icon=='O':
     num='{}'.format(p2)
 print('\n')
 print('your turn player {}'.format(num))
 #print('enter position\n')
 n=int(input('enter your position\n'))#.strip())
 if(b[n-1]==" "):
   b[n-1]=icon
  # a()
 else:
   print('space led ra bal ga')
#print()
def vict(icon):
    if(b[0]==icon and b[1]==icon and b[2]==icon) or \
      (b[3]==icon and b[4]==icon and b[5]==icon) or \
      (b[6]==icon and b[7]==icon and b[8]==icon) or \
      (b[0]==icon and b[3]==icon and b[6]==icon) or \
      (b[1]==icon and b[4]==icon and b[7]==icon) or \
      (b[2]==icon and b[5]==icon and b[8]==icon) or \
      (b[0]==icon and b[4]==icon and b[8]==icon) or \
      (b[2]==icon and b[4]==icon and b[6]==icon):
        return True
    else:
        return False
def draw():
    if " " not in b:
        return True
    else:
        return False
p1=(input('enter player 1 name\n'))
p2=(input('enter player 2 name\n'))
while True:
      
      board()
      move('X')
      board()
      if vict('X'):
          print('{} won'.format(p1))
          break
      elif draw():
         print('draw')
         break
      move('O')
      #board()
      if vict('O'):
         
         print('{} won'.format(p2))
         break
      elif draw():
         print('its draw')
         break

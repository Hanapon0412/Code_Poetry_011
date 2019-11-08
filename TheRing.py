#Three Rings for the Elven-kings under the sky,
#Seven for the Dwarf-lords in their halls of stone,
#Nine for Mortal Men doomed to die,
#One for the Dark Lord on his dark throne
#In the Land of Mordor where the Shadows lie.
#One Ring to rule them all, One Ring to find them,
#One Ring to bring them all and in the darkness bind them
#In the Land of Mordor where the Shadows lie.
import time
import subprocess
import os
three = 3
ring = ''
for theElvenKings in 'the sky':
    ring += ''
    
seven = 7 
for theDwarfLords in 'halls of stone':
    ring += ''
    
nine = 9
for mortalMen in 'doomed to die':
    ring += ''
    
one = 1
for theDarkLord in 'his dark throne':
    ring += ''

for whereTheShadowLie in ' the land of mordor':
    ring += ''

one * ring > 'to rule them all'
one * ring.find('them') 
one * ring > 'to bring them all and in the darkness bing them'
ring += '     O\n\n    '


for whereTheShadowLie in ' the land of mordor':
    ring += 'O'
    if whereTheShadowLie == 'h' : ring += '\n\n   '
    if whereTheShadowLie == 'n' : ring += '\n\n'


while 1:
    
    print ring.replace("I", "O")
    time.sleep(1)
    os.system('clear')
    
    
    print ring.replace("O", "I")
    time.sleep(1) 
    os.system('clear')
    
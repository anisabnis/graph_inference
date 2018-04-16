import os
#dir = ['quest', '6et1', 'geant', 'bellcanada', 'columbus', 'sinet']
dir = ['6et1', 'sinet']
for d in dir:
    for i in range(2,4):
        os.system('./script.sh ./final/' + d + ' ' + str(i))

with open('globulete.txt', 'r') as f:
    a=f.readline()
rosii=int(a)+3
albe=int(a)+rosii-2
with open('bradut.txt', 'w') as f:
    f.write(str(int(a)+rosii+albe))



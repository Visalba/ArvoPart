import random

# given the m note obtains the +t note
mat = [
    [0,0,2,2,4,4,4],    # 0
    [2,2,4,4,7,7,7],    # t+1
    [4,4,7,7,9,9,9],    # t+2
    [7,7,9,9,11,11,11], # t+3
    [-7,-5,-5,-3,-3,0,0],  # t-3
    [-5,-3,-3,0,0,2,2], # t-2
    [-3,0,0,2,2,4,4,4]  # t-1
]
def getTvoice(m,t):
    oct, m = m//7, m%7
    return mat[t][m]+oct*7

vocs = [0,2,4]   # voices of the base chord = tint voices
tVocs = [0,0,1,1,2,2,2] # base for addition t voice for each note
def getTvoice(m,t):
    oct, m = m//7, m%7
    if t<0: 
        m = (m+6)%7
        t = t+4
    v = tVocs[m]+t
    oct, ind = oct+v//3, v%3
    return vocs[ind]+oct*7
# print(getTvoice(4,1))
# test according to table of https://aestheticcomplexity.wordpress.com/2014/03/23/mapping-tintinnabuli-transformations/
l = 'abcdefg'   
for n in range(-14,-7):  # range(7)
    t = getTvoice(n,-3)
    print(n,t,'  ',l[n%7],l[t%7])
# tintinabulation of a motive with random +1 +2 Tvoice
def tint(mot):
    mt = []
    inc = 0
    for n in mot:
        if random.random()<0.5: inc=1
        elif random.random()<0.8: inc=2 
        else: inc=3
        mt.append(getTvoice(n,inc))
    return mt

spaces = SynthDef("spaces")
Root.default = "A"
Scale.default = "minor"
Clock.bpm=90

# expansion descendente por grados contiguos + ascendente
def expand(root,ext):
    return [root-i for i in range(ext)] + [root+ext-i-1 for i in range(ext)]
    #          desdendentes                      ascendentes    

fratres = []
root_note = 4
for j in range(0,9):
    ini = [expand(4-3*j,i) for i in range(2,5)]  # primeras 3 expansiones, 3 compases
    fratres.extend(ini + [m[::-1] for m in ini])   # añadimos los compases invertidos
    
durs = [[2] + [1]*(len(c)-2) +[2] for c in fratres]  # generacion de figuras/duraciones


print(fratres)
print(durs)

f = [x for sublist in fratres for x in sublist]
d = [x for sublist in durs for x in sublist]
t = tint(f)

print('f ', f)
print('t ', t)
print('d ', d)



Clock.bpm=60
Clock.set_time(-1)
p1 >> MidiOut(f, dur=d, channel = 1)
c1 >> MidiOut(t, dur=d, channel = 2)

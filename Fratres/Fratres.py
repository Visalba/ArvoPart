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
ini = [expand(3,i) for i in range(2,5)]  # primeras 3 expansiones, 3 compases
fratres = ini + [m[::-1] for m in ini]   # añadimos los compases invertidos
durs = [[2] + [1]*(len(c)-2) +[2] for c in fratres]  # generacion de figuras/duraciones


print(fratres)
print(durs)

f = [x for sublist in fratres for x in sublist]
d = [x for sublist in durs for x in sublist]
t = tint(f)
print('f ', f)
print('t ', t)
print('d ', d)

Clock.bpm=80
p1 >> keys(f, dur=d, room=.8, mix=0.4, spin=2, amp=0.8)

p2 >> bell(t, dur=d, delay=0.01, room=.8, mix = 0.4, spin=7, amp=0.4)


p2 >> glass(
    dur=1,
    amp=PWhite(0.02,0.05),
    #pan=linvar([-0.8,0.8],2),
    spin=2,
    hpf=linvar([400,1200],4), hpr=0.8,
    oct=6,
    ) + (0,P[2,4])
p3 >> spaces(
    amp=0.1,    
    pan=linvar([-.8,.8],4),
    hpf=linvar([400,1200],4), hpr=0.8,
    room=0.4,mix=0.3,
    oct=3) + (0,2,4)

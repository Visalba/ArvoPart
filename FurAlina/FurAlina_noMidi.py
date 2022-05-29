mat = [
    [-2,0,0,2,2,2,5],    # 0
    [0,0,2,2,2,5,5],    # t+1
    [2,2,5,5,7,7,7],    # t+2
    [5,5,7,7,9,9,9], # t+3
    [-7,-5,-5,-3,-3,0,0],  # t-3
    [-5,-3,-3,0,0,2,2], # t-2
    [-3,0,0,2,2,4,4,4]  # t-1
]
def getTvoice(m,t):
    oct, m = m//7, m%7
    return mat[t][m]+oct*7
    
def getTvoiceFromMelody(motive, tintinnabuli):
    tvoice = []
    for note in motive:
        tvoice.append(getTvoice(note, tintinnabuli))
    return tvoice
#================================= Für Alina ==============================
chords = [(-2, 0, 2),(8, 10, 12),(3, 5, 0),(9, 11, 13)]
Clock.bpm = 60
Root.default("D")
mVoice = [6,7,8,9,9,8,7,6,5,9,8,9,7,8,7,9,12,13,12,7,8,7,5,6,9,7,8,9,14,13,12,5,9,10,11,7,8,5,6,7,6,5,11,10,11,5,6,9,10,7,8,9,9,7,5,0,1,-2,2,7,5,0,5,6,]
#.stutter(n=2)
#Returns a new pattern with each value repeated n number of times. 
#If n is a pattern itself, then each value is repeated by the number at the same index in the given pattern.
furAlina = P[1,4].stutter([[1,2,3,4,5,6,7,6,5,4,3,2,1],[1]])
Clock.set_time(-1)#Para comenzar desde el primer compás
p1 >> keys(mVoice, dur = furAlina, oct = 6)
p2 >> keys(getTvoiceFromMelody(mVoice, 0), dur = furAlina, oct = 6)


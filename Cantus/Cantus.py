#Cantus in Memory Of Benjamin Britten
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
#
def getTvoiceFromMelody(motive, tintinnabuli):
    tvoice = []
    for note in motive:
        tvoice.append(getTvoice(note, tintinnabuli))
    return tvoice
#====================================================================
base = [14]
num=17
notes = [comp for i in range(19) for comp in list(range(14,14-i,-1))]
Root.default("A")
Scale.default = "minor"
Clock.bpm = 112
Clock.set_time(-1)

ampli = 0.1;  

Clock.set_time(-1)
p1 >> keys([0,2,4], amp = linvar([0, 5], [100, inf]))

print(Clock.now(), linvar([0, inf]))


#Violins
Clock.schedule(lambda: #Comienza en el beat 4
		p1 >> MidiOut(notes, dur=[1,2], 
				oct=5, amp=0.1, channel = 0), Clock.now()+4)
Clock.schedule(lambda: #Comienza en el beat 7
		p2 >> MidiOut(getTvoiceFromMelody(notes, 4), dur = [1,2], 
				oct=5, channel = 1, sus = p1.dur-0.1), Clock.now()+4)
#Violins II
Clock.schedule(lambda: 
		v1 >> MidiOut(notes, dur=[2,4], 
				oct = 4, channel = 2), Clock.now()+7)
Clock.schedule(lambda: 
		v2 >> MidiOut(getTvoiceFromMelody(notes, 4), dur = [2,4], 
				oct = 4, channel = 3, sus = p1.dur-0.01), Clock.now()+7)
#Violas
Clock.schedule(lambda: 
		l3 >> MidiOut(notes, dur=[4,8], 
				oct = 4, channel = 2), Clock.now()+13)
#Cellos
Clock.schedule(lambda: 
		c1 >> MidiOut(notes, dur=[8,16], 
				oct = 3, channel = 5), Clock.now()+25)
Clock.schedule(lambda: 
		c2 >> MidiOut(getTvoiceFromMelody(notes, 4), dur = [8,16], 
				oct = 3, channel = 6, sus = p1.dur-0.01), Clock.now()+25)
#Contrabasses
Clock.schedule(lambda: 
		b1 >> MidiOut(notes, dur=[16,32], 
				oct = 2, channel = 7, sus = p1.dur-0.01), Clock.now()+50)
Clock.schedule(lambda: 
		b2 >> MidiOut(getTvoiceFromMelody(notes, 4), dur = [16,32], amp=0.1, 
				oct = 2, channel = 8, sus = p1.dur-1), Clock.now()+50)

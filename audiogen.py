import numpy as np
import math
from scipy.io.wavfile import write

sps = 44100; #samples per second 

def createSin(fr,sec):
    ret = np.array([])
    x = 0
    relfr = fr/sps
    for i in range(sec):
        for j in range(sps):
            #print(math.sin(x))
            ret = np.append(ret,math.sin(relfr*x))
            x += sps/fr
        print("sec: ", i)
    return ret
#
#def createSquare(fr,sec):
#    ret = np.array([])
#    x = 0
#    for i in range(sec):
#        for j in range(sps):
#            if(x % fr == )
#            ret = np.append(ret,math.sin(fr*x))
#            x += 1
#        print("sec: ", i)
#    return ret
            


data = createSin(4000,3)
print(data)


#data = np.random.uniform(-1,1,44100*10) # 44100 random samples between -1 and 1
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('test.wav', sps, scaled)
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
            ret = np.append(ret,math.sin(relfr*x))
            x += sps/fr
        print("sec: ", i)
    return ret

def createSquare(fr,sec):
    ret = np.array([])
    x = 0
    relfr = fr/sps
    for i in range(sec):
        for j in range(sps):
            if (math.sin(relfr*x) > 0 ):
                ret = np.append(ret,1)
            else:
                ret = np.append(ret,-1)
            x += sps/fr
        print("sec: ", i)
    return ret

def createSaw(fr,sec):
    ret = np.array([])
    x = 0
    relfr = fr/sps
    for i in range(sec):
        for j in range(sps):
            if (math.sin(relfr*x) < 0 ):
                ret = np.append(ret,1)
                x = 0
            else:
                ret = np.append(ret,-x*relfr+1)
            x += sps/fr
        print("sec: ", i)
    return ret


data = createSaw(4000,3)
print(data)


#data = np.random.uniform(-1,1,44100*10) # 44100 random samples between -1 and 1
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('test.wav', sps, scaled)
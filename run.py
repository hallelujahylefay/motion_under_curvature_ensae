import numpy as np
import sys
def inOmega(x):
    return (x[0]**2+x[1]**2<=1)

Vect = [[np.cos(k/(2*np.pi)), np.sin(k/(2*np.pi))] for k in range(20)]

epsilon = 0.1

def vbStar(S):
    Sp = []
    for k in range(len(S)):
        for l in range(k+1, len(S)):
            s = S[k]
            sp = S[l]
            print(sp)
            if sp[2][-1]==s[2][-1]:
                if sp[1] > s[1]:
                    Sp.append(sp)
                else:
                     Sp.append(s)
    kmin = 0
    print(len(Sp))
    for k in range(len(Sp)):
        if Sp[k][1] < Sp[kmin][1]:
            kmin = k
    print(k)
    vstar = Sp[kmin][2][-1]
    B = []
    for k in range(len(S)):
        if S[k][2][-1]==vstar:
            B.append(S[k])
    if B[0][1]>B[1][1]:
        bstar = B[0][3][-1]
    else:
        bstar = B[1][3][-1]
    
    for k in range(len(S)):
        if S[k][2][-1]==vstar and S[k][3][-1]==bstar:
            tstar = S[k][1]
    return vstar, bstar, tstar

def f(x, t, V, B):
    if (inOmega(x) and t<=0.5):
        S = []
        for v in Vect:
            for b in [-1, 1]:
                Vp = V
                Vp.append(v)
                Bp = B
                Bp.append(b)
                S.append(f([x[0]+1.41*epsilon*b*v[0], x[1]+1.41*epsilon*b*v[1]], t+epsilon**2, Vp, Bp))
                print(S)
        vstar, bstar, tstar = vbStar(S)
        V.append(vstar)
        B.append(bstar)
        t = tstar
        x = [x[0]+1.41*epsilon*bstar*vstar[0], x[1]+1.41*epsilon*bstar*vstar[1]]
        #print("("+str(x[0])+", "+str(x[1])+")")
    elif not(inOmega(x)):
        print("sortie en " + str(t)+ " ("+str(x[0])+", "+str(x[1])+")" + str(V) + str(B))
        sys.exit(0)
    return (x, t, V, B)

#f([0, 0],0, [], [])
vbStar([[[0,0], 1.01, [Vect[0], Vect[1]], [-1]]])


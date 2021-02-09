import numpy as np

N = 1000000
throws = 0
win_heads = 0
win_tails = 0
outcomes = []
gen = np.random.default_rng()

for i in range(N):
    throw = 0
    heads = 0
    tails = 0
    while heads < 3 and tails < 3:
        throw += 1
        if gen.uniform() < 0.5:
            heads += 1
        else:
            tails += 1
        #print(i,heads,tails)
    if heads == 3:
        win_heads += 1
    else:
        win_tails += 1
    outcomes.append(throw)
    #print('WON')
    throws += throw
    
outcomes = np.array(outcomes)
throws /= N
win_heads /= N
win_tails /= N
print(throws, win_heads, win_tails)

# In[]
import scipy.stats as sts

M = 100000
K = 1000

sg = outcomes.std()
t_975=sts.t.ppf(q = 0.975, df = M-1)

a = np.array([ gen.choice(outcomes, size = M, replace = False).mean() for i in range(K) ])

print(a.mean())
print(4.125-t_975*sg/np.sqrt(M),
      4.125+t_975*sg/np.sqrt(M))
print( ( sts.t.cdf(-(a.mean()-4.125)/(sg/np.sqrt(M)), df = M-1) ) *2)
'''
Is coding inside methods faster than main program?
yes, It is 
'''
import time

def v():
    j1 = time.time()
    j = 0
    for i in xrange(100000000, 1, -1):
        j += i
        # print j 
    j2 = time.time()
    j3 = j2 - j1
    print j3

if  __name__ == "__main__":
    v()
    
''' Time to run    
python main-vs-methods.py 
2.21884703636 sec
This same code without method takes 5.27098011971 sec
'''

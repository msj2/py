j1 = time.time()
j = 0
for i in xrange(10000000000, 1, -1):
    j += i
    # print j 
j2 = time.time()
j3 = j2 - j1
print j3

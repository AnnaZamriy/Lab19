import pickle

fname = "result.bin"
list1 = []
for n in range(100, 1000):
    if n % 7 == 0 and str(n).endswith('1'):
            if n % 3 == 0:
                list1.append(n)



f = open(fname, 'wb')
pickle.dump(list1, f)
f.close()

import pickle 
fname="result.bin" 
f=open(fname,"rb") 
L=pickle.load(f) 
f.close() 
print(L)
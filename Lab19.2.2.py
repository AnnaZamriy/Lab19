import pickle

f = open("result2.bin", "rb")
frequency = pickle.load(f)

for char, count in frequency.items():
    print(f"'{char}': {count}")

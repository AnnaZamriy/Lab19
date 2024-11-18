import pickle
from collections import Counter

text = input("Введіть рядок символів англійського алфавіту: ").lower()

f1 = Counter(char for char in text if char.isalpha())


f = open("result2.bin", "wb")
pickle.dump(f1, f)


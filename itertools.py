import itertools
import collections

items = ["A", "B", "C"]
permutations = list(itertools.permutations(items))
print(f"Permutations of {items}: {permutations}")

text = "hello world"
counter = collections.Counter(text)
print(f"Character frequency in '{text}': {counter}")
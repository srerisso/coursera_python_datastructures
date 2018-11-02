# coursera_python_datastructures

## Week 1 :

- Strings

## Week 2 :

- Installing Python

## Week 3 : Files

- Files

## Week 4 : Lists

- Lists introduction.
- Manipulating Lists. sum(), max(), min(), slice a list, len()
- Lists and Strings. split(), double splitting


## Week 5 : Dictionaries

- Dictionaries. Bag of elements with an id. Key / value pairs.
- Counting with dictionaries. Histograms. get method (x = counts.get(name, 0))

Ejemplo:
```
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
  counts[name] = counts.get(name,0) + 1

print(counts)
```

Ejemplo 2:
```
counts = dict()
line = input('enter a line of text')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
  counts[word] = counts.get(word,0) + 1

print('Counts', counts)
```

- .keys(), .values(), .items() items devuelve una lista de Tuples.

```
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100 }

for k,v in jjj.items():
  print(k, v)
```  

## Week 6 : Tuples

- Tuples

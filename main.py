'''
D = {'Anita': 23, 'Ashwin': 43,
     'Ahana': '24',
     'Adarsh': 30, 'Archana': 15}
try:
    # iterates through the keys from left to right
    for key in D:
        value = D[key]
        if type(value) == str:
            raise 'Error'
        print(f'{key}:{value}')
except:
    print("Values cannot be strings")
    
L = [1, 3, -1, 4, -2, 5, 3]

try:
    n = 10
    for i in range(n):
        if L[i] < 0:
            L[i] = 0
except IndexError:
    for i in range(n - len(L)):
        L.append(0)
finally:
    print(L)

try:
    L = [x for x in range(10)]
    f = open('numbers.txt', 'w')
    for x in L:
      #this x should have been str as argument for write(), but it is int 
        f.write(x)
except FileNotFoundError:
    print('File was not found')
#except:
#    print('This is some other error')
finally:
    print('The file has been closed')
    f.close()
  
L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
print(L)
triplets = [(x, y, z) for x in range(1, 100) 
                      for y in range(x + 1, 100)
                      for z in range(y + 1, 100)
                      if x ** 2 + y ** 2 == z ** 2]
print(triplets)



print([word for word in input().split(',') if 'e' not in word])
P = input().split(',')
L = [ ]
for word in P:
    if 'e' not in word:
        L.append(word)
print(L)'''
L = [word for word in input().split(',') if 'e' not in word]
print(L)

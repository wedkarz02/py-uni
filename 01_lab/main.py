
# Typy danych i zmienne

print(type(5))          # int
print(type("Ala"))      # str
print(type(7))          # int
print(type(7.42))       # float
print(type(-14))        # int
print(type(3 + 2j))     # complex
print(type(True))       # bool

a = 3
b = 3.14
c = 3.14 - 3j
d = "Iskra"

print(float(a))         # 3.0
print(int(b))           # 3
print(int(-b))          # -3
print(complex(a))       # (3+0j)
print(complex(b))       # (3.14+0j)
# TypeError:
# print(float(c))         # 3.0
# print(int(c))           
print(str(a))           # '3'
print(str(b))           # '3.14'

a = 10
b = "Kot"
c = 3.14

print(type(a))          # int
print(type(b))          # str
print(type(c))          # float

# a + b * c - b
b = 2 
result = a + b * c
print(result)           # 16.28
print(type(result))     # float

division_result = a / b
subtraction_result = a - b
print(division_result)  # 5.0
print(subtraction_result) # 8

# Liczby

print(0b1010)           # 10 (binary system)
print(0xa)              # 10 (hexadecimal system)
print(0o123)            # 83 (octal system)
print(0b11 + 0b100000000)  # 259 (11 + 256)

print(bin(10))          # '0b1010'
print(oct(10))          # '0o12'
print(hex(10))          # '0xa'

print(bin(13) + bin(8))  # '0b1101' + '0b1000' = '0b11010'
print(bin(13 + 8))        # '0b10101'

print(3.14 + 2.71)      # 5.85
print(5.0 / 2.0)        # 2.5
print(type(6 / 3))      # float
print(type(6 / 4))      # float

print(3j * 2j)          # -6.0 (type: complex)

x = 4 - 3j
y = 5 + 1.2j
print(x + y)           # 9 - 1.8j
print(x * y)           # 27.0 + 1.2j
print(x / y)           # 0.7482993197278912 - 0.5595238095238095j
print(x ** 2)          # 7 - 24j

print(True + 12)       # 13
print(False * 7)       # 0

# Operatory

a = 10
b = 3
c = 0.3
d = -2

print(a // b)          
print(a % b)           
print(a ** b)          

print(a // c)          
print(-a // c)         

print(5 == 5)          
print(5 != 5)          
print(5 > 3)           
print(5 < 3)           
print(5 >= 5)          
print(5 <= 5)          

print(10 == 10)        # True
print(10 != 5)         # True
print(10 > 5)          # True
print(10 < 5)          # False
print(10 >= 10)        # True
print(10 <= 5)         # False

a = 4
A = "Iskra"

print(a == A)          # False:
print(a != A)          # True:

print(2**10 < 3**7)    # True:
print(0x1a > 0b10111)  # True:
print(0b1010010011110101 == 0xa4f5)  # True

a = 5
b = 8

print((a > 0) and (b < 10))  # True
print((a > 0) or (b < 5))    # True
print(not (a > 0))           # False

# TypeError:
# result = 1j * 2j < 5

# Ciągi znaków

s1 = 'Ala ma kota'
s2 = "Kot ma Alę"

print(type(s1))  # <class 'str'>
print(type(s2))  # <class 'str'>

print(len(s1))
print(len(s2))

# TypeError
# print(len(5))  

print(s1 + " " + s2)  
print(s1 * 2)         

print(s1.upper())     
print(s1.lower())     
print(s1.find('ma'))  
print(s1.replace('kota', 'psa'))

print(s1[2])         
print(s1[0])         
print(s1[-3])        
print(s2[7])         
print(s1[3:6])       
print(s2[:5])        
print(s1[4:])        
print(s1[::3])       
print(s2[1:7:2])     

s = """Two roads diverged in the woods and I
—I took the one less traveled by"""
print(s)

p = "Two roads diverged in the woods and I"
s = "—I took the one less traveled by"

print(p, s)                          
print(p + s)                         
print(p, s, sep='\n')                
print(p, s, sep='?')                 
print(p, s, sep=' ')                 
print(p, s, sep='')                  
print(p, s, sep='\n', end='.')       
print(p, s, sep='\n', end='\n!')     

# Typy danych - ciąg dalszy

l = [1, 2, "Ala", 3.14]   # List
t = (1, 2, "Ala", 3.14)   # Tuple
s = {1, 2, "Ala", 3.14}   # Set

print(type(l))  # <class 'list'>
print(type(t))  # <class 'tuple'>
print(type(s))  # <class 'set'>

print(type(range(6)))     
print(type(b"Hello"))     
print(type(None))         
print(type({"name": "Iskra", "species": "dog"})) 

print(type(frozenset({"apple", "cherry"}))) 
print(type(bytearray(5)))                   
print(type(memoryview(bytes(5))))           

# Listy

l = ["jabłko", 5, 3.14, True, [1, 2, 3]]

print(l[2])        
print(l[0])        
print(l[-2])       
l[2] = "gruszka"   

print(l[2:])       
print(l[:2])       
print(l[1:3])      
print(l[::2])      

l[3] = "Arbuz"     
l[0] = "Truskawka" 
print(l)           

print(len(l))      

l.append("Malina") 
print(l)           

l.insert(1, "Kiwi")
l.insert(13, "Ananas")
print(l)           
l[5:5] = [1, 2, 3] 
l[9:9] = ["Banan"] 
print(l)           

l.pop(2)           
print(l)           
del l[3]           
print(l)           

new_list = l + [4, 7, "Brzoskwinia"]
print(new_list)   

l.extend([4, 7, "Brzoskwinia"])
print(l) 

s = "Pies"
r = s
s = "Kot"
print(s) 
print(r) 

m = [1, 2, 3, ["a", "b", "c"]]
n = m
m[0] = 8
print(m) 
print(n) 

n = m.copy()
m[1] = -4
print(m) 
print(n) 

import os
if not os.path.isdir(r'/tmp/Python'):
    os.mkdir(r'/tmp/Python')
    # -----
    # 1
f = open(r'/tmp/Python/spam.txt', 'w', encoding='utf8')
for i in range(10):
    f.write(f"ligne {i+1}\n")
    f.close()

# !type ./spam.txt

f = open(r'/tmp/Python/spam.txt', 'r', encoding='utf8')
f2 = open(r'/tmp/Python/spam2.txt', 'w', encoding='utf8')
for line in f:
    line = line.split()
    line[0] = line[0].upper()
    f2.write(",".join(line) + "\n")
    f.close()
    f2.close()

# !type /tmp/Python/spam.txt
# !type /tmp/Python/spam2.txt

# -----
# 2
with open(r'/tmp/Python/spam.txt', 'r', encoding='utf8') as f:
    for line in f:
        print(line, end='')
with open(r'/tmp/Python/spam2.txt', 'r', encoding='utf8') as f:
    for line in f:
        print(line, end='')

# -----
with open(r'/tmp/Python/spam.bin', 'bw') as f:
    for i in range(10):
        f.write(b'\x3d')
with open(r'/tmp/Python/spam.bin', 'r') as f:
    for line in f:
        print(line, end='')
        print('\n')

# os.remove(r'/tmp/Python/spam.txt')
# os.remove(r'/tmp/Python/spam2.txt')
# os.remove(r'/tmp/Python/spam.bin')

# -----
lines = "abc" + "\n" + "def" + "\n"
print(lines, end="")
print(repr(lines))

with open("/tmp/Python/foo.txt", "a", encoding='utf-8') as sortie:
    for i in range(100, 102):
        sortie.write(f"{i}\n")

with open("/tmp/Python/foo.txt", encoding='utf-8') as entree:
    for line in entree:
        # line contient déjà un retour à la ligne
        print(line, end='')

with open("/tmp/Python/foo.txt", encoding='utf-8') as entree:
    full_contents = entree.read()
    print(f"Contenu complet\n{full_contents}", end="")

with open("/tmp/Python/foo.txt", encoding='utf-8') as entree:
    for bloc in range(2):
        print(f"Bloc {bloc} >>{repr(entree.read(4))}<<")


with open('/tmp/Python/foo.txt', encoding='utf-8') as strfile:
    for line in strfile:
        print("on a lu un objet de type", type(line))

# -----
with open('/tmp/Python/strbytes', 'w', encoding='utf-8') as output:
    output.write("déjà l'été\n")
with open('/tmp/Python/strbytes', 'rb') as bytesfile:
    # on lit tout le contenu
    octets = bytesfile.read()
    # qui est de type bytes
    print("on a lu un objet de type", type(octets))
    # si on regarde chaque octet un par un
    for i, octet in enumerate(octets):
        print(f"{i} → {repr(chr(octet))} [{hex(octet)}]")

#
with open('/tmp/Python/strbytes', encoding='utf-8') as textfile:
    print(f"en mode texte, {len(textfile.read())} caractères")
with open('/tmp/Python/strbytes', 'rb') as binfile:
    print(f"en mode binaire, {len(binfile.read())} octets")


# module pathlib
from pathlib import Path
path = Path('/tmp/Python')
os.chdir(path)
nom = 'fichier-temoin'
nom
path = Path(nom)
path
path.exists()
with open(nom, 'w', encoding='utf-8') as output:
    output.write('0123456789\n')
    path.exists()
    path.stat()
    path.stat().st_size
    mtime = path.stat().st_mtime
    mtime
    from datetime import datetime
    mtime_datetime = datetime.fromtimestamp(mtime)
    mtime_datetime
    f"{mtime_datetime:%H:%M}"

# destroy file
path.unlink()
path.exists()
with open(nom, 'w', encoding='utf-8') as output:
    output.write('0123456789\n')

path.exists()

try:
    path.unlink()
except FileNotFoundError:
    print("no need to remove")
finally:
    print("Test")
    path.exists()
    path.name
    os.mkdir(r'./data')
    Path('data/file1.txt').touch()
    Path('data/file2.txt').touch()
    dirpath = Path('/tmp/Python/data/')
    dirpath
for afile in dirpath.glob("*.txt"):
    print("A file as been found: ", end='')
    print(afile)

type(path)
from pathlib import PosixPath
issubclass(PosixPath, Path)
isinstance(path, Path)

# File formats
import json

# En partant d'une donnée construite à partir de types de base
data = [
    # des types qui ne posent pas de problème
    [1, 2, 'a', [3.23, 4.32], {'eric': 32, 'jean': 43}],
    # un tuple
    (1, 2, 3),
]

# sauver ceci dans un fichier
with open("s1.json", "w", encoding='utf-8') as json_output:
    json.dump(data, json_output)

# et relire le résultat
with open("s1.json", encoding='utf-8') as json_input:
    data2 = json.load(json_input)
    print(data2)

# le premier élément de data est intact,
# comme si on avait fait une *deep copy* en fait
print("première partie de data :", data[0] == data2[0])
# par contre le `tuple` se fait encoder comme une `list`
print("deuxième partie", "entrée", type(data[1]), "sortie", type(data2[1]))

# -----
# Tuples
t = ()
type(t)
t = (4,)
t
t = (True, 3.4, 18)
t
t = True, 3.4, 18
t
3.4 in t
t[1]
t[:2]
a = list(t)
a
a[0] = False
t = tuple(a)
t
(a, b) = [3, 4]
a
b
a, b = 3, 4
a
b
a = list(range(10))
a
x, *y = a
x
y
*x, y = a
x
y

# sans parenthèse ni virgule terminale
couple1 = 1, 2
# avec parenthèses
couple2 = (1, 2)
# avec virgule terminale
couple3 = 1, 2,
# avec parenthèses et virgule
couple4 = (1, 2,)

couple1 == couple4

mon_tuple = ([1, 2, 3],
             [4, 5, 6],
             [7, 8, 9])

# ATTENTION : ces deux premières formes ne construisent pas un tuple !
simple1 = 1
simple2 = (1)
# celles-ci par contre construisent bien un tuple
simple3 = 1,
simple4 = (1,)

type(simple2)
type(simple3)
simple3 == simple4

x = (1,)
(1,) == x
1, == x # error

tuple1 = (1, 2,)
tuple2 = (3, 4,)
print('addition', tuple1 + tuple2)

tuple1 = (1, 2,)
tuple1 += (3, 4,)
print('apres ajout', tuple1)

# on fabrique une liste pas à pas
liste = list(range(10))
liste[9] = 'Inconnu'
del liste [2:5]
liste

# on convertit le résultat en tuple
mon_tuple = tuple(liste)
mon_tuple

liste = range(10)
# ATTENTION : ceci redéfinit le symbole tuple
tuple = tuple(liste)
tuple

# si bien que maintenant on ne peut plus faire ceci
# car à ce point, tuple ne désigne plus le type tuple
# mais l'objet qu'on vient de créer
autre_liste = range(100)
autre_tuple = tuple(autre_liste) # error

del tuple # deallocate
tuple

# Unpacking
f1 = 0
f2 = 1
n = 10
for i in range(2, n + 1):
    f1, f2 = f2, f1 + f2
f1
f2

couple = (100, 'spam')
gauche = couple[0]
droite = couple[1]
print('gauche', gauche, 'droite', droite)
(gauche, droite) = couple
print('gauche', gauche, 'droite', droite)
gauche, droite = couple
print('gauche', gauche, 'droite', droite)

liste = [1, 2, 3]
[gauche, milieu, droit] = liste
print('gauche', gauche, 'milieu', milieu, 'droit', droit)

# membre droit: une liste
liste = [1, 2, 3]
# membre gauche : un tuple
gauche, milieu, droit = liste
print('gauche', gauche, 'milieu', milieu, 'droit', droit)

a = 1
b = 2
a, b = b, a
print('a', a, 'b', b)

reference = [1, 2, 3, 4, 5]
a, *b, c = reference
print(f"a={a} b={b} c={c}")

reference = range(20)
a, *b, c = reference
print(f"a={a} b={b} c={c}")

# si on sait que data contient prenom, nom, 
# et un nombre inconnu d'autres informations
data = [ 'Jean', 'Dupont', '061234567', '12', 'rue du four', '57000', 'METZ', ]

# on peut utiliser la variable _
# ce n'est pas une variable spéciale dans le langage,
# mais cela indique au lecteur que l'on ne va pas s'en servir
prenom, nom, *_ = data
print(f"prenom={prenom} nom={nom}")

# ceci en toute rigueur est légal
# mais en pratique on évite de le faire
entree = [1, 2, 3]
a, a, a = entree
print(f"a = {a}")

entree = [1, 2, 3]

_, milieu, _ = entree
print('milieu', milieu)

ignored, ignored, right = entree
print('right', right)

structure = ['abc', [(1, 2), ([3], 4)], 5]
(a, (b, ((trois,), c)), d) = structure
print('trois', trois)

(a, (b, ([trois], c)), d) = structure
print('trois', trois)

trois = structure[1][1][0][0]
print('trois', trois) # Flat is better than nested

# un exemple très alambiqué 
tree = [1, 2, [(3, 33, 'three', 'thirty-three')],
        ( [4, 44, ('forty', 'forty-four')])]
tree

# unpacking avec plusieurs variables *extended
*_,  ((_, *x3, _),), (*_, x4) = tree
print(f"x3={x3}, x4={x4}")

# -----
# For loops: sereval variables

item = (1, 2)
a, b = item
print(f"a={a} b={b}")

entrees = [(1, 2), (3, 4), (5, 6)]
for a, b in entrees:
    print(f"a={a} b={b}")

villes = ["Paris", "Nice", "Lyon"]
populations = [2*10**6, 4*10**5, 10**6]
list(zip(villes, populations))
for ville, population in zip(villes, populations):
    print(population, "habitants à", ville)

for i, j, k in zip(range(3), range(100, 103), range(200, 203)):
    print(f"i={i} j={j} k={k}")

# on n'itère que deux fois
# car le premier argument de zip est de taille 2
for units, tens in zip([1, 2], [10, 20, 30, 40]):
    print(units, tens)

for i, ville in enumerate(villes):
    print(i, ville)
for i in range(len(villes)):
    print(i, villes[i])
for i, ville in zip(range(len(villes)), villes):
    print(i, ville)

triple = (1, 2, 3,)
triple[0]
triple[:]
triple[len(triple)] # error
triple[0] = 0 # error

[ ( [ (1) ] ) ] == [ [ 1 ] ]
(1,) == (1)
[ (1,) ] [0][0] == 1
[ (1), ] [0][0] == 1

quadruple = (1, [2, 3], True, [ (4,) ] )
( one, (two, three), ignored, ( ( four ) ) ) = quadruple
four
( one, (two, three,), _, ( ( four, ), ) ) = quadruple
four
( (one,), (two, three), _, [ [ four ] ] ) = quadruple
four
( one, (two, three), _, [ [ four ] ] ) = quadruple
four

liste = [1,2]
tmp = liste[-1]; liste[-1] = liste [-2]; liste[-2] = tmp
liste
liste.reverse(-2, -1)
liste
liste[-2], liste[-1] = liste[-1], liste[-2]
liste

f = open('base_bateaux.txt', 'r', encoding='utf-8')
%timeit 'x' in range(100)

# -----
# Hashtables

%timeit 'x' in range(100)
%timeit 'x' in range(10_000)
%timeit 'x' in range(1_000_000)

t = [1, 2]
t[0]
t = [18, 35]
t['alice'] = 35

# -----
# Dictionary

age = {}
type(age)
age = {'ana':35, 'eve':30, 'bob':38}
age['ana']
a = [('ana', 35), ('eve', 30), ('bob', 38)]
age = dict(a)
age['bob']
age['bob'] = 45
age
del age['bob']
age
len(age)
'ana' in age
'bob' in age
age.keys()
age.values()
age.items()
k = age.keys()
k
age['bob'] = 25
k
'ana' in k
'bill' in k
for k, v in age.items():
    print(f"{k} {v}")
for k in age:
    print(k)



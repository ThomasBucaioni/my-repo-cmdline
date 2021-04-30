'spam'.upper()
note = 10
note
del(note)
note
true = 1
True
prénom = 'Arnaud'
prénom
var = 2
1
i = 1
type(i)
1+3
i = i+5
print(i)
i = 455555555555555555555555555555555555555555555555555555555
i * i
f = 4.2
c = 4 + 5j
c * c

i + f
1 << 16
2 | 16
2 & 16
2 & 3
(3.0 + 3.0) // 5
(3 + 3) / 5
(3.0 + 3) / 5
(3.0 + 3.0) / 5
(3.0 + 3) // 5
(3 + 3) // 5
3 + 2 * 1.j
3 + 2 * 1j
3 + 2j
3 + 2 * 1j
3 + 2 * 1.j
3 + 2.j

str?
dir(str)
help(str)

n = "sonia"
n
a = 30
f"{n} a {a} ans"
a = '""'
type(a)
a = "'"
type(a)
"\u03a6"
a
s = "un noël en été"
print(s)
en = s.encode('utf8')
en.decode()

# sequence
s[0]
len(s)
s[-1]
'no' in s
"te" not in s
t = s + ' chaud'
t
t.index('n')
t.count('n')
min(t)
max(t)
'x'*30  # # shallow-copy

# slicing
s = 'egg, bacon, '*2
s
s[0:3]
s[:3]
s[5:]
s[5:7]
s[:]  # shallow-copy: other string
s[0:10:2]
s[::3]
s[120]  # error
s[5:100]  # no errors
s[50:100]  # no error -> empty
s = "un noël en été"
s[-10:-7]
s[:-3]
s[::-1]
s[5::-1]
s[5:0:-1]
chaine = "douarnenez"
chaine.index('z') == len(chaine)
chaine.index('z') == len(chaine) - 1
chaine[1:3] + chaine[3:5] + chaine[5:] == chaine[1:]

# lists
a = [4, 'spam', 3.2, True]
a
a[0] + 10
a[1:3]
a[1:3] = [1, 2, 3]
a
del a[1:2]
a
a[1:3] = []
a
dir(list)
help(list.append)
a.append(2)
a
a.sort()
a
a.extend([1, 2, 3])
a
s = 'spam egg beams'
a = s.split()
a
a[0] = a[0].upper()
a
" ".join(a)
liste = [0, 1, 2, 3]
liste.insert(2, 4)
liste
liste[2:2] = [4]
suivant = liste[0]; del liste[0]
suivant
suivant = liste.pop(0)
suivant
liste.sort(reverse=True)
liste.sort(); liste.reverse()

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

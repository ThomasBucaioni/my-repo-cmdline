import re
def travel(r, zipcode):
    # your code
    print(f'{zipcode=}')
    #print(r[0:5])
    rl = list(r)
    #print(rl[0:5])
    l = r.split(',')
    #print(l[0])
    m = re.search(r'(.*)([A-Z]{2} [0-9]{5})', l[0])
    #print(f'{m.group(0)=}')
    #print(f'{m.group(1)=}')
    #print(f'{m.group(2)=}')
    dico = [('a',1), ('b',2), ('c',3), ('a', 4)]
    #print(dico)
    #print(dico[0])
    #print(dico[0][0], dico[0][1])
    dico = []
    for line in range(L:=len(l)):
        m = re.search(r'([0-9]+) (.*) ([A-Z]{2} [0-9]{5})', l[line])
        #print(f'{m.group(0)=}')
        #print(f'{m.group(1)=}')
        #print(f'{m.group(2)=}')
        #print(f'{m.group(3)=}')
        dico.append((m.group(3), m.group(2), m.group(1)))
    s = zipcode + ':'
    for item in dico:
        if item[0] == zipcode:
            #print(f'found one: {item}')
            #print(f'{item[0]}')
            #print(f'{item[1]}')
            s = s + item[1] + ','
    s = s + '/'
    for item in dico:
        if item[0] == zipcode:
            s = s + item[2] + ','
    print(f'{s=}')
    return s

#!/bin/python3

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i += 1

Phrase()

Phrase()

Phrase.nb_i

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i += 1
        
    def num():
        return Phrase.nb_i

Phrase()

Phrase()

Phrase.num()

Phrase.num

p = Phrase()
#p.num() # error

p.num

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i += 1

    @staticmethod
    def num():
        return Phrase.nb_i

p = Phrase()
Phrase.num()

p.num()

class PhraseSansCasse(Phrase):
    pass

p = Phrase()
Phrase.num()

PhraseSansCasse.num()

class PhraseSansCasse(Phrase):
    @staticmethod
    def num():
        return f"PhraseSansCasse {Phrase.nb_i}"

p = Phrase()

Phrase.num()

PhraseSansCasse.num()

class PhraseSansCasse(Phrase):
    nb_i = 0
    def __init__(self):
        PhraseSansCasse.nb_i += 1

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i += 1

    @classmethod
    def num(cls):
        return cls.nb_i

class PhraseSansCasse(Phrase):
    nb_i = 0
    def __init__(self):
        PhraseSansCasse.nb_i += 1

    @classmethod
    def num(cls):
        return f"PhraseSansCasse {Phrase.nb_i}"

p = Phrase()
Phrase()

p_no = PhraseSansCasse()
p.num()

Phrase.num()

Phrase.num

p.num

p_no.num()

PhraseSansCasse.num()

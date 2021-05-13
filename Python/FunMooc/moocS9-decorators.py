#!/bin/python3

class NbAppels:
    def __init__(self, f):
        self.appels = 0
        self.f = f
    def __call__(self, *t, **d):
        self.appels += 1
        s = f"Function {self.f.__name__} has been called {self.appels} time(s)"
        print(s)
        return self.f(*t, **d)

@NbAppels
def f(a, b):
    print(f'Arguments of f: {a}, {b}')


f(1, 2)

f(3, 'a')

@NbAppels
def g(a, b, c):
    print(f'Arguments of f: {a}, {b}, {c}')
    
g(1, 2, 3)

#

@NbAppels
def fibo_aux(n):
    "Fibonacci en log(n)"
    if n < 1:
        return 0, 1
    u, v = fibo_aux(n//2)
    u, v = u * (2 * v - u), u*u + v*v
    if n % 2 == 1:
        return v, u + v
    else:
        return u, v

def fibo_log(n):
    return fibo_aux(n)[0]

from math import log

n1 = 100

print(f'{log(n1)/log(2)=}')

print(f'{fibo_log(n1)=}')

n2 = 1600

print(f'{log(n2)/log(2)=}')

print(f'{fibo_log(n2)=}')

def memoize(a_decorer):
    """
    Un décorateur pour conserver les résultats
    précédents et éviter de les recalculer
    """
    def decoree(*args):
        # si on a déjà calculé le résultat
        # on le renvoie
        try:
            return decoree.cache[args]
        # si les arguments ne sont pas hashables,
        # par exemple s'ils contiennent une liste
        # on ne peut pas cacher et on reçoit TypeError
        except TypeError:
            return a_decorer(*args)
        # les arguments sont hashables mais on
        # n'a pas encore calculé cette valeur
        except KeyError:
            # on fait vraiment le calcul
            result = a_decorer(*args)
            # on le range dans le cache
            decoree.cache[args] = result
            # on le retourne
            return result
    # on initialise l'attribut 'cache'
    decoree.cache = {}
    return decoree

@memoize
def fibo_cache(n):
    """
    Un fibonacci hyper-lent (exponentiel) se transforme
    en temps linéaire une fois que les résultats sont cachés
    """
    return n if n <= 1 else fibo_cache(n-1) + fibo_cache(n-2)

fibo_cache(300)

print(f'{len(fibo_cache.cache)=}')

help(fibo_cache)

import functools                                 # +++

# un décorateur de fonction
# implémenté comme une fonction
def memoize(a_decorer):
    """
    Un décorateur pour conserver les résultats
    précédents et éviter de les recalculer
    """
    # on décore la fonction pour qu'elle ait les
    # propriétés de a_decorer : __doc__ et __name__
    @functools.wraps(a_decorer)                  # +++
    def decoree (*args):
        # si on a déjà calculé le résultat
        # on le renvoie
        try:
            return decoree.cache[args]
        # si les arguments ne sont pas hashables,
        # par exemple une liste, on ne peut pas cacher
        # et on reçoit TypeError
        except TypeError:
            return a_decorer(*args)
        # les arguments sont hashables mais on
        # n'a pas encore calculé cette valeur
        except KeyError:
            # on fait vraiment le calcul
            result = a_decorer(*args)
            # on le range dans le cache
            decoree.cache[args] = result
            # on le retourne
            return result
    # on initialise l'attribut 'cache'
    decoree.cache = {}
    return decoree

@memoize
def fibo_cache2(n):
    """
    Un fibonacci hyper-lent (exponentiel) se transforme
    en temps linéaire une fois que les résultats sont cachés
    """
    return n if n <= 1 else fibo_cache2(n-1) + fibo_cache2(n-2)

help(fibo_cache2)

import time

# comme pour memoize, on est limité ici et on ne peut pas
# supporter les appels à la **kwds, voir plus haut
# la discussion sur l'implémentation de memoize

# memoize_expire est une factory à décorateur
def memoize_expire(timeout):

    # memoize_expire va retourner un décorateur sans argument
    # c'est-à-dire un objet qui se comporte
    # comme notre tout premier `memoize`
    def memoize(a_decorer):
        # à partir d'ici on fait un peu comme dans
        # la première version de memoize
        def decoree(*args):
            try:
                # sauf que disons qu'on met dans le cache un tuple
                # (valeur, timestamp)
                valeur, timestamp = decoree.cache[args]
                # et là on peut accéder à timeout
                # parce que la liaison en Python est lexicale
                if (time.time()-timestamp) <= timeout:
                    return valeur
                else:
                    # on fait comme si on ne connaissait pas,
                    raise KeyError
            # si les arguments ne sont pas hashables,
            # par exemple une liste, on ne peut pas cacher
            # et on reçoit TypeError
            except TypeError:
                return a_decorer(*args)
            # les arguments sont hashables mais on
            # n'a pas encore calculé cette valeur
            except KeyError:
                result = a_decorer(*args)
                decoree.cache[args] = (result, time.time())
                return result

        decoree.cache = {}
        return decoree
    # le retour de memoize_expire, c'est memoize
    return memoize

@memoize_expire(0.5)
def fibo_cache_expire(n):
    return n if n<=1 else fibo_cache_expire(n-2)+fibo_cache_expire(n-1)

fibo_cache_expire(300)

print(f'{fibo_cache_expire.cache[(200,)]=}')


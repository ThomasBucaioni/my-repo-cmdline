# Katas

## 8 kyu

- `str.replace()`

## 7 kyu

- `del l[i:j:k]`
- `import copy`, `copy.copy(array)`, `copy.deepcopy(array)`, `arr[::2] + arr[1::2][::-1]`
- `i += 1`
- `s.translate(str.maketrans("1234567890", "9876043215"))`
- `sum(sorted(numbers)[-2:])`

## 6 kyu

- `print(i * '+')`
- `"({}{}{}) {}{}{}-{}{}{}{}".format(*n)`
- `def f(i,j):return(l:=len(i))*(l>j)`
- `[s.split(' ') for s in s_data.split(',')]`, `sum([float(x) for m,x in data]) / len(data)`
- `sorted({sub for sub in a1 if any(sub in s for s in a2)})`
- `s = sub(r'(.)(.*)\1', lambda x: chr((ord(x.group(1))-96)%26+97) + x.group(2),s)`
- `for order in filter(None, lst.split(', ')): if not re.match('\S+ \d+ \d*\.\d+ (B|S)', order):`
- `''.join( f'{"0"*(d.bit_length()-1)}1{d:b}' for d in map(int,s))`, `out.append( int(''.join(next(it) for _ in range(n)), 2) )`
- `is_prime = lambda n: n>1 and n%2 and all(n%d for d in range(3, int(n**.5) + 1, 2))`, `step = lambda g, m, n: next(([i, i+g] for i in [2] + range(m|1, n-g+1, 2) if is_prime(i) and is_prime(i + g)), None)`
- `sum(c // 2 for c in Counter(gloves).values())`

## 5 kyu

- `round_rgb = lambda rgb: min(255, max(rgb, 0))`, `hex_rgb = ("{:02X}" * 3).format(round_rgb(int_r), round_rgb(int_g), round_rgb(int_b))`
- `import itertools`, `import collections`:
- unknown dice numbers, itertools:
```
def rolldice_sum_prob(sum_, dice_amount):
    
    import itertools
    import collections   
    
    sums  = [sum(list(i)) for i in itertools.product([1,2,3,4,5,6], repeat=dice_amount)]
    count = collections.Counter(sums)
    prob  = count[sum_]*1.0/(len(sums))
    
    return prob
```
- unknown dice numbers, recursive:	
```
def s(x,n):
    if n==1:
        return 1 if 1<=x<=6 else 0
    else:
        return sum([s(x-i, n-1) for i in range(1,7)])
    
def rolldice_sum_prob(x, n):
    return 1.0*s(x,n)/6**n
```
- `from math import comb`, `pascal_diag = [comb(n+i, n) for i in range(l)]`
- `d = dict(l)`
- `sum(1 for x in a for y in b for z in c if x + y + z == s)`
- `printf "%d\n" "'$myChar"`

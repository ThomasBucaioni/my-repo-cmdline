# Bash tricks

## Strings

- `myString="${myString:1}"`
- `firstletter="${myString:0:1}"`
- `echo "Tongue tied and twisted just an earth bound misfit" | tr -d t`
- `echo "Tongue tied and twisted just an earth bound misfit" | tr 'a-d' '1-4'`
- `echo "Tongue tied and twisted just an earth bound misfit" | tr [:lower:] [:upper:]`
- `foo="bar" ; echo "${foo/a/}"`

### Characters

```
printf 'Please enter a character: '
IFS= read -r c
case $c in
  ([[:lower:]]) echo lowercase letter;;
  ([[:upper:]]) echo uppercase letter;;
  ([[:alpha:]]) echo neither lower nor uppercase letter;;
  ([[:digit:]]) echo decimal digit;;
  (?) echo any other single character;;
  ("") echo nothing;;
  (*) echo anything else;;
esac
```
- `printf "\x$(printf %x 65)"`, `awk 'BEGIN{printf "%c", 65}'`' `printf '%d\n' "'$A"`
- generate a password: `echo {A..Z} {a..z} {0..9} {0..9} '! @ # % ^ & * ( ) _ + = - [ ] { } " < > . / ?' | tr ' ' "\n" | shuf | xargs | tr -d ' ' | cut -b 1-18`

## bc

- `echo "ibase=16; ${hex^^}" | bc`

## for

```
for (( c=1 ; c<=5 ; c++ ))
do
  echo "c=$c"
done
```


## Lists

```
# Declare a string array
arrVar=("AC" "TV" "Mobile" "Fridge" "Oven" "Blender")

# Add new element at the end of the array
arrVar+=("Dish Washer")

# Iterate the loop to read and print each array element
for value in "${arrVar[@]}"
do
     echo $value
done
```

```
# Declare a string array
arrVar=("PHP" "MySQL" "Bash" "Oracle")

# Add new element at the end of the array
arrVar[${#arrVar[@]}]="Python"

# Iterate the loop to read and print each array element
for value in "${arrVar[@]}"
do
     echo $value
done
```

```
# Declare a string array
arrVar=("Banana" "Mango" "Watermelon" "Grape")

# Add new element at the end of the array
arrVar=(${arrVar[@]} "Jack Fruit")

# Iterate the loop to read and print each array element
for value in "${arrVar[@]}"
do
     echo $value
done
```

```
# Declare two string arrays
arrVar1=("John" "Watson" "Micheal" "Lisa")
arrVar2=("Ella" "Mila" "Abir" "Hossain")

# Add the second array at the end of the first array
arrVar=(${arrVar1[@]} ${arrVar2[@]})

# Iterate the loop to read and print each array element
for value in "${arrVar[@]}"
do
     echo $value
done
```

```

```

# Tricks

- `str.strip()`, `str.lstrip()`, `str.rstrip()`
- `re.subn(r'[aeiouAEIOU]','*',text)`
- `list({name.title() for name in names})`
- `sorted(names, key=lambda x: x.split()[-1], reverse=True)`
- `min(names, key=len)`

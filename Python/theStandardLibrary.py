import platform
# import os
import sys

print("Process id:", os.getpid())
print("Parent process id:", os.getppid())

print("Machine network name:", platform.node())
print("Python version:", platform.python_version())

print("Python module lookup path:", sys.path)
print("Command to run Python:", sys.argv)

print("PATH environment variable:", os.environ["PATH"])

import pathlib
path = pathlib.Path()
print(repr(path))

print(os.getcwd())  # os.chdir()


new_path = path / "folder" / "folder" / "example.py"
print(repr(new_path))

p = pathlib.Path("./Idioms")  # pathlib.Path.cwd()
txt_files = p.glob("*.txt")
print("*.txt:", list(txt_files))
# print("**/*.txt:", list(p.glob("**/*.txt")))
# print("*/*:", list(p.glob("*/*")))
# print("Files in */*:", [f for f in p.glob("*/*") if f.is_file()])

# import shutil # recursively copy, move or delete files

# Hidden files
# p = pathlib.Path.home()
# print(list(p.glob(".*")))

import datetime
datetime.date.today()

from dateutil import tz
d1 = datetime.datetime(1989, 4, 24, 10, 11, tzinfo=tz.gettz("Europe/Madrid"))
print(d1)
d2 = datetime.datetime(1989, 4, 24, hour=8, tzinfo=tz.gettz("America/Los_Angeles"))
print(d2)
print(d1>d2)
print(d1.hour>d2.hour)

d2_madrid = d2.astimezone(tz.gettz("Europe/Madrid"))
print(d2_madrid.hour)

d2_utc = d2.astimezone(datetime.timezone.utc)
print(d2_utc.hour)

import datetime as dt
d1 = dt.datetime(2019, 2, 25, 10, 50, tzinfo=dt.timezone.utc)
d2 = dt.datetime(2019, 2, 26, 11, 20, tzinfo=dt.timezone.utc)
td = d2-d1
print(td)
print(td.total_seconds())
print(d1.isoformat())

import time
time_now = time.time()
#sleep(2)
datetime_now = dt.datetime.now(dt.timezone.utc)
epoch = datetime_now - dt.timedelta(seconds=time_now)
print(time_now, '\t', datetime_now, '\t', epoch)

import calendar
c = calendar.Calendar()
print(list(c.itermonthdates(2019, 2)))
print(list( d for d in c.itermonthdates(2019, 2) if d.month == 2 ))

t_start = time.time()
l = [random.randint(1, 999) for _ in range(10 * 3)]
t_end = time.time()
print(f'Time elapsed: {t_end - t_start} sec = {(t_end - t_start)*10**9} ns')

t_start = time.time_ns()
l = [random.randint(1, 999) for _ in range(10 * 3)]
t_end = time.time_ns()
print(f'Time elapsed: {t_end - t_start} ns')

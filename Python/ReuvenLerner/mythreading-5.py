#!/bin/python3

import threading

# Count up, or count forever!
def count_to(n):
    if n < 4:
        for i in range(n):
            print(threading.current_thread().ident, n)

def count_forever():
    i = 0
    while True:
        if not i%100000:
            print(threading.current_thread().ident, i)
        i += 1


### Problem
print('Never ends...')
# # Start the threads
# for i in range(5):
#     threading.Thread(target=count_to, args=(i,)).start()
# threading.Thread(target=count_forever).start()

# # Joining
# for t in threading.enumerate():
#     if threading.current_thread() == t:
#         continue
#     print("Joining {}".format(t.ident))
#     t.join()

### Problem
print('Never ends...')
# # Start the threads
# for i in range(5):
#     threading.Thread(target=count_to, args=(i,)).start()
# threading.Thread(target=count_forever).start()

# # No joining!

### Error
print('Python error...')
# Start the threads
# for i in range(5):
#     threading.Thread(target=count_to, args=(i,)).start()
# threading.Thread(target=count_forever, daemon=True).start()

# # Joining
# for t in threading.enumerate():
#     if threading.current_thread() == t:
#         continue
#     print("Joining {}".format(t.ident))
#     t.join()

exit

### Ok
print('Ok')
for i in range(5):
    threading.Thread(target=count_to, args=(i,)).start()
# threading.Thread(target=count_forever).start()
threading.Thread(target=count_forever, daemon=True).start()

# Joining
for t in threading.enumerate():
    if threading.current_thread() == t:
        continue
    if t.daemon:
        continue
    print("Joining {}".format(t.ident))
    t.join()
print("All threads are done!")

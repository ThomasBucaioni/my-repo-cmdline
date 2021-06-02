import threading, time
print("Start of program.")
def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

threadObj2 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep':' & '})
threadObj2.start()  # collision
print('End of program.')

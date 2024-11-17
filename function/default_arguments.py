import time as t

def count(end, start=0):
    for i in range(start, end+1):
        print(i)
        t.sleep(1)
    print("done!")
    
count(10)
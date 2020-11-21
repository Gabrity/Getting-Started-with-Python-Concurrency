import threading

def do_some_work(var):
    print('doing some work in thread')
    print(var)

val = 'text'
t = threading.Thread(target = do_some_work, args = (val,))
t.start() # kick off the thread execution
t.join() # wait until the thread has finished execution
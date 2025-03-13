import time
from psutil import Process, Popen

def check_new_streamreader():
    # get the list of all running processes
    processes = Process.all_processes()

    # loop through each process and check if it is a streamreader process
    for p in processes:
        if "streamreader" in p.name():
            print("New streamreader process created")
            break

while True:
    # wait for 10 seconds before checking again
    time.sleep(10)
    check_new_streamreader()

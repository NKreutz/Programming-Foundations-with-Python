import webbrowser
import time

print("This program started at:" + time.ctime())
total_breaks = 3
break_count = 0
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=nfWlot6h_JM")
    break_count += 1


import os
import platform
import time
ostype = platform.system()
osversion = platform.release()
cpu = os.cpu_count()
print(f"Your using {ostype} {osversion} with {cpu} processers")
time.sleep(10)
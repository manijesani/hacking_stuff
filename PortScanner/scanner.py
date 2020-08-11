#Port Scanner Using Nmap
import nmap
import sys
nm = nmap.PortScanner()
print(f"Welcome to Nmap Version{nm.nmap_version()}")
ipadd = input("Enter ip Address --> ")
print(f"Scanning for {ipadd}")
op = int(input("Select Scan Type\n1.TCP Scan\n2.UDP Scan\n -->"))
try:
    if op ==1:
        nm.scan(ipadd,"1-1000","-v -sS")
        print(*[f">{key}:{value}" for key,value in nm.scaninfo()["tcp"].items()])
        print(">Ip State:",nm[ipadd].state())
        print(">Protocol:",*nm[ipadd].all_protocols())
        print(">Open Ports:",*list(nm[ipadd]["tcp"]))
    elif op==2:
        nm.scan(ipadd,"1-1000","-v -sU")
        print(*[f">{key}:{value}" for key,value in nm.scaninfo()["tcp"].items()])
        print(">Ip State:",nm[ipadd].state())
        print(">Protocol:",*nm[ipadd].all_protocols())
        print(">Open Ports:",*list(nm[ipadd]["udp"]))
    else:
        print("Wrong input")
except nmap.PortScannerError:
    print("Nmap Error",sys.exc_info()[0])
except Exception:
    print("Firewalls Are Enabled / Unknown Error Found")
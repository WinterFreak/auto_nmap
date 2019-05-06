import sys
import nmap
import time
import socket

print('\n[*]Running....------\n')
ip = socket.gethostbyname(sys.argv[1])
nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(ip, '80',  arguments='-O')

print(nm_scanner['scan'])
host_is_up = f"the host is {nm_scanner['scan'][ip]['status']['state']}" + "\n"
port_open = f"the port 80 {nm_scanner['scan'][ip]['tcp'][80]['state']}" + "\n"
reason = f"the scanning method is : {nm_scanner['scan'][ip]['tcp'][80]['reason']}" + "\n"
with open(f"{ip}.txt", 'w') as f:
    f.write("Info for " + sys.argv[1]+"\n")
    f.write(host_is_up + port_open + reason)
    try:
        guess_os = f"There is a {nm_scanner['scan'][ip]['osmatch'][0]['accuracy']}  percent that the host is running  {nm_scanner['scan'][ip]['osmatch'][0]['name']}" + "\n\n"
        f.write(guess_os + time.strftime("%Y:%m:%d_%H:M:S GMT", time.gmtime()))
    except IndexError as e:
       f.write("os not found \n "+ time.strftime("%Y:%m:%d_%H:M:S GMT", time.gmtime()))

print("\n[*]Finished.....-----")
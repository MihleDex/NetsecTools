#!/usr/bin/python3
import socket
import concurrent.futures
import time

class Scanner:
    target = ''
    range_start = 1
    range_end = 1024
    port_range = range(range_start,range_end)
    timeout = 1
    open_ports = []

    def __init__(self,target,range_start,range_end,timeout):
        self.target = target
        self.range_start = range_start
        self.range_end = range_end
        self.timeout = timeout
        self.port_range = range(self.range_start,self.range_end)

    def scan_port(self,port):    #scan ports
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates socket
        sock.settimeout(self.timeout)   #Sets timeout
        try: #tries connecting, returns port if successful
            c= sock.connect((self.target,port))
            return port
        except: #return None
            pass

    def scan(self):  #creates multiple threads, runs them
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.range_end/10) as executor:    
            results = executor.map(self.scan_port,self.port_range) #stores scan results in list results
            for result in results:
                if result !=None:#if result is None,skip
                    print(f"Port {result} is open.")
                    self.open_ports.append(result)  #appends open ports to open_ports list

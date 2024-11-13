import telnetlib
import time
import re

def get_cdp_neighbor_ips(host, user, password):
   
   
    tn = telnetlib.Telnet(host, timeout=1) 
   
    tn.read_until(b"Username: ", timeout=1)
    tn.write(user.encode('ascii') + b"\n")

    tn.read_until(b"Password: ", timeout=1)
    tn.write(password.encode('ascii') + b"\n")

   
    tn.write(b"sh cdp neighbors detail | include IP\n")


    time.sleep(1)  

    
    output = tn.read_very_eager().decode('ascii')

    print("Raw Output:\n", output)

   
    tn.write(b"exit\n")
    tn.close()


    ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    ip_addresses = ip_pattern.findall(output)

    return ip_addresses


if __name__ == "__main__":
    HOST = "1.1.1.1"  
    USER = "admin"         
    PASSWORD = "admin" 

    extracted_ips = get_cdp_neighbor_ips(HOST, USER, PASSWORD)
    print("Extracted IP Addresses:", extracted_ips)


import telnetlib
import re

def get_loopback_address(host, username="admin", password="admin", timeout=1):
   
    try:
    
        tn = telnetlib.Telnet(host, timeout=timeout)

        
        tn.read_until(b'Username: ', timeout=timeout)
        tn.write(username.encode('ascii') + b'\n')

      
        tn.read_until(b'Password: ', timeout=timeout)
        tn.write(password.encode('ascii') + b'\n')

     
        tn.write(b'show ip interface brief\n')
        tn.write(b'exit\n')

   
        output = tn.read_all().decode('ascii')

   
        tn.close()

      
        match = re.search(r'Loopback0\s+(\d+\.\d+\.\d+\.\d+)', output)
        if match:
            return match.group(1)  
        else:
            print("Loopback0 address not found.")
            return None

    except (EOFError, ConnectionRefusedError, OSError, TimeoutError) as e:
        print(f"Connection error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    HOST = "1.1.1.1"   
    extracted_ip = get_loopback_address(HOST)
    if extracted_ip:
        print("Loopback0 IP Address:", extracted_ip)
    else:
        print("Could not retrieve Loopback0 IP Address.")


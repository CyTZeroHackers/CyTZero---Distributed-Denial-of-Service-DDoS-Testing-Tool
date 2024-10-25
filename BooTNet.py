from colorama import init, Fore, Style
import time
import os
init()
def get_terminal_width():
    return os.get_terminal_size().columns
def center_text(text):
    terminal_width = get_terminal_width()
    centered_lines = []
    for line in text.splitlines():
        spaces = (terminal_width - len(line)) // 2
        centered_lines.append(" " * spaces + line)
    return "\n".join(centered_lines)
ascii_art = f"""{Fore.RED}
███████╗ ██████╗ ██████╗
██╔════╝██╔═████╗╚════██╗
███████╗██║██╔██║ █████╔╝
╚════██║████╔╝██║ ╚═══██╗
███████║╚██████╔╝██████╔╝
╚══════╝ ╚═════╝ ╚═════╝
{Style.RESET_ALL}"""
text_below = f"""{Fore.WHITE}Instrumentul de DDoS denumit *CyTZero* este în prezent în mentenanță programată și, din acest motiv, este indisponibil temporar. 
Ne cerem scuze pentru eventualele inconveniente și vă asigurăm că lucrăm pentru a îmbunătăți performanța și securitatea acestuia. 
Vă mulțumim pentru înțelegere și vă rugăm să reveniți ulterior pentru actualizări privind repornirea serviciului.{Style.RESET_ALL}"""
def show_ascii_art():
    print(center_text(ascii_art))
    print(center_text(text_below))
if __name__ == "__main__":
    show_ascii_art()
    print("\n")
    try:
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        print("\nProgramul a fost închis manual.")

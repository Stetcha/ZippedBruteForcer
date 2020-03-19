#!/usr/bin/python
from tqdm import tqdm
from zipfile import ZipFile
import sys

def extracting(zipped_file,wordlist,length):
	status_error = "Bad password for file"
	status_found = 'Not Found'
	print("\n[***] Trying",length,"possible Passwords...\n")
	for word in tqdm(wordlist, total=length, unit=" word"):
       
		try:
	
			zipped_file.extractall(pwd = word.strip())

			if not status_error in str(sys.exc_info()):
				
				status_found= 'Found'
				break
                
		except KeyboardInterrupt:
			
			print("\n[-] Exiting, Keyboard got Interrupted")
			exit()
			
		except :
			continue
				
	if status_found =="Not Found":        
		print("\n[-] Password not found") 
		exit()           
	print("\n\n[+] Password found:",str(word.decode()))


print('''
                       _____        ___ _ _     
                      |_  (_)_ __  | __(_) |___ 
                       / /| | '_ \ | _|| | / -_)
                      /___|_| .__/_|_| |_|_\___|
                            |_| |___|           
             _             _        __                    
            | |__ _ _ _  _| |_ ___ / _|___ _ _ __ ___ _ _ 
            | '_ \ '_| || |  _/ -_)  _/ _ \ '_/ _/ -_) '_|
            |_.__/_|  \_,_|\__\___|_| \___/_| \__\___|_|  
            
''')

try:
    zipped_file = ZipFile(input("[+] Zip File: "))
    wordlist = input("[+] File containing wordlist: ")
    length = len(list(open(wordlist,'rb')))
    wordlist = open(wordlist,'rb')
except FileNotFoundError:
    print("[-] File not found")
    exit()
except KeyboardInterrupt:
    print("\n[-] Exiting, Keyboard got Interrupted")
    exit()
except:
	exit("[-] Bad file")    
extracting(zipped_file,wordlist,length)


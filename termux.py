#autor Gilmar FIlho
#feito do dia 01/11/21
import os 

print ('''
  _                                 
 | |                                
 | |_ ___ _ __ _ __ ___  _   ___  __
 | __/ _ \ '__| '_ ` _ \| | | \ \/ /
 | ||  __/ |  | | | | | | |_| |>  < 
  \__\___|_|  |_| |_| |_|\__,_/_/\_\
                                    
''') 

do = input('''
		Choose any number ?
		1- tualizar repositorio
		2- instalar e python
		
		==> ''')


if do == '1':
  
  print ("autualizando repositorio do termux")
os.system ("apt-get update -y")
os.system ("apt-get upgrade -y")


if do == '2:
print ("instalando python  2 3 e autualinzando")
os.system ("pkg install python2 -y")
os.system ("pkg install python3 -y")


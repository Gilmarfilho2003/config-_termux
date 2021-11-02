 essa ferramenta foi criado por gilmar filho

#\033[1;92m	verde claro
import os

print ('''
Ferramenta desenvolvida por Gilmar Filho	
 __\033[1;34m	
|  |_ .-----..----..--------..--.--..--.--.\033[1;92m	#
|   _||  -__||   _||        ||  |  ||_   _|\033[1;91m		
|____||_____||__|  |__|__|__||_____||__.__|\033[1;92m	
\033[1;34m	
''')

do = input('''

    Por Favor escolhe uma opção ?
        1 - atualizar repositorio
        2 - instalar pip
        3 - instalar python
        4 - instalar o tor 
		📋> ''')
	
if do == '1':
  
  print ("autualizando repositorio do termux")
os.system ("apt-get update")
os.system ("apt-get upgrade")

if do == '2':
  
  print ("instalando pip  no termux")
os.system ("pip install")
os.system ("apt-get upgrade ")


if do == '3':
  
  print ("instalando python")

os.system("pkg insall python")
os.system("pkg insall python2")
os.system("pkg insall python3")

if do == '4' :

  print ("instalando o tor")

  os.system("pkg install tor")


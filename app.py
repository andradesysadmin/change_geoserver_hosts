import os 

#host novo
database_host = '192.168.10.200'

#hosts antigos
host_antigo1 = 'localhost'
host_antigo2 = '192.168.10.100'

for root, dirs, files in os.walk('workspaces/'):

        alterar_xml = False 
        pastas = root.split('/')
         
        #valida se ira alterar o xml ou não
        if pastas[len(pastas)-1] == pastas[len(pastas)-2]:
            alterar_xml = True

        for file in files:
            if file == 'datastore.xml' and alterar_xml:

                with open(f"{root}/{file}", 'r') as f:
                    datastore_string = f.read()

                datastore_string = datastore_string.replace(host_antigo1, database_host).replace(host_antigo2, database_host)
                #print(datastore_string)

                with open(f"{root}/{file}", 'w') as f:
                    f.write(datastore_string)
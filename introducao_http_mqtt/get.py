#> Thonny > Options > Package manager... > uresquest
#get

import urequests
import time

url = "http://10.31.2.83:5000/tasks"

response = urequests.get(url)

if response.status_code == 200:
    print("Tarefas recebidas com sucesso!")
    print (response.json())

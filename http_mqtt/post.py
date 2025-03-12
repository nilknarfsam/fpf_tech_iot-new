import urequests
import time
#import json

url = 'http://10.31.2.82:5000/tasks'

payload = {"done": False, "id": 31, "name": "Teste", "title": "Teste teste teste"}


response = urequests.post(url, json=payload)
 
if response.status_code == 200:
    print("Tarefas recebidas com sucesso!")
    print (response.json())

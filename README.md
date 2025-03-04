# FPF eTech 
Curso de IoT realizado pela FPF Etech entre os meses de fevereiro e março de 2025. Foram explorados os seguintes temas:
- História do IoT
- microPython
- Eletrônica básica
- Sistemas embarcados
- Protocolos de comunicação

## Como dar flash do MicroPython no ESP32
1. Baixe e instale o driver USB do ESP32 para garantir a conexão, [clique aqui](https://github.com/ayrtonaraujo/fpf_tech_iot/tree/main/drivers_esp32).
2. Faça o download do MicroPython para ESP32 (o arquivo .bin da última versão) [clicando aqui.](https://micropython.org/download/ESP32_GENERIC/)
3. Abra o CMD e digite:
```
pip install esptool
```
4. Conecte o ESP32 via USB e verifique a porta COM no Gerenciador de Dispositivos (se estiver no Windows)
5. Digite no CMD e execute o comando para limpar a memória do ESP32:
```
esptool --port {NOME_DA_PORTA (Exemplo: COM3} erase_flash
```
6. Pressione o botão **BOOT** do ESP32 por 5 segundos:
![Boot ESP32](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/boot-button-1.jpg?quality=100&strip=all&ssl=1)

7. Volte para o CMD e digite:
```
esptool --port {NOME_DA_PORTA (Exemplo: COM3} --baud 460800 write_flash 0x1000 {NOME DO ARQUIVO .bin do firmware MicroPython}.bin
```
8. Faça o download do **Thonny IDE** [clicando aqui](https://thonny.org/), e após a instalação, execute-o.
9. No Thonny vá em no menu **Tools** > **Options...**, abra a aba **Interpreter** selecione a opção _MicroPython (ESP32)_ em "**Which kind of interpreter(...)**" e em "**Port**", selecione a porta que o ESP32 está  conectada.
10. Se a conexão for bem sucedida, uma mensagem parecido com "MicroPython v1.24.1 on 2024-11-29; Generic ESP32 module with ESP32" vai aparecer no Shell do Thonny.
11. Para testar, digite o seguinte código e execute o programa (Tecla F5 ou botão de "play"):
```
#codigo para dar blink no led nativo do esp32

from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
while True:
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
```

12. Você pode salvar o programa criado na memória do ESP32 salvando o código como "main.py", em "Salvar como..." e escolhendo a opção no "MicroPython device" ou movendo o arquivo acessando a Aba **View** > **Files**
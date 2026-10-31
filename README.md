<p align="center">
 <img width="650" height="606" alt="image" src="https://github.com/user-attachments/assets/98549c8c-5c1f-4943-afb4-66ed5f256687" />
 /><br/>
Radar de Proximidade com Alerta Visual e Sonoro <br/>
</p>

<br/>

## :pushpin: Descrição

O projeto consiste em um sistema de radar e alerta de proximidade. O objetivo é medir a distância de objetos próximos ao dispositivo e alertar o usuário através de múltiplos estímulos: uma tela que mostra a distância exata em centímetros, um LED cujo brilho aumenta conforme o objeto se aproxima, e um buzzer que emite bipes sonoros mais rápidos e agudos à medida que a distância diminui.
<br/>

## :robot: Montagem do dispositivo físico


### Lista de materiais

| Quantidade | Nome | Link para referência |
| --- | --- | --- |
| 1 | ESP32 e cabo USB | https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html |
| 1 | Sensor Ultrassônico HC-SR04 | https://www.baudaeletronica.com.br/sensor-de-distancia-ultrassonico-hc-sr04.html |
| 1 | Display OLED SSD1306 128x64 (I2C) | https://www.baudaeletronica.com.br/display-oled-0-96-i2c-branco.html |
| 1 | Buzzer Ativo/Passivo | https://www.baudaeletronica.com.br/buzzer-ativo-5v.html |
| 1 | LED (ex: Vermelho) | https://www.amazon.com.br/Led-Difuso-Vermelho-5mm-Unidades/dp/B09V1LZQDK/ref=asc_df_B09V1LZQDK?mcid=a6b7dcfa642934039cc975175e6e355f&tag=googleshopp00-20&linkCode=df0&hvadid=709968341020&hvpos=&hvnetw=g&hvrand=13710345455053614801&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9197442&hvtargid=pla-2593150511912&psc=1&hvocijid=13710345455053614801-B09V1LZQDK-&hvexpln=0&language=pt_BR |
| 1 | Resistor (ex: 220Ω ou 330Ω) para o LED | https://www.amazon.com.br/Resistor-220R-4W-5-Kit-Unidades/dp/B09TWXJ8RV/ref=asc_df_B09TWXJ8RV?mcid=f81fa0f2148d38ac870879b561f1b39d&tag=googleshopp00-20&linkCode=df0&hvadid=715067048070&hvpos=&hvnetw=g&hvrand=7255216473740701999&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9197442&hvtargid=pla-2455549367687&psc=1&hvocijid=7255216473740701999-B09TWXJ8RV-&hvexpln=0&language=pt_BR |
| 13 | Jumpers variados (M-M e M-F) | https://www.amazon.com.br/Cabo-Jumper-Cada-Para-Arduino/dp/B0CZXRQZ5L/ref=asc_df_B0CZXRQZ5L?mcid=33cba154dcd63d19af8a59557fcd82ae&tag=googleshopp00-20&linkCode=df0&hvadid=709884378136&hvpos=&hvnetw=g&hvrand=7867927582475496027&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9197442&hvtargid=pla-2402025454035&psc=1&hvocijid=7867927582475496027-B0CZXRQZ5L-&hvexpln=0&language=pt_BR |
| 1 | Protoboard | https://www.eletrogate.com/protoboard-400-pontos?utm_source=Site&utm_medium=GoogleMerchant&utm_campaign=GoogleMerchant&gad_source=1&gad_campaignid=20223015315&gclid=CjwKCAjwo5bXBhAEEiwAkgpgXIUSqy7IXiqNgbkE5qPjL2ieiqObmucfrZiGTtwtJqqXvoTERNPCkBoC5OkQAvD_BwE |


### Lista de conexões
| Componente | Pino da placa (ESP32) |
| --- | --- |
| Display OLED - SCL | 22 |
| Display OLED - SDA | 23 |
| Buzzer | 14 |
| Sensor Ultrassônico - TRIG (Ativado) | 5 |
| Sensor Ultrassônico - ECHO | 35 |
| LED | 4 |


### Funcionamento dos sensores e atuadores

#### Sensor Ultrassônico HC-SR04
O HC-SR04 é um sensor de distância que utiliza ondas sonoras de alta frequência (ultrassom). Ele envia um pulso sonoro pelo pino *Trigger* e mede o tempo que o eco desse som leva para retornar através do pino *Echo*. Com base na velocidade do som no ar, o microcontrolador consegue calcular com precisão a distância do objeto à sua frente.

#### Display OLED SSD1306 (128x64)
É uma pequena tela gráfica. No projeto, ele é utilizado como um painel visual ("Radar") que exibe em tempo real o status ("Área Livre" ou "ALERTA!") e a medida da distância em centímetros.

#### Buzzer e LED (Atuadores via PWM)
- **Buzzer:** Componente que emite som. O código utiliza PWM (Modulação por Largura de Pulso) para alterar a frequência sonora, tornando o som mais agudo (e com bipes mais rápidos) à medida que o obstáculo fica mais próximo.
- **LED:** Diodo emissor de luz, que também é controlado por PWM. Uma função matemática (elevada ao cubo) adapta o nível de tensão (Duty cycle) para alterar o brilho do LED gradualmente de forma perceptível ao olho humano, brilhando mais forte quando algo se aproxima demais.

### Circuito

<p align="center">
<img width="650" height="606" alt="image" src="https://github.com/user-attachments/assets/ae82289a-b0d8-43ec-9a1c-2bafc4ef5e4f" />
  <br/>
Figura - Diagrama do circuito do Radar de Proximidade<br/>

</p>
O circuito deve ser montado garantindo que o HC-SR04 e o display OLED recebam a tensão correta. O LED deve com o resistor para evitar queimar a porta GPIO 4.

<br/>

## :electric_plug: Funcionamento do sistema

**Link do vídeo do sistema funcionando:** *https://drive.google.com/file/d/1fkl6XJE1yCCtbS78FTgV6ljgG9OPb4Wz/view?usp=sharing*

**Requisitos do código:**
- O microcontrolador deve estar rodando o firmware do **MicroPython**.
- É necessário ter as bibliotecas `hcsr04.py` e `ssd1306.py` salvas na memória interna do ESP32 para que o código principal funcione sem erros de importação.

**Estrutura de arquivos sugerida:**
- `main.py`: Contém a lógica principal do sistema.
- `hcsr04.py`: Driver para interpretar os dados do sensor ultrassônico.
- `ssd1306.py`: Driver de comunicação I2C para controlar a tela OLED.

**Lógica do Código:**
1. **Inicialização:** O código configura os pinos do I2C para o display, os pinos PWM para o LED e o Buzzer, e os pinos digitais para o sensor ultrassônico.

2. **Loop Principal (`while True`):**
   - A distância é lida continuamente pelo sensor em centímetros.
   - Os valores de distância são limitados (`clamp`) entre uma faixa mínima (8cm) e máxima (50cm) para calcular as proporções de alerta.
   - A função `mapear_brilho_perceptivel` traduz a distância em brilho do LED (distância menor = maior brilho).
   - O Display é atualizado mostrando o valor numérico e avisando se o limite foi extrapolado, se é um "ALERTA!" (distância < 10cm) ou "Área Livre".
   - A função `tocar_buzzer` calcula a velocidade de repetição e o tom do som dinamicamente, ligando e desligando o pino com `time.sleep_ms`.

<br/>

## :busts_in_silhouette: Contribuir no projeto

### Features implementadas

- [x] Leitura de distância em tempo real utilizando ultrassom.
- [x] Interface gráfica no Display exibindo a distância em cm.
- [x] Resposta visual dinâmica usando brilho adaptativo de LED.
- [x] Alerta sonoro responsivo que altera a frequência do som conforme a proximidade.

### Features para incrementar no projeto

- [ ] Adicionar um botão físico para "silenciar" temporariamente o alarme do buzzer.
- [ ] Conexão WiFi e envio de notificações para o celular quando um objeto for detectado a uma distância perigosa.

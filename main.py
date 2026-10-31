import machine
import time
from hcsr04 import HCSR04
import ssd1306

SCREEN_W = 128
SCREEN_H = 64
#Display Oled que estamo utilizando:
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(23),freq=40000)

display = ssd1306.SSD1306_I2C(SCREEN_W, SCREEN_H, i2c, addr = 0x3c)

buzzerPin = 14
delay = 150
duty = 216


pino_ativado = 5
pino_echo = 35

pino_led = 4 
led_pwm = machine.PWM(machine.Pin(pino_led))
led_pwm.freq(1000)

def mapear_brilho_perceptivel(distancia, dist_min, dist_max):
    if distancia < 0:
        return 0

    # Trava a distância nos limites
    dist_clamped = max(dist_min, min(dist_max, distancia))
    
    # Cria uma proporção linear de 0.0 (longe) a 1.0 (perto)
    proporcao = 1.0 - ((dist_clamped - dist_min) / (dist_max - dist_min))
    
    # Eleva a proporção ao cubo para corrigir a percepção do olho humano
    brilho = int((proporcao ** 3) * 1023)
    
    return brilho

def tocar_buzzer(distancia, dist_min, dist_max):

    if distancia < 0:
        buzzer.duty(0)
        return

    dist_clamped = max(dist_min, min(dist_max, distancia))
    
    proporcao = 1.0 - ((dist_clamped - dist_min) / (dist_max - dist_min))
    
    frequencia = int(250 + (proporcao * 2000))
    
    sleep = int(100 - (proporcao * 95))
    buzzer.duty(duty)
    buzzer.freq(frequencia)
    time.sleep_ms(sleep)
    buzzer.duty(0)
    time.sleep_ms(sleep)

buzzer = machine.PWM(machine.Pin(buzzerPin))
sensor = HCSR04(trigger_pin=pino_ativado, echo_pin=pino_echo, echo_timeout_us=10000)
buzzer.init(freq=1200, duty=0)


display.fill(0)
display.text("Iniciando sensor...", 0, 20)
display.show()

for i in range(1,4):
    display.fill(0)
    display.text("." * i, 0,20)
    display.show()
time.sleep_ms(20)

while True:
    distancia = sensor.measure_distance_cm()

    dist_min = 8  
    dist_max = 50 

    dist_clamped = max(dist_min, min(dist_max, distancia))
    
    brilho = mapear_brilho_perceptivel(distancia, dist_min, dist_max)
    led_pwm.duty(brilho)

    display.fill(0)
    display.text("RADAR", 0, 0)
    display.text("Distancia: ", 0, 20)
    
    
    if (distancia < 0):
        display.text("Fora do limite", 0, 35)

    elif(distancia < 10):
        display.text("{:.2f} cm".format(distancia), 0 ,35)
        display.text("ALERTA!", 0, 52)
    else:
        display.text("{:.2f} cm".format(distancia), 0 ,35)
        display.text("Area Livre", 0, 52)
    
    display.show()
    tocar_buzzer(distancia, dist_min, dist_max)

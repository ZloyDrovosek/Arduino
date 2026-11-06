import keyboard
import serial
import time

# !!! ВНИМАНИЕ: Замените 'COM3' на ТОТ номер порта, который был выбран в Arduino IDE
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

try:
    # Подключаемся к плате
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Ждем перезагрузку платы
    print("==================================================")
    print("Скрипт готов! Печатайте текст в ЛЮБОМ месте (в браузере, Discord, Блокноте).")
    print("Arduino будет моргать на каждый символ.")
    print("Для выхода закройте это окно командной строки.")
    print("==================================================")

    def on_key_press(event):
        # Реагируем только на буквы, цифры и пробел
        if len(event.name) == 1 or event.name == 'space':
            ser.write(b'x') # Отправляем байт-сигнал

    # Регистрируем функцию на нажатие клавиш
    keyboard.on_press(on_key_press)

    # Блокируем скрипт, чтобы он работал в фоне
    keyboard.wait()

except Exception as e:
    print(f"Ошибка: {e}")
    print("\nЧек-лист для исправления:")
    print("1. Вы закрыли 'Монитор порта' в Arduino IDE? (Он должен быть закрыт).")
    print(f"2. Плата точно подключена к порту {SERIAL_PORT}?")
    input("\nНажмите Enter для выхода...")



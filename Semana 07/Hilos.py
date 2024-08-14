import threading
import time

# Función que será ejecutada por cada hilo
def print_numbers(thread_name):
    for i in range(5):
        print(f'{thread_name}: {i}')
        time.sleep(1)  # Simula alguna tarea que toma tiempo

# Crear los hilos
thread1 = threading.Thread(target=print_numbers, args=('Hilo 1',))
thread2 = threading.Thread(target=print_numbers, args=('Hilo 2',))

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que los hilos terminen
thread1.join()
thread2.join()

print("Hilos terminados.")

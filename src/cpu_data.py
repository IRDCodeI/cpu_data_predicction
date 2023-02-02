import psutil
import pandas as pd
import threading
import os
import subprocess as sp

freq_cpus = psutil.cpu_freq(percpu=True) #? Frecuencia
process_cpu = psutil.pids() #? Procesos Activos
memory_ram_cpu = psutil.virtual_memory().percent #? Memoria ram
threads_cpu = threading.active_count() #? Hilos?
trans_data_cpu = psutil.disk_io_counters() #? I/O de informacion

aux = 0
for e in freq_cpus:
    aux = aux + float(str(e.current))

freq = aux/len(freq_cpus)

process = sp.Popen(['ps', '-eo' ,'nlwp'], stdout=sp.PIPE, stderr=sp.PIPE)
stdout, notused = process.communicate()

aux_nTh = 0
for line in stdout.splitlines():
    #print(type(int.from_bytes(line, "little")))
    aux_nTh = aux_nTh + int.from_bytes(line, "little")
    #pid, cmdline = line.split(' ', 1)

print("Frecuencia:", freq)
print("Cantidad de procesos:", process_cpu[-1])
print("Hilos Activos: ", aux_nTh)

print("Memoria ram:", (memory_ram_cpu*16)/100) #? Fix
print("Cantidad de lectura:", trans_data_cpu.read_count)
print("Cantidad de escritura:", trans_data_cpu.write_count)
print("Consumo de energia: ")

# p = sp.run(['lscpu'], capture_output=True, text=True)
# print(f'lscpu: {p.stdout}')
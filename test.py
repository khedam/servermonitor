import wmi
import os
class Server:
    Hersteller    = "test"
    Modelname     = "test"
    Systemname    = "test"
    Prozesse      = "test"
    Systemtyp     = "test"
    Systemfamilie = "test"




c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]

print(f"Hersteller: {my_system.Manufacturer}")
print(f"Modelname: {my_system. Model}")
print(f"Computername: {my_system.Name}")
print(f"AnzahlDerProzessoren: {my_system.NumberOfProcessors}")
print(f"SystemTyp: {my_system.SystemType}")
print(f"SystemFamilie: {my_system.SystemFamily}") 


def get_cpu_temp():
    
    
    result = 0.0
    
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        
        if line.isdigit():
            
            result = float(line) / 1000
    
    return result
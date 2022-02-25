import wmi
<<<<<<< HEAD
import os
class Server:
    Hersteller    = "test"
    Modelname     = "test"
    Systemname    = "test"
    Prozesse      = "test"
    Systemtyp     = "test"
    Systemfamilie = "test"
=======
 
class Server:
    Hersteller    = test
    Modelname     = test
    Systemname    = test
    Prozesse      = test
    Systemtyp     = test
    Systemfamilie = test
>>>>>>> 3b5f4f1d6d2a966242b69983c25a04f9f887c650




c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
<<<<<<< HEAD

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
=======
 
print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system. Model}")
print(f"Name: {my_system.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}")
>>>>>>> 3b5f4f1d6d2a966242b69983c25a04f9f887c650

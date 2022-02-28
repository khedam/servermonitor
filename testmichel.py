import shutil
import psutil

gesamt, benutzt, verfügbar = shutil.disk_usage("/")

print("Gesamt: %d GiB" % (gesamt // (2**30)))
print("Benutzt: %d GiB" % (benutzt // (2**30)))
print("Verfügbar: %d GiB" % (verfügbar // (2**30)))
print('RAM:', psutil.virtual_memory()[2])
print("CPU", psutil.cpu_percent(4))
import shutil

gesamt, benutzt, verfügbar = shutil.disk_usage("/")

print("Gesamt: %d GiB" % (gesamt // (2**30)))
print("Benutzt: %d GiB" % (benutzt // (2**30)))
print("Verfügbar: %d GiB" % (verfügbar // (2**30)))
import argparse, socket, time, json, datetime, platform, psutil, requests, pprint, uuid
from psutil import cpu_percent
import logging
import sys
# parse args
parser = argparse.ArgumentParser(description='')
parser.add_argument('-d', '--dest', default='http://localhost:8080/', help='')
parser.add_argument('-i', '--interval', default=5, type=int, help='Interval in dem geprüft wird (Sekunden)')
parser.add_argument('-a', '--attempts', default=30, type=int, help='')
parser.add_argument('-t', '--timeout', default=60, type=int, help='')
args = parser.parse_args()


if args.interval >= 2:
    args.interval -= 2
log = open("log.txt", 'a')


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


def oprint(message):
    print(message)
    global log
    log.write(message)
    return()
def main():
    
    # Hostname Info
    hostname = socket.gethostname()
    print("Hostname:", hostname)

    # CPU Info
    cpu_count = psutil.cpu_count()
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU:\n\tAnzahl Kerne:", cpu_count, "\n\tAuslastung:", cpu_usage)
     
       

    # Memory Info
    memory_stats = psutil.virtual_memory()
    memory_total = memory_stats.total
    memory_used = memory_stats.used
    memory_used_percent = memory_stats.percent
    print("Arbeitsspeicher:\n\tProzent:", memory_used_percent, "\n\tGesamt:", memory_total / 1e+6, "MB", "\n\tGenutzt:", memory_used / 1e+6, "MB")

    # Disk Info
    disk_info = psutil.disk_partitions()
    print("Disks:")
    disks = []
    for x in disk_info:
        # Listet mounted Geräte 
        try:
            disk = {
                "name" : x.device,
                "mount_point" : x.mountpoint,
                "type" : x.fstype,
                "total_size" : psutil.disk_usage(x.mountpoint).total,
                "used_size" : psutil.disk_usage(x.mountpoint).used,
                "percent_used" : psutil.disk_usage(x.mountpoint).percent
            }

            disks.append(disk)

            print("\tDisk name",disk["name"], "\tMount Point:", disk["mount_point"], "\tType",disk["type"], "\tSize:", disk["total_size"] / 1e+9,"\tUsage:", disk["used_size"] / 1e+9, "\tPercent Used:", disk["percent_used"])
        except:
            print("")

  
    # Netzwerk Info
    nics = []
    print("NetzwerkInfoss:")
    for name, snic_array in psutil.net_if_addrs().items():
        # Objekt für die Netzwerkinfos 
        nic = {
            "name": name,
            "mac": "",
            "address": "",
            "address6": "",
            "netmask": ""
        }
        # Netwerkinfos 
        for snic in snic_array:
            if snic.family == -1:
                nic["mac"] = snic.address
            elif snic.family == 2:
                nic["address"] = snic.address
                nic["netmask"] = snic.netmask
            elif snic.family == 23:
                nic["address6"] = snic.address
        nics.append(nic)
        print("\tNIC:",nic["name"], "\tMAC:", nic["mac"], "\tIPv4 Address:",nic["address"], "\tIPv4 Subnet:", nic["netmask"], "\tIPv6 Address:", nic["address6"])

    # Platform Info
    system = {
        "name" : platform.system(),
        "version" : platform.release()
    }
    print("OS - Betriebssystem:\n\t",system["name"],system["version"])

    # Zeit Info
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    uptime = int(time.time() - psutil.boot_time())
    print("System Uptime:\n\t",uptime)

    # System UUID 
    sys_uuid = uuid.getnode()

    # Objekt für rechnerinfos
    machine = {
    	"hostname" : hostname,
		"uuid" : sys_uuid,
        "system" : system,
        "uptime" : uptime,
    	"cpu_count" : cpu_count,
    	"cpu_usage" : cpu_usage,
    	"memory_total" : memory_total,
    	"memory_used" : memory_used,
    	"memory_used_percent" : memory_used_percent,
    	"drives" : disks,
        "timestamp" : timestamp
    }

    data = json.dumps(machine)
    print("\nData:")
    pprint.pprint(machine, indent=4)



""" Test Cases 
if cpu_percent >= 80:
        print("Warnung. CPU Auslastung ist über 80%", cpu_usage)

if psutil.disk_usage(x.mountpoint).percent >= : 90%)
        print("Festplatte ist über 90%")


"""


log.close()



while True:
    main()
    stdoutOrigin=sys.stdout 
    sys.stdout = open("log.txt", "w")
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    print("-----------------------------------------------------------------")
    time.sleep(args.interval)
    

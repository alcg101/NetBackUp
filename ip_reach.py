import sys
import subprocess

#Checking IP reachability
def ip_reach(list):

    for ip in list:
        ip = ip.rstrip("\n")

        #ping_reply = subprocess.call('ping %s -n 2' % (ip,), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #for windows
        ping_reply = subprocess.call(['ping', '-c', '2', '-w', '2', '-q', '-n', ip]) #for linux

        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue

        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()

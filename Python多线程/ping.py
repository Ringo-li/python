import threading,subprocess

def run(host):
    ret=subprocess.call('ping -n 3 -w 1 '+host,shell=True,stdout=subprocess.PIPE) # linux 系统将 '-n' 替换成 '-c'
    if ret:
        print("%s is down" % host)
    else:
        print("%s is up" % host)


if __name__ == "__main__":
    ip_list = ['192.168.31.'+str(x) for x in range(1,254)] #ping 192.168.31 网段
    ts = {}
    for i in range(1):
        for ip in ip_list:
            t = threading.Thread(target=run, args=(ip,))
            t.start()
            ts[i] = t

    for i in range(1):
        ts[i].join()
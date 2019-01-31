import math
import sys


def calculate_ipv6(ipv6address):
    ipv6net = ipv6address.split("/")
    if(len(ipv6net) == 2):
        diff = 64 - int(ipv6net[1])
        if(diff < 0):
            Numof64 = 0
        else:
            Numof64 = math.pow(2,diff)
        ipv6add = ipv6net[0].split(":")

        if(int(len(ipv6add)) <= 8):
            num = 0
            blank = 0
            addr = {}
            for l in ipv6add:
                if not l:
                    #print("array is blank")
                    a = l.zfill(4)
                    addr[num] = l.zfill(4)
                    blank = blank + 1
                    num = num + 1

                    nextarray = 8 - (len(ipv6add) - num)
                    for x in range(blank+1, nextarray):
                        #num = num + 1
                        addr[x] = "0".zfill(4)
                        num = num + 1
                    num = num - 1
                else:
                    a = l.zfill(4)
                    addr[num] = l.zfill(4)
                    num = num + 1
            if(blank > 1):
                print("only 1 blank")
            else:
                #print(addr[7])
                addrs = ""
                for l in range(len(addr)): 
                    addrs = addrs + addr[l]
                addrbin1 = ""
                binzero = ""
                binf = ""
                binprefix = ""
                
                for i in range(128 - int(ipv6net[1])):
                    binzero = binzero + "0"
                    binf = binf + "1"

                for a in addrs:
                    addrbin = bin(int(str(int(a,8))))[2:].zfill(4)
                    addrbin1 = str(addrbin1) + str(addrbin)
                
                binprefix = addrbin1[:int(ipv6net[1])]
                binstart = str(binprefix) + str(binzero)
                hexstart = hex(int(binstart,2))[2:]
                binstop = str(binprefix) + str(binf)
                hexstop = hex(int(binstop,2))[2:]
                    #print(a)
                #binprefix = addrs[0:int(ipv6net[1])]
                
                
                newaddr = [addrs[i: i+4] for i in range(0, len(addrs), 4)]
                newaddr = ":".join(newaddr)
                splitbin = [addrbin1[i: i+16] for i in range(0, len(addrbin1), 16)]
                splitbin = ":".join(splitbin)
                addrstart = ":".join([hexstart[i: i+4] for i in range (0, len(hexstart),4)])
                addrstop = ":".join([hexstop[i: i+4] for i in range (0, len(hexstop),4)])
                



        else:
            print("wrong input")

        ### OUTPUT
        print("IPv6 Address Entered: %s" % ipv6address)
        print("====== output =====")
        print("Full IPv6 Address = %s/%s " % (newaddr, ipv6net[1]))
        print("IPv6 Address Range - Start : %s" % addrstart)
        print("IPv6 Address Range - End : %s" % addrstop)
        print("Number of /64 Prefix: %s" % int(Numof64))
    else:
        print("IPv6 Format: x:x:x:x/yy")
        
    
        

if __name__ == "__main__":
    ipv6address = sys.argv[1]
    calculate_ipv6(ipv6address)

     
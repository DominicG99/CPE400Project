import math

flag = True
while flag:
    print("1.Route packets in network\n2.Display routing table\n3.Exit Program\nPlease select an option.")
    cmd = input()
    if cmd == '1':
        print("Enter a source address: ")
        srcAdd = input()
        print("Enter a destination address: ")
        dstAdd = input()
    elif cmd == '2':
        print("Do something else here")
    elif cmd == '3':
        flag = False

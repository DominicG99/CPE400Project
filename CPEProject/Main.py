import math
print("This program simulates Multilevel hierarchial routing with an example network.\nThis example network can be found inside the project folder.\n")
while True:
    print("Please select an option.\n1.Route packets in network\n2.Display routing table\n3.Exit Program")
    cmd = input()
    if cmd == '1':
        print("Enter a source address: ")
        srcAdd = input()
        print("Enter a destination address: ")
        dstAdd = input()
        break
    elif cmd == '2':
        print("Enter a router address: ")
        rtrAdd = input()
        break
    elif cmd == '3':
        break

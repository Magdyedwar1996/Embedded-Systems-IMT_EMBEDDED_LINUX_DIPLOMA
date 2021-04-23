file = open('init.c', 'w')
file.write("void Init_PORTA_DDRA(void)\n{")
i = 0
DDRA = ''
while i < 8:
    while 1:
        bit =input(f"enter the bit{i} mode  : ")
        bit = bit.lower()
        if bit == "input" or bit == "0":
            DDRA= "0" + DDRA
            break
        elif bit == "output" or bit == "1":
            DDRA= "1" + DDRA
            break
        else:
            print("wrong option \n")
    i+=1
DDRA = "0b" + DDRA
file.write("    DDRA = "+ DDRA + "\n}\n")
file.close()









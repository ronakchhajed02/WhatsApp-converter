fw = open(r"C:\Users\Ronak Chhajed\chats\WhatsappChats_new.csv", "a", encoding='UTF-8')
fw.seek(0)
fw.truncate()
fr = open(r"C:\Users\Ronak Chhajed\Downloads\WhatsApp Chat with Krishna 427.txt", "r", encoding='UTF-8')

while True:
    line = fr.readline()
    if line == "":
        break
    d=0
    if "joined using this group's invite link" in line:
        index = line.index("joined using this group's invite link")
        d=1
    line = list(line)

    if (len(line) >= 10) and (line[2] == "/") and (line[5] == "/") and (line[10] == ","):
        fw.write("\n")
        if d==1:
            line[index-2] = ":"
        p=0
        q=0
        j=0
        while (j+17 != len(line)):
            if (line[j+17] == "-") and (p == 0):
                line[j+17] = ","
                p=1
            if (line[j+17] == ":"):
                line[j+17] = ","
                q = 1
                k=0
                while (j+18+k != len(line)):
                    if line[j+18+k] == ",":
                        line[j+18+k] = "#"
                    k+=1
                break
            j+=1
        line = "".join(line)
        if q == 1:
            fw.write(line.replace('\n', ''))
    else:
        i=0
        while (i != len(line)):
            if line[i] == ",":
                line[i] = "#"
            i+=1
        line = "".join(line)
        fw.write(line.replace('\n', ''))
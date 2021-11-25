import time

content =list() # content in file
tags    =list() # Tags 
InFo    =list() # info of tag
types   =list() # type of tag
flag    =list() # Отмечает позицию тега, имеющего тип данных dict
lines =0
index =0
count =0
f =open("json_s.json", "r",encoding='UTF-8')
start_time = time.perf_counter()
# read file and count the number of lines
txt = f.readline()
while txt:
    content.append(txt)
    lines += 1
    txt = f.readline()
for a in content: # поиск построчно
    b= a.find("\"") # найти позицию "
    c= a.find("\"",b+1) # найти позицию "
    if a[b+1:c].isalnum():
        tags.append(a[b+1:c])
        # найти положение {
        temp=a.find("{")
        # если не найден
        if temp==-1:
            types.append("str")
            d= a.find("\"",c+1) # найти позицию "
            e= a.find("\"",d+1) # найти позицию "
            InFo.append(a[d+1:e])
        # если найден
        else: 
            types.append("dict")
            flag.append(len(types)-1)
            InFo.append("")
with open("xml_sNoLib.xml", "w",encoding='UTF-8') as m:
    m.write("<?xml version=\"1.0\" ?>\n<all>\n")
    for a in range(1,lines-1-len(flag)):
        if(types[a-1]=="dict"):
            if(index!=0 and index!=-1):
                m.write("\t\t</"+tags[flag[count+1]]+">\n\t\t<"+tags[a-1]+" type=\""+types[a-1]+"\">\n")
                count+=1
                index= a-1
            #index =-1 => write second tag dict
            elif index==-1:
                m.write("\t\t<"+tags[a-1]+" type=\""+types[a-1]+"\">\n")
                index= a-1 # index =1
            #index =0 => write first tag dict 
            else:
                m.write("\t<"+tags[a-1]+" type=\""+types[a-1]+"\">\n")
                index=-1 # index =-1 
        else: # type = str
            m.write("\t\t\t<"+tags[a-1]+" type=\""+types[a-1]+"\">"+InFo[a-1]+"</"+tags[a-1]+">\n")
    tempC=count #count изменится
    for ind in range (tempC,len(flag)):
        if(ind ==len(flag)-1):
            m.write("\t</"+tags[flag[0]]+">\n")
        else:
            m.write("\t\t</"+tags[flag[count+1]]+">\n")
        count+=1
    m.write("</all>")
m.close()
f.close()
print(time.perf_counter() - start_time)
import time
f =open("json_s.json", "r",encoding='UTF-8')
start_time = time.perf_counter()
txt = f.readline()
content =list()
tags    =list()
InFo    =list()
types   =list()
flag    =list()
lines =0
index =0
count =0
while txt:
    content.append(txt)
    lines += 1
    txt = f.readline()
for a in content:
    b= a.find("\"")
    c= a.find("\"",b+1) 
    if a[b+1:c].isalnum():
        tags.append(a[b+1:c])
        temp=a.find("{")
        if temp==-1:
            types.append("str")
            d= a.find("\"",c+1)
            e= a.find("\"",d+1)
            InFo.append(a[d+1:e])
        else:
            types.append("dict")
            flag.append(len(types)-1)
            InFo.append("")
with open("xml_sNoLib.xml", "w",encoding='UTF-8') as m:
    m.write("<?xml version=\"1.0\" ?>\n+<all>\n")
    for a in range(1,lines-1-len(flag)):
        if(types[a-1]=="dict"):
            if(index!=0 and index!=-1):
                m.write("\t\t</"+tags[flag[count+1]]+">\n\t\t<"+tags[a-1]+" type=\""+types[a-1]+"\">\n")
                count+=1
                index= a-1
            elif index==-1:
                m.write("\t\t<"+tags[a-1]+" type=\""+types[a-1]+"\">\n")
                index= a-1   
            else:
                m.write("\t<"+tags[a-1]+" type=\""+types[a-1]+"\">\n")
                index=-1
        else:
            m.write("\t\t\t<"+tags[a-1]+" type=\""+types[a-1]+"\"+>"+InFo[a-1]+"</"+tags[a-1]+">\n")
    tempC=count
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
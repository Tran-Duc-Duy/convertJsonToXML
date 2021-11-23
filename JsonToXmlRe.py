"""
Сначал я использую регулярное выражение для поиска заголовков dict, 
затем нахожу все заголовки, 
затем нахожу заголовков str и, 
наконец, нахожу информацию.
"""
import re
import time
f =open("json_s.json", "r",encoding='UTF-8')
start_time = time.perf_counter()
txt = f.read()

pattern = '\".+\"\:\s\{'
tagDict = re.findall(pattern,txt)
for i in range(len(tagDict)):
    tagDict[i]=tagDict[i][1:len(tagDict[i])-4]

#find str
pattern1 = '\".+\"\:\s[^{]'
tagStr = re.findall(pattern1,txt)
for i in range(len(tagStr)):
    tagStr[i] = tagStr[i][1:len(tagStr[i])-4]

#find info
pattern = '\:\s\".+\"'
tagInfo = re.findall(pattern,txt)
for i in range(len(tagInfo)):
    tagInfo[i] = tagInfo[i][3:len(tagInfo[i])-1] 

count =0 #Переменная, в которой хранится значение, определяет порядок информации.
curDich=1 #Переменная, в которой хранится значение, - это порядок пары.
with open("./bt/xml_s2.xml", "w",encoding='UTF-8') as m:
    m.write("<?xml version=\"1.0\" ?>\n<all>\n\t<"+tagDict[0]+" type=\"dict\">\n")
    """
    Поскольку есть только один день, заголовок первого словаря представляет день недели.
    """
    while (curDich < len(tagDict)):
        m.write("\t\t<"+tagDict[curDich]+" type=\"dict\">\n")
        while (count < len(tagStr)):
            if count >= curDich *len(tagStr)//2:
                break
            m.write("\t\t\t<"+tagStr[count]+" type=\"str\">"+tagInfo[count]+"</"+tagStr[count]+">\n")
            count+=1
        m.write("\t\t</"+tagDict[curDich]+">\n")
        curDich+=1
    m.write("\t</"+tagDict[0]+">\n</all>")
m.close()
f.close()
print(time.perf_counter() - start_time)
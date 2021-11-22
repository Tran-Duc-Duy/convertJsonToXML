"""
Сначал я использую регулярное выражение для поиска заголовков dict, 
затем нахожу все заголовки, 
затем нахожу заголовков str и, 
наконец, нахожу информацию.
"""
import re
f =open("json_s.json", "r",encoding='UTF-8')
txt = f.read()

pattern = '\".+\"\:\s\{'
tags = re.findall(pattern,txt)
tagDict =list() 
for tag in tags:
    tagDict.append(tag[1:len(tag)-4])

#find str
pattern1 = '\".+\"\:'
tags1 = re.findall(pattern1,txt)
tagStr =list()
for tag in tags1:
    tagStr.append(tag[1:len(tag)-2])

tagStr1= tagStr.copy()
for tag0 in tagDict:
    for tag in tagStr:
        if (tag == tag0):
            tagStr1.remove(tag)
#find info
pattern = '\:\s\".+\"'
tagInfoTemp = re.findall(pattern,txt)
tagInfo =list()
for tag in tagInfoTemp:
    tagInfo.append(tag[3:len(tag)-1])  

count =0 #Переменная, в которой хранится значение, определяет порядок информации.
curDich=1 #Переменная, в которой хранится значение, - это порядок пары.
with open("xml_sByRe.xml", "w",encoding='UTF-8') as m:
    m.write("<?xml version=\"1.0\" ?>\n")
    m.write("<all>\n")
    """
    Поскольку есть только один день, заголовок первого словаря представляет день недели.
    """
    m.write("\t<")
    m.write(tagDict[0])
    m.write(" type=\"dict\">\n")
    
    while (curDich < len(tagDict)):
        m.write("\t\t<")
        m.write(tagDict[curDich])
        m.write(" type=\"dict\">\n")
        while (count < len(tagStr1)):
            if count >= curDich *len(tagStr1)//2:
                break
            m.write("\t\t\t<")
            m.write(tagStr1[count])
            m.write(" type=\"str\">")
            
            m.write(tagInfo[count])

            m.write("</")
            m.write(tagStr1[count])
            m.write(">\n")
            count+=1
        m.write("\t\t</")
        m.write(tagDict[curDich])
        m.write(">\n")
        
        curDich+=1

    m.write("\t</")
    m.write(tagDict[0])
    m.write(">\n")

    m.write("</all>")
m.close()
f.close()
import pandas as pd
import csv
import json
import time
from os import write
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
f =open("json_s.json", "r",encoding='UTF-8')
start_time = time.perf_counter()
txt =f.read()
df = pd.read_json (r'D:\DuyStudy\\FILE_TinHocHocKy1\\TranDucDuy_Lab4_JsonToXML\\Json_s.json')
df.to_csv (r'D:\DuyStudy\\FILE_TinHocHocKy1\\TranDucDuy_Lab4_JsonToXML\\csv_s.csv', index = None)
data = readfromstring(txt)
result = json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml()
print(result)
m= open("xml_sByLib.xml", "w",encoding='UTF-8')
m.write(result)
m.close()
f.close()
print(time.perf_counter() - start_time)
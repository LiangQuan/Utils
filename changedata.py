# coding=UTF-8
import json
f = open("/Users/shang/lq/dumi/项目/idea/zhongqiu/data.txt")
line = f.readline()
list = []
index = 0
num = {'A':1,'B':2,'C':3,'a':1,'b':2,'c':3}
while line:
    dict = {'node_id': index, 'question': 'test', 'type': 'option','option':[],'answer':1}
    data = line.split('##')
    dict['node_id'] =  index
    dict['question'] =  data[0]
    dict['option'].append(data[1])
    dict['option'].append(data[2])
    dict['option'].append(data[3])
    dict['answer'] = num[data[4].replace("\n","")]
    list.append(dict)
    line = f.readline()
    index +=1
json = json.dumps(list)

r = open("/Users/shang/lq/dumi/项目/idea/zhongqiu/data.json",'w')
r.write(json)
f.close()

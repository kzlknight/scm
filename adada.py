import json

out1_datas = json.load(open('spider/out1.json', 'r'))
out2_datas = json.load(open('spider/out2.json', 'r'))
pdf_datas = json.load(open('spider/pdf1.json', 'r'))
in_datas = json.load(open('spider/inside1.json', 'r'))

for d in out2_datas:
    print(d)

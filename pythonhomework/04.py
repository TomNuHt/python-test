# !/usr/bin/python
#  --coding:utf8--

filePath = '/Users/haoqianpan/Desktop/hm/python/in/1998-05.txt'
file = open(filePath, mode='r')
specialChar = '，。：、“”《》（）『』〓[★；’！'
specialChar2 = '·．-'
sca = list(specialChar)
sca.append('－－－')
sca.append('……')
sca.append('———')
dateLength = len('19980502-01-009-009/m')
lineList = file.readlines()
d = {}
for i in lineList:
    arrayTemp = i.split()
    for j in arrayTemp:
        if len(j) == dateLength:
            continue
        wTemp = j.split('/')[0]
        if wTemp in sca:
            continue
        for k in specialChar:
            if k in j:
                j = j.replace(k, '')
        if ']' in j:
            j = j.split(']')[0]
        if '{' in j and '}' in j:
            j = j[0:j.index('{')] + j[j.index('}') + 1:len(j)]
        if j[0] == '/':
            continue
        aTemp = j.split('/')
        word = aTemp[0]
        wordType = aTemp[1]
        if word.isdigit():
            continue
        wTemp2 = word
        for k in specialChar2:
            wTemp2 = wTemp2.replace(k, '')
        if wTemp2.isdigit():
            continue
        if word in d:
            inDTemp = d.get(word)
            if wordType in inDTemp:
                inDTemp[wordType] += 1
            else:
                inDTemp[wordType] = 1
        else:
            inDTemp = {wordType: 1}
            d[word] = inDTemp
d2 = {}
# d3 = {}
for key in d:
    for key2 in d[key]:
        d2[key + '(/' + key2 + ')'] = d[key][key2]
        # if key2 in d3:
        #     d3[key2] = d3[key2] + d[key][key2]
        # else:
        #     d3[key2] = d[key][key2]
d2Order = sorted(d2.items(), key=lambda x: x[1], reverse=False)
# d3Order = sorted(d3.items(), key=lambda x: x[1], reverse=False)
print(d2Order)
# print(d3Order)





file.close()



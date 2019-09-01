import sys
import re
#0. Declaration
transitionDict = {}
transitionProbDict = {}
tagCountDict = {}
outgoingTagTotalCountDict = {}
wordList = []
emissionProbDict = {}
prevTag = 'Q0'
tagString = ''
# read trained file and make a sentace list
trainingTextFile = 'nepali_data_set.txt'
trainFileP = open(trainingTextFile,'r',encoding="utf-8")
for lines in trainFileP:
    wordList.append(lines.split())
trainFileP.close()
#end the reading file and make a sentace list
import sys
import re
for line in wordList:
    prevTag = 'Q0'
    tag = ''
    for words in line:
        tag = re.findall(r'\<.*?>', words)
        try:
            tag = tag[0]
        except:
            continue
        if tag in tagCountDict.keys():
            tagCountDict[tag] = tagCountDict[tag] + 1
        else:
            tagCountDict[tag] = 1
        if words in emissionProbDict.keys():
            emissionProbDict[words] = emissionProbDict[words] + line.count(words)
        else:
            emissionProbDict[words] = line.count(words)
        if tag == '' or prevTag == '':
            prevTag = tag
            continue
        tranTagSet = prevTag + '-' + tag
        if tranTagSet in transitionDict:
            transitionDict[tranTagSet] = transitionDict[tranTagSet] + 1
        else:
            transitionDict[tranTagSet] = 1
        # count outgoing tag total count
        if prevTag in outgoingTagTotalCountDict.keys():
            outgoingTagTotalCountDict[prevTag] = outgoingTagTotalCountDict[prevTag] + 1
        else:
            outgoingTagTotalCountDict[prevTag] = 1
        prevTag = tag

# transition probability tag WITH smoothing
for i in tagCountDict.keys():
    tagString = tagString + ',' + i
modelFileW = open('hmmmodel.txt','w+',encoding="utf-8")
#write no of states(tags)
modelFileW.write('No. of tags:' + str(len(tagCountDict)) + '\n')
modelFileW.write('Tags:' + tagString.strip(',') + '\n')
modelFileW.write('Outgoing Count:\n')
for i in outgoingTagTotalCountDict.keys():
    modelFileW.write(i+':' + str(outgoingTagTotalCountDict[i])+ '\n')
modelFileW.write('Transition Probability:\n')
for i in transitionDict.keys():
    print(i)
    outTag = i.split('-')[0]
    outTag1 = i.split('-')[1]
    if outgoingTagTotalCountDict[outTag] > 0:
        transitionProbDict[i] = (transitionDict[i] + 1) / (outgoingTagTotalCountDict[outTag] + len(tagCountDict))

        if outTag == 'Q0':
           # ws = 'Begin-' +outTag1+ ':' + str('{:.8f}'.format(transitionProbDict[i])) + '\n'
            t1 = "%f13"%(transitionProbDict[i])
            ws = 'Begin-' + outTag1 + ':' + t1 + '\n'
        else:
            t2 = "%f13" % (transitionProbDict[i])
            #ws = i + ':' + str('{:.8f}'.format(transitionProbDict[i])) + '\n'
            ws = i + ':' + t2 + '\n'
        modelFileW.write(ws)
        ws = ''

l = len(transitionDict)

# Emission Probablity
modelFileW.write('\n\n\nEmission Probability:\n')
for i in emissionProbDict.keys():
    Tag = re.findall(r'\<.*?>', i)
    print(emissionProbDict)

    try:
        Tag = Tag[0]
        print(Tag)
    except:
        continue
    if tagCountDict[Tag] > 0:
        emissionProbDict[i] = emissionProbDict[i] / tagCountDict[Tag]
        t3 = "%f13" % (emissionProbDict[i])
        ws = 'P('+i[0:len(i)-4].replace('<','').replace('V','')+'|'+Tag+'):->' + t3 + '\n'
        modelFileW.write(ws)
#print (l)
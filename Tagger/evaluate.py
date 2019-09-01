from collections import Counter


ipn='testoutput.txt'
f1=  open(ipn,'r',encoding='utf-8')
ipn1='testpos.txt'
f3= open(ipn1,'r',encoding='utf-8')
f2= f1.read().split()
f4= f3.read().split()
total_words_tagged=0
for word in f2:
    #print(word)
    total_words_tagged+=1

correctly_tagged_words=0
for i,j in zip(f2,f4):
    if i==j:
        correctly_tagged_words+=1
        #print(i,j)
        #print(i,j)
    else:
        #print("wrong tags:",i,j)
        pass

print ("Correctly tagged words:",correctly_tagged_words)
print("Total tagged words:",total_words_tagged)
precision = "%.2f" %((correctly_tagged_words/total_words_tagged)*100)
print("Precision:",precision)




    #print(i,j)












    #words1=f1.read().split()
    #words2=f2.read().split()



   # words=set(words1) & set(words2)



from django.shortcuts import render,redirect
import os
from tagger.forms import ParagraphForm
from .hmmdecode2 import Np
import re

def home (request):
    return render(request, 'index.html')

def paragraph(request):
    if request.method == 'GET':
        context = {
            'form': ParagraphForm(),
            'form1': ParagraphForm(),
        }
        return render(request, 'index.html', context)
    else:
        text = request.POST.get('testSentence')
        text = re.sub(r"[a-zA-z]+",'', text)
        try:
            module_dir = os.path.dirname(__file__)
            file_path = os.path.join(module_dir, 'writefile.txt')
            file1 = open(file_path,"w",encoding='utf-8')
            file1.write(text)
            file1.close()
            out_file_path = os.path.join(module_dir,'hmmoutput.txt')
            nepali_dict = {'<NN>': 'नाम','<NNP>': 'नाम','<PP>': 'सर्बनाम','<NP>':'नाम', '<PP$>':'सर्बनाम', '<PPR>': 'सर्बनाम', '<DM>': 'सर्बनाम', '<DUM>': 'सर्बनाम','<VBX>': 'क्रियापद','<VBF>': 'क्रियापद' ,'<VBI>': 'क्रियापद','<VBNE>': 'क्रियापद','<VBKO>': 'क्रियापद',
                            '<VBO>': 'क्रियापद',
                            '<JJ>': 'विशेषण',
                            '<JJM>': 'विशेषण',
                            '<JJD>': 'विशेषण',
                            '<RBM>': 'क्रियाविशेषण',
                            '<RBO>': 'क्रियाविशेषण',
                            '<PLE>': 'विभक्ति',
                            '<PLAI>': 'विभक्ति',
                            '<PKO>': 'विभक्ति',
                            '<POP>': 'विभक्ति',
                            '<CC>': 'सम्योजक',
                            '<CS>': 'सम्योजक',
                            '<UH>': 'विस्मयबोधक',
                            '<CD>': 'अंक',
                            '<OD>': 'अंक',
                            '<HRU>': 'बहुवचन संकेत',
                            '<QW>': 'प्रश्नवाचक सर्बनाम',
                            '<CL>': 'संख्याबोधक विशेषण',
                            '<RP>': 'अब्यय',
                            '<DT>': 'निश्चयवाचक सर्बनाम',
                            '<UNW>': 'अज्ञात शब्द',
                            '<FW>': 'आगन्तुक शब्द',
                            '<YF>': 'चिन्ह',
                            '<YM>': 'चिन्ह',
                            '<YQ>': 'चिन्ह',
                            '<YB>': 'चिन्ह',
                            '<FB>': 'संक्षेप',
                            '<ALPH>': 'सुचि संकेत',
                            '<SYM>': 'संकेत चिन्ह',
                            }
            print(nepali_dict)
            a =  Np()
            all_postag = []
            with open(out_file_path, 'r',encoding='utf-8') as f:
                for line in f:
                    for x,y in nepali_dict.items():
                        line = re.sub(x,y,line)
                    all_postag.append(line)
            p = str(all_postag)
            line = re.sub('/', '=', p)
            file1.close()
            return render(request, 'index.html', {'postag': line[2:-4]})
        except IndexError:
            errtxt = 'Please enter the input correctly'
            return render(request, 'index.html', {'postag': errtxt})
#Self-created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def remove_punc(request):
    #Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('remove_punc','off')
    fullcaps = request.POST.get('fullcaps','off')
    e_space = request.POST.get('e_space','off')
    l_remove = request.POST.get('l_remove','off')
    lower_case=request.POST.get('lower_case','off')
    title_case=request.POST.get('title_case','off')
    camel_case=request.POST.get('camel_case','off')
    c_count = request.POST.get('c_count','off')
    swap_case = request.POST.get('swap_case','off')
    is_alnum=request.POST.get('is_alnum','off')
    is_alpha=request.POST.get('is_alpha','off')
    is_digit=request.POST.get('is_digit','off')
    is_identifier=request.POST.get('is_identifier','off')
    is_space=request.POST.get('is_space','off')
    split_line = request.POST.get('split_line','off')
    
    fcount=0
    analyzed = ""
    purp=[]
    steps=[]
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    if (fullcaps =='on'):
        fcount +=1
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to upper case', 'analyzed_text':analyzed}

        step = f"After UPPER CASE : {analyzed}"
        steps.append(step)

        djtext = analyzed
        purp.append(params['purpose'])

    if (lower_case =='on'):
        fcount +=1
        analyzed=djtext.lower()
        params = {'purpose':'Change to lower case', 'analyzed_text':analyzed}

        step = f"After lower case : {analyzed}"
        steps.append(step)

        djtext = analyzed
        purp.append(params['purpose'])
    
    if (title_case =='on'):
        fcount +=1
        analyzed=djtext.title()
        params = {'purpose':'Change to title case', 'analyzed_text':analyzed}

        step = f"After Title Case : {analyzed}"
        steps.append(step)

        djtext = analyzed
        purp.append(params['purpose'])

    if (camel_case =='on'):
        fcount +=1
        analyzed=""
        djtext = djtext.title()
        for char in djtext:
            if char !=" ":
                analyzed+= char
        params = {'purpose':'Change to camel case', 'analyzed_text':analyzed}

        step = f"After Camel Case : {analyzed}"
        steps.append(step)

        djtext = analyzed
        purp.append(params['purpose'])
    
    if (swap_case =='on'):
        fcount +=1
        analyzed = djtext.swapcase()
        params = {'purpose':'Change to Swap case', 'analyzed_text':analyzed}

        step = f"After Swapping Cases : {analyzed}"
        steps.append(step)

        djtext = analyzed
        purp.append(params['purpose'])

    if (is_alnum =='on'):
        fcount +=1
        x = djtext.isalnum()
        analyzed=f"Is Al-num? : {x}"
        
        step = analyzed
        steps.append(step)

        params = {'purpose':'Is Al-num?', 'analyzed_text':analyzed}
        purp.append(params['purpose'])

    if (is_alpha =='on'):
        fcount +=1
        x = djtext.isalpha()
        analyzed = f"Is Alpha : {x}"
        #analyzed = f"{analyzed}\n\n{analyzed1}"

        step = analyzed
        steps.append(step)

        params = {'purpose':'Is Alpha?', 'analyzed_text':analyzed}
        purp.append(params['purpose'])

    if (is_digit =='on'):
        fcount +=1
        x = djtext.isdigit()
        analyzed = f"Is Digit? : {x}"
        
        step = analyzed
        steps.append(step)

        params = {'purpose':'Is Digit?', 'analyzed_text':analyzed}
        purp.append(params['purpose'])

    if (is_identifier =='on'):
        fcount +=1
        x = djtext.isidentifier()
        analyzed =f"Is Identifier ? : {x}"
        
        step = analyzed
        steps.append(step)

        params = {'purpose':'Is Identifier?', 'analyzed_text':analyzed}
        purp.append(params['purpose'])
    
    if (is_space =='on'):
        fcount +=1
        count=0
        for i in djtext:
            if i == ' ':
                count += 1
        if count>0:    
            analyzed=f"Is Space : Yes and total spaces = {count}"
        else:
            analyzed=f"Is Space : No"
        
        step = analyzed
        steps.append(step)

        params = {'purpose':'Is Space?', 'analyzed_text':analyzed}
        purp.append(params['purpose'])

    if removepunc=="on":
        analyzed = ""
        fcount +=1
        for char in djtext:
            if char ==" ":
                analyzed += char
            elif char not in punctuation:
                analyzed += char
        params = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed}

        step = f"After removing Punctuation : {analyzed}"
        steps.append(step)

        djtext = analyzed
        purp.append(params['purpose'])
      
    if (e_space =='on'):
        fcount +=1
        analyzed=""
        i=0
        analyzed += djtext[0]
        for i in range(1,len(djtext)):
            if ((djtext[i]==djtext[i-1]) and (djtext[i-1]==" ")):
                pass
            else:
                analyzed += djtext[i]
        params = {'purpose':"Removing Extra Spaces", 'analyzed_text':analyzed}

        step = f"After Removing Extra Spaces : {analyzed}"
        steps.append(step)

        purp.append(params['purpose'])
        djtext = analyzed
    
    if (l_remove =='on'):
        fcount +=1
        analyzed=""
        for char in djtext:
            if char=='\n' or char=='\r':
                analyzed = analyzed + " "
            else:
                 analyzed = analyzed + char
        params = {'purpose':'Line Remove', 'analyzed_text':analyzed}

        step = f"After Removing Lines : {analyzed}"
        steps.append(step)

        djtext = analyzed
        purp.append(params['purpose'])
        
    if (c_count =='on'):
        fcount +=1
        count = 0
        for char in djtext:
            if char !=' ' or char !='\n':
                count += 1
        analyzed = f"Total Characters : {count}"
        
        step = analyzed
        steps.append(step)

        params = {'purpose':'Character count', 'analyzed_text':analyzed}
        purp.append(params['purpose'])

    if (split_line =='on'):
        fcount +=1
        x = djtext.splitlines(True)
        analyzed = f"Splitted Lines : {x}"
    
        params = {'purpose':'Split Line', 'analyzed_text':x}

        step = analyzed
        steps.append(step)

        purp.append(params['purpose'])
        
    if fcount==0:
        return render(request,'error.html')

    step='\n'.join(steps)
    params['steps']=step

    purp = " , ".join(purp)    
    params['purpose']=purp

    return render(request,'analyze.html',params)

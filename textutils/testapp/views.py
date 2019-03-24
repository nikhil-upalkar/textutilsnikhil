from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def results(request):
    text=request.POST.get("textarea",'default')
    print(text,"***")
    removepuncs=request.POST.get('removepuncs','off')
    fullcaps=request.POST.get('fullcaps','default')
    nlremove= request.POST.get('nlremove','default')
    espace=request.POST.get('espaceremove','default')
    charcount=request.POST.get('charcount','off')
    puncs="""!()-[]{};:'"\,<>./?@#$%^&*_~"""
    if text !='':
        if removepuncs=='on':
            final_text=''
            for x in text:
                if x not in puncs:
                    final_text+=x
            text=final_text
            
        if fullcaps == 'on':
            final_text=''
            final_text=text.upper()
            text=final_text
        # if nlremove=='on':
        #     final_text=''
        #     for x in text:
        #         if x != '\n'and x!='\r':
        #             final_text+=x
        #     text=final_text
        if espace=='on':
            final_text=''
            for i,x in enumerate(text):
                if x==text[-1]:
                    if not (text[i]==" "):
                        final_text+=x
                elif not(text[i]==" " and text[i+1]==" "):
                    final_text=final_text + x
            text=final_text
        if nlremove=='on':
            final_text=''
            for x in text:
                if x != '\n'and x!='\r':
                    final_text+=x
            text=final_text
        if (removepuncs!='on'and fullcaps!='on' and nlremove!='on' and espace!='on'):
            text="please select any operation and try again"
        
        
        # if charcount=='on':
        #     final_text=len(text)
    else:
        text="Enter the Text"
        print(text)
      # final_text=text.upper()
    params={'value':text}
    return render(request,'testapp/results.html',params)
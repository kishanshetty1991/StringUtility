# This is made by Kishan
from django.http import HttpResponse
from django.shortcuts import render
import re
#Code for video 6
# def index(request):
#   ##If file is in the project directory
#   # with open('mysite/one.txt','r') as f:
#   #   x = f.read()
#   # return HttpResponse(x)

#   ##If file is in the project directory
#   # with open('one.txt','r') as f:
#   #   x = f.read()
#   # return HttpResponse(x)

#   ##Personal navigator
#   return HttpResponse('''
#       <a target="_blank" href = "https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU">Team Blind</a>
#       <a target="_blank" href = "https://www.amazon.com">Amazon</a>
#       <a target="_blank" href = "https://www.flipkart.com">Flipkart</a><br><br>
#       <a target="_blank" href = "https://www.google.com">Google</a>
#       <a target="_blank" href = "https://www.youtube.com">Youtube</a>
#       ''')


# def about(request):
#   return HttpResponse("This is about us page")

#Code for video 7
# def index(request):
#   return HttpResponse('''Home <button> <a href="/">Back</a></button> ''')

# def removepunc(request):
#   return HttpResponse('''Remove Punc <button> <a href="/">Back</a></button> ''')
    
# def capitalizefirst(request):
#   return HttpResponse('''Capitalize First <button> <a href="/">Back</a></button> ''')

# def newlineremove(request):
#   return HttpResponse('''New Line Remove <button> <a href="/">Back</a></button> ''')

# def spaceremove(request):
#   return HttpResponse('''Space Remove <button> <a href="/">Back</a></button> ''')

# def charcount(request):
#   return HttpResponse('''Character count <button> <a href="/">Back</a></button>''')   

##Code for video 8
# def index(request):
#   params = {'name': 'Kishan', 'place': 'India'}
#   return render(request,'index.html',params)

##Code for video 9 and 10
def index(request):
    return render(request,'index.html')
def analyze_text(request):
    word = request.POST.get('txt1','default')
    c1 = request.POST.get('c1','off')
    c2 = request.POST.get('c2','null')
    c3 = request.POST.get('c3','null')
    c4 = request.POST.get('c4','null')
    c5 = request.POST.get('c5','null')
    neword = word
    c = 0
    if c1 != 'off':
        # To remove Punctuations
        neword = re.sub(r'[^\w\s]',"",neword)

    if c2 != 'null':
        #Makes first word capital all other small
        neword = neword.capitalize()

    if c3 != 'null':
        # To remove new line (To remove line you need to also remove \r along with \n)
        n = list(neword)
        if '\n' in n:
            n.remove('\n')
            n.remove('\r')
            neword = "".join(n)
        else:
            pass

    if c4 != 'null':
        # To remove Whitespaces
        neword = neword.replace(" ","") 
    if c5 != 'null':
        # To count only character not \n or \s because these get counted so replacing whitespaces first
        x = neword.replace(" ", "")
        c = len(x)
    if c5 == 'null':
        # If char count not selected then 
        c = '''Please Choose Char Count to get Character Count'''
    if neword == "default":
        return HttpResponse("Error Please Enter a Word")    
    if c1 == "null" and c2 == "null" and c3 == "null" and c4 == "null" and c5 == "null":
        return HttpResponse(f"Error Please check something for the {neword}")    
    params = {'neword': neword,'c': c}
    return render(request,'analyze.html',params)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    
def links(request):
    return render(request,'links.html')   
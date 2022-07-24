from django.shortcuts import render

# Create your views here.
def home(req):
    if(req.method == "POST"):
        print(req.POST.get('username'))
        username = req.POST.get('username')
        return render(req,'result.html',{'username':username})
    elif(req.method == "GET"):
        return render(req,'home.html')
    

def result(req):
    return render(req,"result.html")
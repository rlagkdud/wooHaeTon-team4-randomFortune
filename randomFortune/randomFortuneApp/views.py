from random import random
from django.shortcuts import render
import random

# Create your views here.
def getItem():
    itemList = ["모자", "립밤", "팔찌", "손거울", "손수건", "에어팟", "핸드폰", "집게핀", "시계", "셔츠", "가방", "백팩"]
    luckyItem = random.choice(itemList)
    return luckyItem


def home(req):
    if(req.method == "POST"):
        username = req.POST.get('username')
        luckyItem = getItem()  
        return render(req,'result.html',{'username':username,'luckyItem':luckyItem})
    elif(req.method == "GET"):
        return render(req,'home.html')

def result(req):  
    return render(req,"result.html")
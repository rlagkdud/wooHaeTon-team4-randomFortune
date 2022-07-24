from random import random
from django.shortcuts import render
import random

# Create your views here.
def getItem():
    itemList = ["모자", "립밤", "팔찌", "손거울", "손수건", "에어팟", "핸드폰", "집게핀", "시계", "셔츠", "가방", "백팩"]
    luckyItem = random.choice(itemList)
    return luckyItem

def getPlace():
    placeList = ["노래방", "PC방", "식당", "카페", "주유소", "학교", "영화관", "친구집", "공원", "콘서트", "헬스장", "공항", "볼링장", "당구장", "도서관", "경찰서", "문구점", "병원"]
    luckyPlace = random.choice(placeList)
    return luckyPlace

def getNumber():
    numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    luckyNumber = random.choice(numberList)
    return luckyNumber

def getColor():
    luckyColor = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    return luckyColor



def home(req):
    if(req.method == "POST"):
        username = req.POST.get('username')
        luckyItem = getItem()
        luckyPlace = getPlace()
        luckyColor = getColor()
        luckyNumber = getNumber()
        return render(req,'result.html',{'username':username,'luckyItem':luckyItem, 'luckyPlace':luckyPlace, 'luckyColor':luckyColor, 'luckyNumber':luckyNumber})
    elif(req.method == "GET"):
        return render(req,'home.html')

def result(req):  
    return render(req,"result.html")
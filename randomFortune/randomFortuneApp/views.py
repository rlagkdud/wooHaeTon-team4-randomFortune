from random import random
from django.shortcuts import render
import random

# Create your views here.
def getItem():
    itemList = ["모자", "립밤", "팔찌", "반지", "귀걸이", "향수", "손거울", "손수건", "이어폰", "헤드폰", "시계", "셔츠", "긴바지", "반바지", "백팩", "핸드백", "책", "볼펜", "노트북", "태블릿", "니트", "후드티", "자전거", "차", "오토바이", "양산", "우산", "선글라스", "넥타이", "양말", "핸드크림", "카메라", "물티슈", "운동화", "슬리퍼", "구두"]
    luckyItem = random.choice(itemList)
    return luckyItem

def getPlace():
    placeList = ["노래방", "PC방", "식당", "카페", "주유소", "학교", "영화관", "학원", "집", "회사", "공원", "콘서트장", "헬스장", "공항", "볼링장", "당구장", "도서관", "병원", "경찰서", "백화점", "대형마트", "문구점", "병원", "주차장", "옥상", "화장실", "산", "바다", "터미널", "지하철역", "기차역", "버스정류장"]
    luckyPlace = random.choice(placeList)
    return luckyPlace

def getNumber():
    numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    luckyNumber = random.choice(numberList)
    return luckyNumber

def getColor():
    luckyColor = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
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
from django.shortcuts import render
from django.http import HttpResponse
 
from .models import Candidate #models에 정의된 Candidate를 불러온다




# Create your views here.

# def blog(request):
#     return render(request, 'home.html')

def index(request):
    candidates = Candidate.objects.all() #Candidate에 있는 모든 객체를 불러와 candidates에 저장
    str = '' #리턴해줄 문자열(14번째줄)
    for candidate in candidates:
        str += "<p>No. {}번  name. {}<br>".format(candidate.party_number,
            candidate.name)#<br>은 html코드로 다음줄로 줄내림할때 사용
        str += candidate.introduction+"</p>"#<p>는 html코드로 단락이동할때 
    return HttpResponse(str)




from django.shortcuts import render,redirect
import time
# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import FiboniciForm
from .models import FibonanciMethod
from .serilizer import FibonanciSerializer

def index():
    return Response ("hello world")


def fibonanci_out(request):
    starttime = time.time()
    if request.method == "POST":
        form=FiboniciForm(request.POST)
        if form.is_valid:
            fibonanci=[1,1]
            a=int(form.data['number'])
            for i in range(1,(a-1)):
                fibonanci.append(fibonanci[i-1]+fibonanci[i])
            print (fibonanci)
            endtime = time.time()
            total = endtime-starttime
            data = FibonanciMethod(number=a,startTime=starttime, endTime = endtime,
                                   totalTime=total,FiboniciList=fibonanci,Fibonaci_output=fibonanci[a-1])
            data.save()
            return redirect('/lists')
    else:
        form = FiboniciForm()
    return render(request, 'Myapp/fibonanci.html',{'fibo':form})



def fibonice_lists(request):
    data = FibonanciMethod.objects.all()
    return render(request, 'Myapp/output.html',{'output':data})

#=================================django restframeworks=======================================

@api_view(['GET', 'POST'])
def snippet_list(request):
    starttime = time.time()
    if isinstance(request.data['number'], int):
        fibonanci = [1, 1]
        data = (request.data['number'])
        if not data:
            return Response("number is not empty", status=status.HTTP_404_NOT_FOUND)
        elif data<0:
            return Response("Please enter positive number", status=status.HTTP_404_NOT_FOUND)
        for i in range(1, (data - 1)):
            fibonanci.append(fibonanci[i - 1] + fibonanci[i])
        endtime = time.time()
        total = endtime - starttime
        data = FibonanciMethod(number=data, startTime=starttime, endTime=endtime,
                               totalTime=total, FiboniciList=fibonanci, Fibonaci_output=fibonanci[data - 1])
        data.save()
        result={"number":data.number, "startTime":data.startTime,
                "endTime":data.endTime, "totalTime":data.totalTime,
                "FiboniciList":data.FiboniciList, "Fibonaci_output":data.Fibonaci_output}
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response("You must enter a number (i.e. 1,2...)",status=status.HTTP_404_NOT_FOUND)

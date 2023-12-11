from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

# # def demo(request):
# #     return render(request,"demo.html")
#
# # def demo1(request):
# #     name="Australia"
# #     return render(request,"demo1.html",{'obj':name})  #passing value in views to html
#
# def demo2(request):
#     return HttpResponse('This is an html response to show multiple views in django python')
#
# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mult=x*y
#     div=x/y
#     return render(request,'result.html',{'addition':add,
#                                          'subtraction':sub,'multiplication':mult,'division':div})
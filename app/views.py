from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'Name':'Dhruba','Age':23}
    return render(request,'data_render.html',context=d)

def condition(request):
    dict={'A':100,'B':20,'C':150}
    return render(request,'condition.html',context=dict)
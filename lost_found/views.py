from django.shortcuts import render

details=[
    {
        'Name':'Gokul Ramanan',
        'item':'earphones',
        'color':'blue',
        'class': 'SEIT',
        'category':'LostAndFound',
    },

    {
        'Name':'Pranav Kumar',
        'item':'physics book',
        'color':'orange',
        'class': 'SEIT',
        'category':'LostAndFound',
    },
]

# Create your views here.
def home(request):
    return render(request,'lost_found/home.html')

def lf(request):
    context={
        'details':details,
    }
    return render(request,'lost_found/laf.html',context)


# def register(request):
#     return render(request,'lost_found/register.html')

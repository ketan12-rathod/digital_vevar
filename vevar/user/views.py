from django.shortcuts import render,redirect
from user.models import Vevar,Name
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.urls import reverse

# Create your views here.

def index(request, myboy, mygirl):
    id = request.user.id
    # Now myboy and mygirl are obtained from the URL parameters
    # You can use them to retrieve the Name object or perform other logic
    name_object = Name.objects.get(boy_name=myboy, girl_name=mygirl, user_id=id)
    
    context = {
        'myboy': myboy,
        'mygirl': mygirl,
        'result_id': name_object.id  # Pass the ID of the Name object as result_id
        # Other context data you want to pass to the template
    }
    return render(request, 'user/index.html', context)


def store_vevar(request):
    result_id = request.POST['result_id']
    name = request.POST['name']
    village = request.POST['village']
    vevar = request.POST['vevar']
    myboy=request.POST['myboy']
    mygirl=request.POST['mygirl']

    # Assuming you have a Vevar model
    Vevar.objects.create(vevaname=name, village=village, vevar=vevar, name_id=result_id)

    # Generate the URL for the index view using reverse with kwargs
    index_url = reverse('index', kwargs={'myboy': myboy, 'mygirl': mygirl})
    # Replace 'myboy_value' and 'mygirl_value' with appropriate values or variables from your code

    # Redirect to the index view
    return redirect(index_url)

# def all_vevar(request,id):
#     result=Vevar.objects.filter(name_id=id)
   
#     total_sum = Vevar.objects.aggregate(total_sum=Sum('vevar'))['total_sum']
#     context={'result':result,'total_sum':total_sum}
#     return render(request,'user/all_vevar.html',context)

def all_vevar(request, id, boy_name, girl_name):
    result = Vevar.objects.filter(name_id=id)
    total_sum = Vevar.objects.filter(name_id=id).aggregate(total_sum=Sum('vevar'))['total_sum']
    context = {
        'result': result,
        'total_sum': total_sum,
        'girl_name': girl_name,
        'boy_name': boy_name,
    }
    return render(request, 'user/all_vevar.html', context)


def edit_vevar(request,id):
    result=Vevar.objects.get(pk=id)
    context={'result':result}
    return render(request,'user/edit_vevar.html',context)

def update_vevar(request,id):
    myname=request.POST['name']
    myvillage=request.POST['village']
    myvevar=request.POST['vevar']
    
    data={
        'name':myname,
        'village':myvillage,
        'vevar':myvevar
    }
    
    Vevar.objects.update_or_create(pk=id,defaults=data)
    return redirect('/user/all_vevar')

def register(request):
    context={}
    return render(request,'user/register.html',context)

def store_register(request):
    boyname=request.POST['FName']
    girlname=request.POST['LName']
    myusername=request.POST['UName']
    myemail=request.POST['email']
    mypassword=request.POST['password']
    mycpassword=request.POST['cpassword']

    if mycpassword == mypassword:
        User.objects.create_user(first_name=boyname,last_name=girlname,username=myusername,email=myemail,password=mypassword)
        return redirect('/user/info')
    else:
        messages.info(request,'Password not mathching!!')
        return redirect('/user/register')

def info(request):
    context={}
    return render(request,'user/info.html',context)

def store_info(request):
    boyname=request.POST['Name']
    mypassword=request.POST['gName']

    result=auth.authenticate(request,username=boyname,password=mypassword)

    if result is not None:
        auth.login(request,result)
        return redirect('/user/name')
    else:
        messages.info(request,'Password not mathching!!')
        return redirect('/user/info')

def name(request):
    context={}
    return render(request,'user/name.html',context)

# def store_name(request):
#     id=request.user.id
#     myboy=request.POST['Name']
#     mygirl=request.POST['gName']
    
#     Name.objects.create(boy_name=myboy,girl_name=mygirl,user_id=id)
#     return redirect('/user/index')

def store_name(request):
    id = request.user.id
    myboy = request.POST['Name']
    mygirl = request.POST['gName']
    
    # Create the Name object
    name_object = Name.objects.create(boy_name=myboy, girl_name=mygirl, user_id=id)
    
    # Redirect to the index view with myboy and mygirl as parameters
    return redirect('index', myboy=myboy, mygirl=mygirl)

def all_name(request, boy_name, girl_name):
    id=request.user.id
    result=Name.objects.filter(user_id=id)
    context={
            'result':result,
            'girl_name': girl_name,
            'boy_name': boy_name
            }
    return render(request,'user/all_name.html',context)


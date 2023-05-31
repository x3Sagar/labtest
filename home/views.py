from django.shortcuts import render,HttpResponse
import csv
from django.core.mail import send_mail
from home.models import test,accounts

# Create your views here.
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def email(k):                     #k=dictionary
  name=k['name']
  send=k['email']
  test=[]
  l=len(k)
  for key,val in k.items():
    if key!='name' or key!='email' or key!='gender' or key!='age' or key!='adderess':
      test.append(val)
  test=str(test)
  content='''Thank you ,'''+name+''',\n for placing an apointment in pathology lab,for'''+test+'''\n you
  will pay for test on arrival \n
  ,best regards!'''
  return send_mail(
    'pathology lab',
    content,
    'projectcs404@gmail.com',
    [send],
    fail_silently=False
  )

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def homel(request):                                                    #for login
    if  request.method=="POST":                                    
      con=request.POST.get('contact')
      name=request.POST.get('Name')
      if accounts.objects.filter(contact=con).exists():
        if accounts.objects.filter(contact=con).exists():
          return render(request,'home.html',{'name':name})
        else:
          return HttpResponse('signup before!')
      else:
        return HttpResponse('signup before!')
    else:
      return render('home.html')

def homes(request):  
  if  request.method=="POST":                                             #for signup
    name=request.POST.get('Name')
    age=request.POST.get('age')
    con=request.POST.get('contact')
    email=request.POST.get('email')
    gen=request.POST.get('gender')


    if accounts.objects.filter(contact=con).exists():
      return HttpResponse('contact number already exists!')
    elif accounts.objects.filter(email=email).exists():
      return HttpResponse('email already exists!')

    else:
        acc=accounts()
        acc.name=name
        acc.age=age
        acc.email=email
        acc.gender=gen
        acc.contact=con
        
        acc.save()
        return render(request,'home.html')
  else:
    print('something wrong')

    

def lab(request):
    if request.method=='POST':
        dict1=request.POST
        #k={}
        #for i,j in dict1:
        #  if i=='name' and i=='email':
        #   k[i]=j 
        with open('report.csv','a') as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
              wrt.writerow([key,value])
            #email(k)
            #del k                                               #firewall refused to connect actively
    return render(request,'pop.html')
def labtest(request):
  tests=test.objects.all()
  return render(request,'labtest.html',{'tests':tests})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def acc(request):
  return render(request,'acount.html')

def home(request):
  return render(request,'home.html')
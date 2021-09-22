from django.shortcuts import render



def home(request):
    # return render(request, 'myapp/layout.html') 
    if request.method == "POST":
       number = int(request.POST.get("num1"))
       if number<0:
          return render(request, 'myapp/layout.html', context={"message":"Please enter positive number"})
       elif number>500:
          return render(request, 'myapp/layout.html', context={"message":'Please enter number less than 500'})
       else:
          result = [i for i in range(1, number+1)]
          return render(request, 'myapp/num.html', {"listnum": result , "link":"http://127.0.0.1:8000"})
    return render(request, "myapp/layout.html", {})

# def numdisplay(request):
#     if request.method == "POST":
#        number = int(request.GET["num1"])
#        if number<0:
#           return render(request, 'myapp/layout.html', context={"message":"Please enter positive number"})
#        elif number>500:
#           return render(request, 'myapp/layout.html', context={"message":'Please enter number less than 500'})
#        else:
#           result = [i for i in range(1, number+1)]
#           return render(request, 'myapp/num.html', {"listnum": result , "link":"http://127.0.0.1:8000"})
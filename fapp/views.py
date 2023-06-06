from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from fapp.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method == "POST":
        data = request.POST
        newuser = User.objects.create_user(username = data["user"], password = data["password"])
        newuser.save()
        return redirect ("http://127.0.0.1:8000/second")
    return render(request, 'reg.html')

def main(request):
    return render(request, 'nav.html')

def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username = data["user"], password = data["password"])
        if user is not None:
            request.session['is_auth'] = True 
            return redirect ("http://127.0.0.1:8000/second")
        else:
            return HttpResponse("Вы ошиблись")
    return render (request, 'auth.html')

def second(request):
    res = []
    if request.method == "POST":
        data = request.POST 
        res = Product1.objects.filter(Name = data["search"])
    cat_list = ProdCategory.objects.all()
    prod = Product1.objects.all()
    return render(request, 'navbar.html',{"cat":cat_list, "search":res, "prod":prod})

def cat_page(request, cat_name):
    catid = ProdCategory.objects.filter(category_name=cat_name)
    prod = Product1.objects.filter(cat = catid[0].id)
    cat_list = ProdCategory.objects.all()
    return render(request, 'prod.html', {"prod":prod, "categ":cat_list})

def card_page(request, prod_name):
    if request.method == "POST":
        if request.session.get('is_auth', None) != None:
            data = request.POST
            cart = Cart(user_id = request.session.get('is_auth', None), product_id = int(data["prodid"]))
            cart.save()
        else:
            return redirect ("http://127.0.0.1:8000/auth")
    catid = Product1.objects.filter(id = prod_name)
    return render(request, 'card.html', {"card":catid})
    

def contact_us(request):
    cat_list = ProdCategory.objects.all()
    prod = Product1.objects.all()
    return render(request, 'contact_us.html', {"product":prod, "category":cat_list})

def cart(request):
    prod = Cart.objects.filter( user_id = request.session.get('is_auth', None)) # при переходе в корзину мы отрисовываем все что данный пользователь добавил
    if request.method == "POST":
        if  request.session.get('is_auth', None) != None:
            data = request.POST
            print(data)
            delobj = Cart.objects.filter(user_id = request.session.get('is_auth', None), product_id = data["prodid"])
            delobj.delete() # а вот тут удаляем тот обьект который нам не нравится

    return render(request, 'cart.html',{"prod":prod})  # страницу отрисовываем всегда 
    
#def cart_del(request):
#    if request.method == "POST":
#        if request.session.get('is_auth', None) != None:
#            data = request.POST
#            Cart.objects.filter(user_id = request.session.get('is_auth', None), product_id = int(data["prodid"])).delete()
#    return render(request, 'cart.html')
#

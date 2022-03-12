from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User

from accounts.models import History, Item, Juma_User

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['user_email']
        password = request.POST['user_password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_phone = request.POST['user_phone']
        user_photo = request.FILES['user_photo']

        user = Juma_User(
            user_name = user_name,
            user_phone = user_phone,
            user_email = user_email,
            user_password = user_password,
            user_photo = user_photo
            )
        user.save()

        user = User(
            username = user_email,
            password = user_password,
            )
        user.save()
        return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        user_email = request.user.username
        user_obj = Juma_User.objects.filter(user_email=user_email)[0]
        sale_items = Item.objects.filter(item_owner=user_obj)
        bought_items = History.objects.filter(item_buyer=user_obj)
        data = {
            'user' : user_obj,
            'sale_items' : sale_items,
            'bought_items' : bought_items
        }
        return render(request, 'profile.html',data)
    else:
        return redirect('/accounts/login/')
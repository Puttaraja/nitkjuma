from distutils.command.sdist import sdist
from unicodedata import category
from django.shortcuts import redirect, render

from accounts.models import Item_Type, Item, Juma_User

# Create your views here.
def categories(request):
    if request.user.is_authenticated:
        categories = Item_Type.objects.all()
        data = {
            'categories' : categories
        }
        return render(request, 'store.html', data)
    else:
        return redirect('/accounts/login/')

def items(request,**kwargs):
    if request.user.is_authenticated:
        user_email = request.user.username
        user_obj = Juma_User.objects.filter(user_email=user_email)[0]
        id = kwargs['cat_id']
        categories = Item_Type.objects.all()
        item_type = Item_Type.objects.filter(id=id)[0]
        items = Item.objects.filter(item_type=item_type)
        cat = Item_Type.objects.filter(id=id)[0]
        data = {
            'items' : items,
            'categories' : categories,
            'cat' : cat
        }
        return render(request, 'items.html', data)
    else:
        return redirect('/accounts/login/')

def item(request,**kwargs):
    if request.user.is_authenticated:
        item_id = kwargs['item_id']
        print(item_id)
        item = Item.objects.filter(id=item_id)[0]
        seller_obj = item.item_owner
        data = {
            'item' : item,
            'seller' : seller_obj
        }
        return render(request, 'item.html', data)
    else:
        return redirect('/accounts/login/')


def upload(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            user_email = request.user.username
            print(user_email)
            user_obj = Juma_User.objects.filter(user_email=user_email)[0]
            item_type_id = request.POST['item_type']
            print(item_type_id)
            category = Item_Type.objects.filter(id=item_type_id)[0]
            print(user_email)
            new_item = Item(
                item_type = category,
                item_name = request.POST['item_name'],
                item_owner = user_obj,
                item_price = request.POST['item_price'],
                item_description = request.POST['item_description'],
                item_image = request.FILES['item_image']
            )
            print(user_email)
            new_item.save()
            print(user_email)
            return redirect('/store/upload/')
        else:
            categories = Item_Type.objects.all()
            data = {
                'categories' : categories
            }
            return render(request, 'upload.html', data)
    else:
        return redirect('/accounts/login/')
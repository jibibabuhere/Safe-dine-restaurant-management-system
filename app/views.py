from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import *


def login(request):
    return render(request, "admin/Login.html")




def logoutcode(request):
  return render(request,"admin/login.html")


def addlogincode(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']

    try:

        ob=login_table.objects.get(username=uname,password=pswd)
        if ob.type == 'admin':
            return HttpResponse('''<script>alert("welcome to adminhome");window.location='/admin_home'</script>''')

        elif ob.type == 'restaurant':
            request.session["lid"] = ob.id
            return HttpResponse('''<script>alert("welcome to resturant home");window.location='/restaurant_home'</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')

    except:
        return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')

def accept(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='restaurant'
    ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location='/Verify_restuarent'</script>''')



def reject(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'rejected'
    ob.save()
    return HttpResponse('''<script>alert('Rejected.......');window.location='/Verify_restuarent'</script>''')

def edit_food_ispector(request,id):
    ob = inspector_table.objects.get(id=id)
    return render(request,'admin/edit foodinspector.html',{'val':ob})


def edit_food_inspector_post(request):
    edit_name = request.POST['textfield']
    edit_gender = request.POST['fav_language']
    edit_address = request.POST['textarea']
    edit_phone = request.POST['textfield2']
    edit_email = request.POST['textfield3']
    edit_photo = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(edit_photo.name, edit_photo)
    edit_position = request.POST['textfield7']

    # ins_c_password = request.POST['textfield6']
    ob2 = login_table()
    ob2.type = 'inspector'
    ob2.save()

    ob = inspector_table()
    ob.name = edit_name
    ob.gender = edit_gender
    ob.address = edit_address
    ob.phone = edit_phone
    ob.photo = fsave
    ob.email = edit_email
    ob.position = edit_position
    ob.login = ob2
    # ob.password = ins_c_password

    ob.save()
    return HttpResponse('''<script>alert("Updated");window.location='/'</script>''')


def delete_food_ispector(request,id):
    ob=inspector_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleting the Inspector.......');window.location='/manage_menu_add_item'</script>''')

def manage_food_inspector(request):
    ob = inspector_table.objects.all()
    return render(request, "admin/Manage Food Inspector.html",{'val':ob})

def add_food_inspector(request):
    return render(request, "admin/Add foodinspector.html")




def manage_food_menu(request):
    ob = food_menu.objects.all()
    return render(request, "restaurant/manage food menu.html",{'val':ob})

# def add_food_item(request):
#     return render(request, "admin/Add foodinspector.html")

def add_food_item(request):
    menu_name = request.POST['textfield']
    menu_details = request.POST['textfield3']
    menu_price = request.POST['textfield2']
    menu_stock = request.POST['textfield4']
    menu_quantity = request.POST['textfield5']
    menu_photo = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(menu_photo.name, menu_photo)

    ob = food_menu()
    ob.name = menu_name
    ob.details = menu_details
    ob.price = menu_price
    ob.stock = menu_stock
    ob.quantity = menu_quantity
    ob.image = fsave
    ob.restaurant=restaurant.objects.get(login=request.session["lid"])

    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/manage_menu_add_item'</script>''')
def delete_food_item(request,id):

    print("============================",id)
    ob=food_menu.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleting the Item.......');window.location='/manage_menu_add_item'</script>''')

def manage_menu_add_item(request):
    ob = food_menu.objects.all()
    return render(request, "restaurant/manage menu add item.html",{'val':ob})


def restaurant_home(request):
    return render(request, "restaurant/Restaurant home.html")

def view_restaurent_profile(request):
    ob = restaurant.objects.get(login=request.session['lid'])
    return render(request, "restaurant/view restauarant profile.html",{'val':ob})


def restaurant_registration(request):
    return render(request, "restaurant/restaurant registration.html")



def addreg(request):
    name=request.POST['textfield']
    photo=request.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(photo.name,photo)
    place=request.POST['textarea']
    post = request.POST['textfield2']
    pin = request.POST['textfield3']
    phone = request.POST['textfield4']
    email = request.POST['textfield5']
    certificate = request.FILES['file2']
    fc = FileSystemStorage()
    fo = fc.save(certificate.name, certificate)
    username = request.POST['textfield6']
    password = request.POST['textfield7']




    obj=login_table()
    obj.username=username
    obj.password=password
    obj.type='pending'
    obj.save()


    ob=restaurant()
    ob.name=name
    ob.photo=fp
    ob.phone=phone
    ob.email=email
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.certificate=fo
    ob.login=obj
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/'</script>''')

def add_inspetor_details(request):
    ins_name = request.POST['textfield']
    ins_gender = request.POST['fav_language']
    ins_address = request.POST['textarea']
    ins_phone = request.POST['textfield2']
    ins_email = request.POST['textfield3']
    ins_photo = request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(ins_photo.name,ins_photo)
    ins_position = request.POST['textfield7']
    ins_username = request.POST['textfield4']
    ins_password = request.POST['textfield5']
    # ins_c_password = request.POST['textfield6']


    ob1=login_table()
    ob1.username=ins_username
    ob1.password=ins_password
    ob1.type='inspector'
    ob1.save()


    ob = inspector_table()
    ob.name = ins_name
    ob.gender = ins_gender
    ob.address = ins_address
    ob.phone = ins_phone
    ob.photo = fsave
    ob.email = ins_email
    ob.position = ins_position
    ob.login = ob1
    # ob.password = ins_c_password


    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/'</script>''')

def restaurent_profile(request):
    ob = restaurant.objects.get(login=request.session["lid"])
    return render(request, "restaurant/restaurent profile.html",{"val":ob})



def restaurent_profile_edit_post(request):
    rest_name = request.POST['textfield']
    rest_phone = request.POST['textfield4']
    rest_email = request.POST['textfield5']
    rest_place = request.POST['textarea']
    rest_post = request.POST['textfield2']
    rest_pin = request.POST['textfield3']
    rest_photo = request.FILES['file']
    rest_certificate = request.FILES['file2']

    fs = FileSystemStorage()
    fsave = fs.save(rest_photo.name, rest_photo)


    # ins_c_password = request.POST['textfield6']


    ob = restaurant.objects.get(login=request.session["lid"])
    ob.name = rest_name
    ob.phone = rest_phone
    ob.email = rest_email
    ob.place = rest_place
    ob.post = rest_post
    ob.pin = rest_pin
    ob.photo = fsave

    ob.certificate = rest_certificate
    ob.save()

    # ob.password = ins_c_password


    ob.save()
    return HttpResponse('''<script>alert("Updated");window.location='/view_restaurent_profile'</script>''')

def send_replay(request,id):
    request.session['oo']=id
    return render(request, "restaurant/send replay.html")

def sreplay(request):
    replay=request.POST['textfield']
    ob=complaint.objects.get(id=request.session['oo'])
    ob.replay=replay
    ob.save()
    return HttpResponse('''<script>alert("Reply sent");window.location='/view_complaints'</script>''')



def Verify_restuarent(request):
    ob=restaurant.objects.filter(login__type='pending')
    return render(request, "admin/Verify restuarent.html",{"val":ob})

def View_accepted_restuarent(request):
    ob=restaurant.objects.filter(login__type='restaurant')
    return render(request, "admin/View_accepted_shop.html",{"val":ob})

def view_assigned_work(request):
    return render(request, "restaurant/view assigned work.html")


def view_booking(request):
    ob = order.objects.all()
    return render(request, "admin/view booking.html",{'val':ob})



def view_booking_view_more(request):
    ob = order_details.objects.all()
    return render(request, "admin/view booking view more.html",{'val':ob})


def view_complaints_and_take_action(request):
    ob = complaint.objects.all()
    return render(request, "admin/view complaints and take action.html",{'val':ob})


def view_complaints(request):
    ob = complaint.objects.all()
    return render(request, "restaurant/view complaints.html",{'val':ob})


def view_fitness_certificate(request):
    ob = certificate.objects.all()
    return render(request, "admin/view fitness certificate.html",{'val':ob})



def view_order(request):
    ob = order.objects.all()
    return render(request, "restaurant/view order.html",{'val':ob})


def view_order_and_status(request,id):
    ob=order_details.objects.filter(order_id__id=id)
    return render(request, "restaurant/view order and status .html",{'val':ob})

def view_payment(request):
    ob = payment.objects.all()
    return render(request, "restaurant/view payment.html",{'val':ob})


def view_review_rating(request):
    ob = rating_review.objects.all()
    return render(request, "admin/view review rating.html",{'val':ob})




def view_rating_review(request):
    ob = rating_review.objects.all()
    return render(request, "restaurant/view rating and review.html",{'val':ob})





def view_user(request):
    ob = user.objects.all()
    return render(request, "restaurant/view user.html",{'val':ob})




def action(request):
    return render(request, "admin/action.html")



def admin_home(request):
    return render(request, "admin/Admin home.html")


def assign_deliveryboy(request,id):
    request.session['pp']=id
    ob = delivery_boy.objects.filter(id=id)
    return render(request, "restaurant/assign deliveryboy.html",{'val':ob})


def add_delivery_boy(request):
    ob = assign.objects.all()
    ob.date = datetime.today()
    ob.status='pending'

    return HttpResponse('''<script>alert("Assigned"...);window.location="//"</script>''')



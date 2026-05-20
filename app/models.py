from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class user(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    photo = models.FileField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    date = models.DateField()



class restaurant(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    photo = models.FileField()
    certificate = models.FileField()



class delivery_boy(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    phone = models.BigIntegerField()
    photo = models.FileField()
    email = models.EmailField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class inspector_table(models.Model):
    login=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    photo = models.FileField()
    email = models.EmailField()
    position = models.CharField(max_length=100)

class food_menu(models.Model):

    restaurant = models.ForeignKey(restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    image = models.FileField()
    price = models.IntegerField()
    stock = models.IntegerField()
    quantity = models.IntegerField()


class certificate(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    inspector = models.ForeignKey(inspector_table, on_delete=models.CASCADE)
    certificate = models.FileField()
    report = models.FileField()
    date = models.DateField()

class order(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    landmark = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class order_details(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(food_menu, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()



class payment(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(food_menu, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=100)


class chat(models.Model):
    from_id = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="fromid")
    to_id = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="toid")
    message = models.CharField(max_length=100)
    date = models.DateField()


class complaint(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    replay = models.CharField(max_length=100)

class action(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    restaurant =models.ForeignKey(restaurant, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=100)
    inspector = models.ForeignKey(inspector_table, on_delete=models.CASCADE)

class rating_review(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    menu = models.ForeignKey(food_menu, on_delete=models.CASCADE)
    # restaurant=models.ForeignKey(restaurant, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.CharField(max_length=100)
    date = models.DateField()




class assign(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=100)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    delivery_boy_id = models.ForeignKey(delivery_boy, on_delete=models.CASCADE)
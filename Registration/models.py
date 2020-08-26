from django.db import models
import uuid


class Guest(models.Model):
    fname=models.CharField(max_length=20)
    age=models.IntegerField()
    guestid=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    marital_status=models.CharField(max_length=20)
    house_name=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phone=models.IntegerField()
    guest_email=models.EmailField(max_length=50)


class Agent(models.Model):
    agentid=models.CharField(max_length=50,default='SRNTYAG101')
    agent_name=models.CharField(max_length=50)
    aget_phone=models.IntegerField()
    agentemail=models.EmailField(max_length=50)
    address = models.CharField(max_length=20)


class Booking(models.Model):
    guestemail = models.EmailField(max_length=50)
    bookingid= models.CharField(max_length=50)
    bid = models.UUIDField(default=uuid.uuid4, editable=False)
    agentid = models.CharField(max_length=50)
    no_of_rooms=models.IntegerField()
    room_number=models.CharField(max_length=50)
    no_of_adults=models.IntegerField()
    no_of_childrens=models.IntegerField()
    proof_submitted=models.CharField(max_length=50)
    check_in_date=models.CharField(max_length=50)
    checkindate=models.CharField(max_length=50)
    check_out_date=models.CharField(max_length=50)
    grc_number=models.CharField(max_length=50)
    total_amount=models.IntegerField()
    advance_amount=models.IntegerField()
    balance_amount=models.IntegerField()
    paymentmode=models.CharField(max_length=50)


class admin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50,default='user')


class room(models.Model):
    roomnumber=models.IntegerField()
    floornumber=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    roomtype=models.CharField(max_length=50 ,default='none')
    rate=models.IntegerField(default=0)
    status=models.CharField(max_length=50,default='Available')


class Floor(models.Model):
    floorno=models.CharField(max_length=50)
    noofrooms=models.IntegerField()

class Roomcategory(models.Model):
    category=models.CharField(max_length=50)
    ac=models.CharField(max_length=50)
    wifi=models.CharField(max_length=50)
    beverage=models.CharField(max_length=50)
    breakfast=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    rate = models.IntegerField()
    status=models.CharField(max_length=50,default='okay')
    staticcategory=models.CharField(max_length=50,default='okay')

class Roomtype(models.Model):
    type=models.CharField(max_length=50)
    noofbeds=models.IntegerField()
    area=models.CharField(max_length=50)
    rate=models.IntegerField()



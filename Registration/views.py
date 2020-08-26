import sqlite3

from django.db.models import Count, Func
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from Registration.models import *
import datetime
now = datetime.datetime.today()

def test(request):
    return render(request,'test.html')


def bookings(request):
    # roomval = Booking.objects.latest('room_number').room_number
    # print(roomval)
    usersession = admin.objects.get(username=request.session['mail'])

    roysuiteval=Roomcategory.objects.filter(category='Royal suite')
    presuiteval = Roomcategory.objects.filter(category='Premium suite')
    exesuiteval = Roomcategory.objects.filter(category='Executive suite')
    tensuiteval = Roomcategory.objects.filter(category='Tent camping')

    bkngid = Booking.objects.all()
    guestid = Guest.objects.all()
    obb = Booking.objects.all().raw('select * from Registration_booking where id>42 order by id desc')

    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    full = 0
    exist = c.fetchone()

    if exist is None:
        full = 0
        Booking.objects.get_or_create(bookingid='SRNTYBKNG100', checkindate='March 07, 2020', room_number=1, no_of_rooms=1,
                                      guestemail='none@1',
                                      no_of_adults=1, no_of_childrens=1, proof_submitted='none', check_in_date='March 7, 2020, 11:08 p.m.',
                                      check_out_date='2020-03-06 18:30:00', grc_number=1, total_amount=1, advance_amount=1,
                                      balance_amount=1, paymentmode='none'
                                      )
    else:
        full = 1
        roomval = Booking.objects.last().room_number
        print(roomval)
        tolist = roomval.split(',')
        for index, i in enumerate(tolist):
            print(index, i)
            v = room.objects.get(roomnumber=i)
            v.status = 'Booked'
            v.save()
            print(v)
            conn.commit()

    lastid = Booking.objects.latest('bookingid').bookingid
    lastidsplt = lastid.rpartition('G')[2]
    lastidsplttoint = int(lastidsplt) + 1
    lastidsplttostr = str(lastidsplttoint)
    newval = 'SRNTYBKNG' + lastidsplttostr



    agentob=Agent.objects.all().raw('select * from Registration_agent where agentid !=%s',['SRNTYAG100'])

    roomob1 = room.objects.filter(category='Royal suite').filter(status='Available')
    roomob2 = room.objects.filter(category='Premium suite').filter(status='Available')
    roomob3 = room.objects.filter(category='Executive suite').filter(status='Available')
    roomob4 = room.objects.filter(category='Tent camping').filter(status='Available')



    tdy=datetime.date.today()
    formatedDate = tdy.strftime("%B %d, %Y")
    no = Booking.objects.filter(checkindate=formatedDate).values('room_number').count()
    roomob=room.objects.all()
    ob=Booking.objects.all()
    ob1 = Guest.objects.raw("select * from Registration_guest as a inner join Registration_booking  as b on a.guest_email=b.guestemail ORDER BY a.id DESC")
    ob3 = Booking.objects.raw("select * from Registration_agent as a ,Registration_booking  as b where a.agentid=b.agentid ")
    now = datetime.datetime.now()
    if request.method=='POST' and 'agentsearchbtn' in request.POST:
        val=request.POST.get('agentid')
        agntsearchob=Agent.objects.raw('select * from Registration_agent where agentid=%s',[val])
        return render(request, 'bookings.html',
                      context={'bookingid': newval,'roomob1':roomob1,'roomob2':roomob2,'roomob3':roomob3,'roomob4':roomob4, 'data4':agentob, 'today':formatedDate, 'time':now,'bid':ob,'data1':ob1,'data2':roomob,'data3':no,
                               'data5':agntsearchob, })

    if request.method=='POST' and 'btn1' in request.POST:


        cv1=request.POST.get('cfname')
        cv2=request.POST.get('cphone')
        cv3=request.POST.get('cemail')
        cv4=request.POST.get('caddress')
        cv5=request.POST.get('cage')
        cv6=request.POST.get('cgender')
        cv7=request.POST.get('cmaritalstatus')
        cv8=request.POST.get('ccountry')
        cv9=request.POST.get('cstate')
        cv10=request.POST.get('cdistrict')
        cv11=request.POST.get('cpincode')

        av12=request.POST.get('agentid')
        av13=request.POST.get('agentname')
        av14=request.POST.get('agentnumber')
        # av15=request.POST.get('aaddress')
        # av16=request.POST.get('aage')
        # av17=request.POST.get('agender')
        # av18=request.POST.get('noofcustomers')

        v19=request.POST.get('numberofrooms')

        v55=request.POST.get('bkid')
        # v21=request.POST.get('roomnumber')
        # v22=request.POST.get('floornumber')
        v23=request.POST.get('numberofadults')
        v24=request.POST.get('proofsubmitted')
        v25=request.POST.get('grcnumber')
        v26=request.POST.get('checkin')
        v27=request.POST.get('checkout')

        v28=request.POST.get('totalamount')
        v29=request.POST.get('advanceamount')
        v30=request.POST.get('balanceamount')
        v31=request.POST.get('paymentmode')
        v32 = request.POST.get('numberofchildrens')
        v33=request.POST.get('checkindate')

        v200 = request.POST.get('selectedrooms')
        vvv=v200.split(',')#string to list split by commas
        vvvv=set(vvv)#list to set to avoid duplication
        vvvvv=list(vvvv)#set to lst
        str1 = ','.join(vvvvv)#list to string to save
        str2=str1.lstrip(',')#remove left comma of string
        v20 = str2
        Guest.objects.get_or_create(guestid=v55, fname=cv1,age=cv5,gender=cv6,marital_status=cv7,house_name=cv4,district=cv10,state=cv9,country=cv8,pincode=cv11,phone=cv2,guest_email=cv3)

        Booking.objects.get_or_create(bookingid=v55, agentid=av12, checkindate=v33,room_number=v20,no_of_rooms=v19,guestemail=cv3,
                                      no_of_adults=v23,no_of_childrens=v32,proof_submitted=v24,check_in_date=v26,
                                      check_out_date=v27,grc_number=v25,total_amount=v28,advance_amount=v29,balance_amount=v30,paymentmode=v31)
        roomval = Booking.objects.last().room_number
        messages.add_message(request, messages.SUCCESS, "Booking successfull")
        print(roomval)
        tolist = roomval.split(',')
        for i in tolist:
            if i!='':
                print(tolist.index(i), i)
                v = room.objects.get(roomnumber=i)
                v.status = 'Booked'

                v.save()
                print(v)
        conn.commit()
        return redirect(Reciept)

    if request.method == 'POST' and 'bookingsearchbtn' in request.POST:
        val=request.POST.get('bookngid')
        gustob=Guest.objects.raw('select * from Registration_guest where guestid=%s ',[val])
        bkngob = Booking.objects.raw('select * from Registration_booking where bookingid=%s ', [val])
        return render(request, 'bookings.html',
                      context={ 'bkngob':bkngob, 'gustob':gustob, 'bkngid': bkngid, 'guestid': guestid, 'demo': ob3, 'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})
    if request.method == 'POST' and 'updatebtn' in request.POST:
        updateob= Guest.objects.get(guestid=request.POST.get('updatebtn'))
        updateob1 = Booking.objects.get(bookingid=request.POST.get('updatebtn'))
        updatedcv3 = request.POST.get('updatedcemail')

        updatedav12 = request.POST.get('updatedagentid')
        updatedv19 = request.POST.get('updatednumberofrooms')
        # updatedv20 = request.POST.get('updatedselectedrooms')



        updatedv23 = request.POST.get('updatednumberofadults')
        updatedv24 = request.POST.get('updatedproofsubmitted')
        updatedv25 = request.POST.get('updatedgrcnumber')
        updatedv26 = request.POST.get('updatedcheckin')
        updatedv27 = request.POST.get('updatedcheckout')
        updatedv28 = request.POST.get('updatedtotalamount')
        updatedv29 = request.POST.get('updatedadvanceamount')
        updatedv30 = request.POST.get('updatedbalanceamount')
        updatedv31 = request.POST.get('updatedpaymentmode')
        updatedv32 = request.POST.get('updatednumberofchildrens')
        updatedv33 = request.POST.get('updatedcheckindate')

        v200 = request.POST.get('updatedselectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        updatedv20 = str2

        tolist = updatedv20.split(',')
        for i in tolist:
            if i != '':
                print(tolist.index(i), i)
                v = room.objects.get(roomnumber=i)
                v.status = 'Booked'
                v.save()
                print(v)
        conn.commit()

        updateob1.guestemail=updatedcv3
        updateob1.agentid=updatedav12
        updateob1.no_of_rooms=updatedv19
        updateob1.room_number=updatedv20
        updateob1.no_of_adults=updatedv23
        updateob1.proof_submitted=updatedv24
        updateob1.grc_number=updatedv25
        updateob1.check_in_date=updatedv26
        updateob1.check_out_date=updatedv27
        updateob1.total_amount=updatedv28
        updateob1.advance_amount=updatedv29
        updateob1.balance_amount=updatedv30
        updateob1.paymentmode=updatedv31
        updateob1.no_of_childrens=updatedv32
        updateob1.checkindate=updatedv33
        updateob1.save()

        messages.add_message(request, messages.SUCCESS, "Booking details updated successffully")
        return render(request, 'bookings.html',
                      context={ 'bkngid': bkngid, 'guestid': guestid, 'demo': ob3,
                               'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})

    return render(request, 'bookings.html',context={'usersession': usersession,'roysuiteval':roysuiteval,'presuiteval':presuiteval,'exesuiteval':exesuiteval,'tensuiteval':tensuiteval, 'bkngid':bkngid,'guestid':guestid, 'demo':ob3,'bookingid': newval,'roomob1':roomob1,'roomob2':roomob2,'roomob3':roomob3,'roomob4':roomob4, 'data4':agentob, 'today':formatedDate, 'time':now,'bid':ob,'data1':obb,'data2':roomob,'data3':no})


def bookingsadmin(request):
    # roomval = Booking.objects.latest('room_number').room_number
    # print(roomval)
    usersession = admin.objects.get(username=request.session['mail'])
    roysuiteval=Roomcategory.objects.filter(category='Royal suite')
    presuiteval = Roomcategory.objects.filter(category='Premium suite')
    exesuiteval = Roomcategory.objects.filter(category='Executive suite')
    tensuiteval = Roomcategory.objects.filter(category='Tent camping')

    bkngid = Booking.objects.all()
    guestid = Guest.objects.all()
    obb = Booking.objects.all().raw('select * from Registration_booking where id>42 order by id desc ')

    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    full = 0
    exist = c.fetchone()

    if exist is None:
        full = 0
        Booking.objects.get_or_create(bookingid='SRNTYBKNG100', checkindate='March 07, 2020', room_number=1, no_of_rooms=1,
                                      guestemail='none@1',
                                      no_of_adults=1, no_of_childrens=1, proof_submitted='none', check_in_date='March 7, 2020, 11:08 p.m.',
                                      check_out_date='2020-03-06 18:30:00', grc_number=1, total_amount=1, advance_amount=1,
                                      balance_amount=1, paymentmode='none'
                                      )
    else:
        full = 1
        roomval = Booking.objects.last().room_number
        print(roomval)
        tolist = roomval.split(',')
        for index, i in enumerate(tolist):
            print(index, i)
            v = room.objects.get(roomnumber=i)
            v.status = 'Booked'
            v.save()
            print(v)
            conn.commit()

    lastid = Booking.objects.latest('bookingid').bookingid
    lastidsplt = lastid.rpartition('G')[2]
    lastidsplttoint = int(lastidsplt) + 1
    lastidsplttostr = str(lastidsplttoint)
    newval = 'SRNTYBKNG' + lastidsplttostr



    agentob=Agent.objects.all().raw('select * from Registration_agent where agentid !=%s',['SRNTYAG100'])

    roomob1 = room.objects.filter(category='Royal suite').filter(status='Available')
    roomob2 = room.objects.filter(category='Premium suite').filter(status='Available')
    roomob3 = room.objects.filter(category='Executive suite').filter(status='Available')
    roomob4 = room.objects.filter(category='Tent camping').filter(status='Available')



    tdy=datetime.date.today()
    formatedDate = tdy.strftime("%B %d, %Y")
    no = Booking.objects.filter(checkindate=formatedDate).values('room_number').count()
    roomob=room.objects.all()
    ob=Booking.objects.all()
    ob1 = Guest.objects.raw("select * from Registration_guest as a inner join Registration_booking  as b on a.guest_email=b.guestemail ORDER BY a.id DESC")
    ob3 = Booking.objects.raw("select * from Registration_agent as a ,Registration_booking  as b where a.agentid=b.agentid ")
    now = datetime.datetime.now()
    if request.method=='POST' and 'agentsearchbtn' in request.POST:
        val=request.POST.get('agentid')
        agntsearchob=Agent.objects.raw('select * from Registration_agent where agentid=%s',[val])
        return render(request, 'admin/bookings.html',
                      context={'bookingid': newval,'roomob1':roomob1,'roomob2':roomob2,'roomob3':roomob3,'roomob4':roomob4, 'data4':agentob, 'today':formatedDate, 'time':now,'bid':ob,'data1':ob1,'data2':roomob,'data3':no,
                               'data5':agntsearchob, })

    if request.method=='POST' and 'btn1' in request.POST:


        cv1=request.POST.get('cfname')
        cv2=request.POST.get('cphone')
        cv3=request.POST.get('cemail')
        cv4=request.POST.get('caddress')
        cv5=request.POST.get('cage')
        cv6=request.POST.get('cgender')
        cv7=request.POST.get('cmaritalstatus')
        cv8=request.POST.get('ccountry')
        cv9=request.POST.get('cstate')
        cv10=request.POST.get('cdistrict')
        cv11=request.POST.get('cpincode')

        av12=request.POST.get('agentid')
        av13=request.POST.get('agentname')
        av14=request.POST.get('agentnumber')


        v19=request.POST.get('numberofrooms')
        v55=request.POST.get('bkid')

        v23=request.POST.get('numberofadults')
        v24=request.POST.get('proofsubmitted')
        v25=request.POST.get('grcnumber')
        v26=request.POST.get('checkin')
        v27=request.POST.get('checkout')

        v28=request.POST.get('totalamount')
        v29=request.POST.get('advanceamount')
        v30=request.POST.get('balanceamount')
        v31=request.POST.get('paymentmode')
        v32 = request.POST.get('numberofchildrens')
        v33=request.POST.get('checkindate')

        v200 = request.POST.get('selectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        v20 = str2

        Guest.objects.get_or_create(guestid=v55, fname=cv1,age=cv5,gender=cv6,marital_status=cv7,house_name=cv4,district=cv10,state=cv9,country=cv8,pincode=cv11,phone=cv2,guest_email=cv3)

        Booking.objects.get_or_create(bookingid=v55, agentid=av12, checkindate=v33,room_number=v20,no_of_rooms=v19,guestemail=cv3,
                                      no_of_adults=v23,no_of_childrens=v32,proof_submitted=v24,check_in_date=v26,
                                      check_out_date=v27,grc_number=v25,total_amount=v28,advance_amount=v29,balance_amount=v30,paymentmode=v31)
        messages.add_message(request, messages.SUCCESS, "Booking successfull")
        roomval = Booking.objects.last().room_number
        tolist = roomval.split(',')
        for i in tolist:
            if i!='':
                v = room.objects.get(roomnumber=i)
                v.status = 'Booked'
                v.save()
        conn.commit()
        return redirect(Recieptadmin)

    if request.method == 'POST' and 'bookingsearchbtn' in request.POST:
        val=request.POST.get('bookngid')
        gustob=Guest.objects.raw('select * from Registration_guest where guestid=%s ',[val])
        bkngob = Booking.objects.raw('select * from Registration_booking where bookingid=%s ', [val])
        return render(request, 'admin/bookings.html',
                      context={ 'bkngob':bkngob, 'gustob':gustob, 'bkngid': bkngid, 'guestid': guestid, 'demo': ob3, 'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})
    if request.method == 'POST' and 'updatebtn' in request.POST:
        updateob= Guest.objects.get(guestid=request.POST.get('updatebtn'))
        updateob1 = Booking.objects.get(bookingid=request.POST.get('updatebtn'))
        updatedcv3 = request.POST.get('updatedcemail')

        updatedav12 = request.POST.get('updatedagentid')
        updatedv19 = request.POST.get('updatednumberofrooms')
        # updatedv20 = request.POST.get('updatedselectedrooms')

        updatedv23 = request.POST.get('updatednumberofadults')
        updatedv24 = request.POST.get('updatedproofsubmitted')
        updatedv25 = request.POST.get('updatedgrcnumber')
        updatedv26 = request.POST.get('updatedcheckin')
        updatedv27 = request.POST.get('updatedcheckout')
        updatedv28 = request.POST.get('updatedtotalamount')
        updatedv29 = request.POST.get('updatedadvanceamount')
        updatedv30 = request.POST.get('updatedbalanceamount')
        updatedv31 = request.POST.get('updatedpaymentmode')
        updatedv32 = request.POST.get('updatednumberofchildrens')
        updatedv33 = request.POST.get('updatedcheckindate')

        v200 = request.POST.get('updatedselectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        updatedv20 = str2

        tolist = updatedv20.split(',')
        for i in tolist:
            if i != '':
                print(tolist.index(i), i)
                v = room.objects.get(roomnumber=i)
                v.status = 'Booked'
                v.save()
                print(v)
        conn.commit()

        updateob1.guestemail=updatedcv3
        updateob1.agentid=updatedav12
        updateob1.no_of_rooms=updatedv19
        updateob1.room_number=updatedv20
        updateob1.no_of_adults=updatedv23
        updateob1.proof_submitted=updatedv24
        updateob1.grc_number=updatedv25
        updateob1.check_in_date=updatedv26
        updateob1.check_out_date=updatedv27
        updateob1.total_amount=updatedv28
        updateob1.advance_amount=updatedv29
        updateob1.balance_amount=updatedv30
        updateob1.paymentmode=updatedv31
        updateob1.no_of_childrens=updatedv32
        updateob1.checkindate=updatedv33
        updateob1.save()

        messages.add_message(request, messages.SUCCESS, "Booking details updated successfully")
        return render(request, 'admin/bookings.html',
                      context={ 'bkngid': bkngid, 'guestid': guestid, 'demo': ob3,
                               'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})

    return render(request, 'admin/bookings.html',context={'usersession': usersession,'roysuiteval':roysuiteval,'presuiteval':presuiteval,'exesuiteval':exesuiteval,'tensuiteval':tensuiteval, 'bkngid':bkngid,'guestid':guestid, 'demo':ob3,'bookingid': newval,'roomob1':roomob1,'roomob2':roomob2,'roomob3':roomob3,'roomob4':roomob4, 'data4':agentob, 'today':formatedDate, 'time':now,'bid':ob,'data1':obb,'data2':roomob,'data3':no})

def agentbooking(request):
    # roomval = Booking.objects.latest('room_number').room_number
    # print(roomval)
    usersession = Agent.objects.get(agentemail=request.session['mail'])

    roysuiteval=Roomcategory.objects.filter(category='Royal suite')
    presuiteval = Roomcategory.objects.filter(category='Premium suite')
    exesuiteval = Roomcategory.objects.filter(category='Executive suite')
    tensuiteval = Roomcategory.objects.filter(category='Tent camping')

    bkngid = Booking.objects.all()
    guestid = Guest.objects.all()
    agnid=usersession.agentid
    obb = Booking.objects.all().raw('select * from Registration_booking where agentid=%s',[agnid])

    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    full = 0
    exist = c.fetchone()

    if exist is None:
        full = 0
        Booking.objects.get_or_create(bookingid='SRNTYBKNG100', checkindate='March 07, 2020', room_number=1, no_of_rooms=1,
                                      guestemail='none@1',
                                      no_of_adults=1, no_of_childrens=1, proof_submitted='none', check_in_date='March 7, 2020, 11:08 p.m.',
                                      check_out_date='2020-03-06 18:30:00', grc_number=1, total_amount=1, advance_amount=1,
                                      balance_amount=1, paymentmode='none'
                                      )
    else:
        full = 1
        roomval = Booking.objects.last().room_number
        print(roomval)
        tolist = roomval.split(',')
        for index, i in enumerate(tolist):
            print(index, i)
            v = room.objects.get(roomnumber=i)
            v.status = 'Booked'
            v.save()
            print(v)
            conn.commit()

    lastid = Booking.objects.latest('bookingid').bookingid
    lastidsplt = lastid.rpartition('G')[2]
    lastidsplttoint = int(lastidsplt) + 1
    lastidsplttostr = str(lastidsplttoint)
    newval = 'SRNTYBKNG' + lastidsplttostr



    agentob=Agent.objects.all().raw('select * from Registration_agent where agentid !=%s',['SRNTYAG100'])

    roomob1 = room.objects.filter(category='Royal suite').filter(status='Available')
    roomob2 = room.objects.filter(category='Premium suite').filter(status='Available')
    roomob3 = room.objects.filter(category='Executive suite').filter(status='Available')
    roomob4 = room.objects.filter(category='Tent camping').filter(status='Available')



    tdy=datetime.date.today()
    formatedDate = tdy.strftime("%B %d, %Y")
    no = Booking.objects.filter(checkindate=formatedDate).values('room_number').count()
    roomob=room.objects.all()
    ob=Booking.objects.all()
    ob1 = Guest.objects.raw("select * from Registration_guest as a inner join Registration_booking  as b on a.guest_email=b.guestemail ORDER BY a.id DESC")
    ob3 = Booking.objects.raw("select * from Registration_agent as a ,Registration_booking  as b where a.agentid=b.agentid ")
    now = datetime.datetime.now()
    if request.method=='POST' and 'agentsearchbtn' in request.POST:
        val=request.POST.get('agentid')
        agntsearchob=Agent.objects.raw('select * from Registration_agent where agentid=%s',[val])
        return render(request, 'agent/agentbooking.html',
                      context={'bookingid': newval,'roomob1':roomob1,'roomob2':roomob2,'roomob3':roomob3,'roomob4':roomob4, 'data4':agentob, 'today':formatedDate, 'time':now,'bid':ob,'data1':ob1,'data2':roomob,'data3':no,
                               'data5':agntsearchob, })

    if request.method=='POST' and 'btn1' in request.POST:


        cv1=request.POST.get('cfname')
        cv2=request.POST.get('cphone')
        cv3=request.POST.get('cemail')
        cv4=request.POST.get('caddress')
        cv5=request.POST.get('cage')
        cv6=request.POST.get('cgender')
        cv7=request.POST.get('cmaritalstatus')
        cv8=request.POST.get('ccountry')
        cv9=request.POST.get('cstate')
        cv10=request.POST.get('cdistrict')
        cv11=request.POST.get('cpincode')

        av12=request.POST.get('agentid')
        av13=request.POST.get('agentname')
        av14=request.POST.get('agentnumber')
        # av15=request.POST.get('aaddress')
        # av16=request.POST.get('aage')
        # av17=request.POST.get('agender')
        # av18=request.POST.get('noofcustomers')

        v19=request.POST.get('numberofrooms')

        v55=request.POST.get('bkid')
        # v21=request.POST.get('roomnumber')
        # v22=request.POST.get('floornumber')
        v23=request.POST.get('numberofadults')
        v24=request.POST.get('proofsubmitted')
        v25=request.POST.get('grcnumber')
        v26=request.POST.get('checkin')
        v27=request.POST.get('checkout')

        v28=request.POST.get('totalamount')
        v29=request.POST.get('advanceamount')
        v30=request.POST.get('balanceamount')
        v31=request.POST.get('paymentmode')
        v32 = request.POST.get('numberofchildrens')
        v33=request.POST.get('checkindate')

        v200 = request.POST.get('selectedrooms')
        vvv=v200.split(',')#string to list split by commas
        vvvv=set(vvv)#list to set to avoid duplication
        vvvvv=list(vvvv)#set to lst
        str1 = ','.join(vvvvv)#list to string to save
        str2=str1.lstrip(',')#remove left comma of string
        v20 = str2
        Guest.objects.get_or_create(guestid=v55, fname=cv1,age=cv5,gender=cv6,marital_status=cv7,house_name=cv4,district=cv10,state=cv9,country=cv8,pincode=cv11,phone=cv2,guest_email=cv3)

        Booking.objects.get_or_create(bookingid=v55, agentid=av12, checkindate=v33,room_number=v20,no_of_rooms=v19,guestemail=cv3,
                                      no_of_adults=v23,no_of_childrens=v32,proof_submitted=v24,check_in_date=v26,
                                      check_out_date=v27,grc_number=v25,total_amount=v28,advance_amount=v29,balance_amount=v30,paymentmode=v31)
        roomval = Booking.objects.last().room_number
        messages.add_message(request, messages.SUCCESS, "Booking successfull")
        tolist = roomval.split(',')
        for i in tolist:
            if i!='':
                print(tolist.index(i), i)
                v = room.objects.get(roomnumber=i)
                v.status = 'Booked'
                v.save()
                print(v)
        conn.commit()
        return redirect(Recieptagent)

    if request.method == 'POST' and 'bookingsearchbtn' in request.POST:
        val=request.POST.get('bookngid')
        gustob=Guest.objects.raw('select * from Registration_guest where guestid=%s ',[val])
        bkngob = Booking.objects.raw('select * from Registration_booking where bookingid=%s ', [val])
        return render(request, 'agent/agentbooking.html',
                      context={ 'bkngob':bkngob, 'gustob':gustob, 'bkngid': bkngid, 'guestid': guestid, 'demo': ob3, 'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})
    if request.method == 'POST' and 'updatebtn' in request.POST:
        updateob= Guest.objects.get(guestid=request.POST.get('updatebtn'))
        updateob1 = Booking.objects.get(bookingid=request.POST.get('updatebtn'))
        updatedcv3 = request.POST.get('updatedcemail')

        updatedav12 = request.POST.get('updatedagentid')
        updatedv19 = request.POST.get('updatednumberofrooms')
        # updatedv20 = request.POST.get('updatedselectedrooms')

        updatedv23 = request.POST.get('updatednumberofadults')
        updatedv24 = request.POST.get('updatedproofsubmitted')
        updatedv25 = request.POST.get('updatedgrcnumber')
        updatedv26 = request.POST.get('updatedcheckin')
        updatedv27 = request.POST.get('updatedcheckout')
        updatedv28 = request.POST.get('updatedtotalamount')
        updatedv29 = request.POST.get('updatedadvanceamount')
        updatedv30 = request.POST.get('updatedbalanceamount')
        updatedv31 = request.POST.get('updatedpaymentmode')
        updatedv32 = request.POST.get('updatednumberofchildrens')
        updatedv33 = request.POST.get('updatedcheckindate')

        v200 = request.POST.get('updatedselectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        updatedv20 = str2

        tolist = updatedv20.split(',')
        for i in tolist:
            if i != '':
                print(tolist.index(i), i)
                v = room.objects.get(roomnumber=i)
                v.status = 'Booked'
                v.save()
                print(v)
        conn.commit()



        updateob1.guestemail=updatedcv3
        updateob1.agentid=updatedav12
        updateob1.no_of_rooms=updatedv19
        updateob1.room_number=updatedv20
        updateob1.no_of_adults=updatedv23
        updateob1.proof_submitted=updatedv24
        updateob1.grc_number=updatedv25
        updateob1.check_in_date=updatedv26
        updateob1.check_out_date=updatedv27
        updateob1.total_amount=updatedv28
        updateob1.advance_amount=updatedv29
        updateob1.balance_amount=updatedv30
        updateob1.paymentmode=updatedv31
        updateob1.no_of_childrens=updatedv32
        updateob1.checkindate=updatedv33
        updateob1.save()

        messages.add_message(request, messages.SUCCESS, "Booking details updated successffully")
        return render(request, 'agent/agentbooking.html',
                      context={ 'bkngid': bkngid, 'guestid': guestid, 'demo': ob3,
                               'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})

    return render(request, 'agent/agentbooking.html',context={'usersession': usersession,'roysuiteval':roysuiteval,'presuiteval':presuiteval,'exesuiteval':exesuiteval,'tensuiteval':tensuiteval, 'bkngid':bkngid,'guestid':guestid, 'demo':ob3,'bookingid': newval,'roomob1':roomob1,'roomob2':roomob2,'roomob3':roomob3,'roomob4':roomob4, 'data4':agentob, 'today':formatedDate, 'time':now,'bid':ob,'data1':obb,'data2':roomob,'data3':no})



def Reciept(request):
    obj=Booking.objects.latest('bookingid').bookingid
    ob = Booking.objects.raw("select * from Registration_booking order by id desc limit 1")
    ob1=Guest.objects.raw("select * from Registration_guest order by id desc limit 1")
    return render(request, 'Reciept.html',context={'data':obj,'data1':ob,'data2':ob1})

def Recieptadmin(request):
    obj=Booking.objects.latest('bookingid').bookingid
    ob = Booking.objects.raw("select * from Registration_booking order by id desc limit 1")
    ob1=Guest.objects.raw("select * from Registration_guest order by id desc limit 1")
    return render(request, 'admin/Reciept.html',context={'data':obj,'data1':ob,'data2':ob1})

def Recieptagent(request):
    tdy = datetime.date.today()
    formatedDate = tdy.strftime("%B %d, %Y")
    obj=Booking.objects.latest('bookingid').bookingid
    ob = Booking.objects.raw("select * from Registration_booking order by id desc limit 1")
    ob1=Guest.objects.raw("select * from Registration_guest order by id desc limit 1")
    return render(request, 'agent/Reciept.html',context={'data':obj,'data1':ob,'data2':ob1,'today':formatedDate, 'time':now,})


# def Recieptagent(request):
#     obj=Booking.objects.latest('bookingid').bookingid
#     ob = Booking.objects.raw("select * from Registration_booking order by id desc limit 1")
#     ob1=Guest.objects.raw("select * from Registration_guest order by id desc limit 1")
#     return render(request, 'agent/Reciept.html',context={'data':obj,'data1':ob,'data2':ob1})
#

def dashboard(request):
    tdy = datetime.date.today()
    ob=room.objects.filter(status='Available').count()
    ob1 = room.objects.filter(status='Booked').count()
    ob3=Guest.objects.all().count()
    ob4=Agent.objects.all().count()
    formatedDate = tdy.strftime("%B %d, %Y")
    checkintoday = Booking.objects.filter(checkindate=formatedDate).count()
    checkouttoday=Booking.objects.filter(check_out_date=tdy).count()
    usersession =  admin.objects.get(username=request.session['mail'])
    return render(request,'dashboard.html',{'usersession':usersession,'data3':checkintoday,'data4':checkouttoday,'data5':ob,'data6':ob1,'data7':ob3,'data8':ob4})

def login(request):
    if request.method=="POST":
        user=request.POST.get('uname')
        pswd=request.POST.get('pswd')
        if admin.objects.all().filter(username=user,password=pswd).exists():
            ob1 = admin.objects.get(username=user)
            request.session['mail'] = user
            if ob1.type=='user':
                return redirect(dashboard)
            elif ob1.type=='superuser':
                return redirect(admindashboard)
            else:
                return redirect(login)
        elif Agent.objects.all().filter(agentid=pswd,agentemail=user).exists():
            request.session['mail'] = user
            return redirect(agentview)
        else:
            return render(request, 'login.html', {'msg': 'Invalid username or password'})
    return render(request,'login.html')


def logout(request):
    request.session['mail'] = {}
    return redirect(login)


def rooms(request):
    usersession =  admin.objects.get(username=request.session['mail'])
    ob2=Roomtype.objects.all()
    ob3=Roomcategory.objects.all()
    ob4=Floor.objects.all()

    ob1 = room.objects.raw('select * from Registration_room where id >1')
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    full = 0
    exist = c.fetchone()

    if exist is None:
        full = 0
        room.objects.get_or_create(roomtype='none',roomnumber=100,rate=000,floornumber=000,category='none')
    else:
        full = 1
    lastval = room.objects.latest('roomnumber').roomnumber
    newval = lastval + 1

    if request.method=='POST' and 'btn1' in request.POST:
        v1=request.POST.get('roomno')
        v2=request.POST.get('floorno')
        v3=request.POST.get('roomcategory')
        # v4=request.POST.get('roomtype')
        # v5=request.POST.get('rate')
        room.objects.get_or_create(roomnumber=v1,floornumber=v2,category=v3)
        messages.add_message(request, messages.SUCCESS, "Successfully added new rooms")
        return redirect(rooms)
    if request.method == 'POST' and 'btn2' in request.POST:
        val1=request.POST.get('selectedroomno')
        val2=room.objects.raw('select * from Registration_room where roomnumber=%s',[val1])
        return render(request, 'admin/rooms.html', {'data1': ob1, 'data2': ob2, 'data3': ob3, 'data4': ob4, 'data5': newval, 'data6': val2})
    if request.method == 'POST' and 'btn3' in request.POST:
        roomno=request.POST.get('roomno')
        category = request.POST.get('category')
        # rate = request.POST.get('rate')
        floorno = request.POST.get('floorno')
        # roomtype = request.POST.get('roomtype')
        ob=room.objects.get(roomnumber=request.POST.get('btn3'))
        ob.roomnumber=roomno
        ob.category=category
        # ob.rate=rate
        ob.floornumber=floorno
        # ob.roomtype=roomtype
        ob.save()
        messages.add_message(request, messages.SUCCESS, "Successfully updated room details")
        return redirect(rooms)
    if request.method == 'POST' and 'btn4' in request.POST:
        room.objects.get(roomnumber=request.POST.get('btn4')).delete()
        messages.add_message(request, messages.SUCCESS, "One room deleted from your home !")
        return redirect(rooms)
    return render(request, 'admin/rooms.html', {'usersession':usersession, 'data1':ob1, 'data2':ob2, 'data3':ob3, 'data4':ob4, 'data5':newval})







def agent(request):
    usersession = admin.objects.get(username=request.session['mail'])
    ob1=Agent.objects.raw('select * from Registration_agent where id >1')
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    full = 0
    exist = c.fetchone()

    if exist is None:
        full = 0
        Agent.objects.get_or_create(agentid='SRNTYAG100',agentemail='s@1',aget_phone=55555,address='demo')
    else:
        full = 1
    lastid=Agent.objects.latest('agentid').agentid
    lastidsplt=lastid.rpartition('G')[2]
    lastidsplttoint=int(lastidsplt)+1
    lastidsplttostr=str(lastidsplttoint)
    newval='SRNTYAG'+lastidsplttostr
    if request.method=='POST' and 'btn1' in request.POST:
        agid=request.POST.get('agentid')
        agname=request.POST.get('agentname')
        agaddress=request.POST.get('agentaddress')
        agcontactno=request.POST.get('agentcontactno')
        agemial=request.POST.get('agentemailid')
        Agent.objects.get_or_create(agentid=agid,agent_name=agname,address=agaddress,aget_phone=agcontactno,agentemail=agemial)
        messages.add_message(request, messages.SUCCESS, "Successfully created new agent")
        return redirect(agent)
    if request.method == 'POST' and 'btn2' in request.POST:
        slctdagentid=request.POST.get('selectedagentid')
        ob2=Agent.objects.raw('select * from Registration_agent where agentid = %s',[slctdagentid])
        return render(request, 'agent.html', {'agentid': newval, 'data1': ob1, 'data2': ob2})

    if request.method == 'POST' and 'btn3' in request.POST:
        agid = request.POST.get('updatedid')
        agname = request.POST.get('updatedname')
        agaddress = request.POST.get('updatedaddress')
        agcontactno = request.POST.get('updatedphone')
        agemial = request.POST.get('updatedemail')
        ob=Agent.objects.get(agentid=request.POST.get('btn3'))
        ob.agent_name=agname
        ob.address=agaddress
        ob.aget_phone=agcontactno
        ob.agentemail=agemial
        ob.save()
        messages.add_message(request, messages.SUCCESS, "Agent details updated successfully")
        return redirect(agent)
    if request.method == 'POST' and 'btn4' in request.POST:
        Agent.objects.get(agentid=request.POST.get('btn4')).delete()
        messages.add_message(request, messages.SUCCESS, "Agent deleted successfully")
        return redirect(agent)
    return render(request,'agent.html',{'usersession':usersession,'agentid':newval, 'data1':ob1})



def agentadmin(request):
    usersession = admin.objects.get(username=request.session['mail'])
    ob1=Agent.objects.raw('select * from Registration_agent where id >1')
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    full = 0
    exist = c.fetchone()

    if exist is None:
        full = 0
        Agent.objects.get_or_create(agentid='SRNTYAG100',agentemail='s@1',aget_phone=55555,address='demo')
    else:
        full = 1
    lastid=Agent.objects.latest('agentid').agentid
    lastidsplt=lastid.rpartition('G')[2]
    lastidsplttoint=int(lastidsplt)+1
    lastidsplttostr=str(lastidsplttoint)
    newval='SRNTYAG'+lastidsplttostr
    if request.method=='POST' and 'btn1' in request.POST:
        agid=request.POST.get('agentid')
        agname=request.POST.get('agentname')
        agaddress=request.POST.get('agentaddress')
        agcontactno=request.POST.get('agentcontactno')
        agemial=request.POST.get('agentemailid')
        Agent.objects.get_or_create(agentid=agid,agent_name=agname,address=agaddress,aget_phone=agcontactno,agentemail=agemial)
        messages.add_message(request, messages.SUCCESS, "Successfully created new agent")
        return render(request, 'admin/agent.html',)
    if request.method == 'POST' and 'btn2' in request.POST:
        slctdagentid=request.POST.get('selectedagentid')
        ob2=Agent.objects.raw('select * from Registration_agent where agentid = %s',[slctdagentid])
        return render(request, 'admin/agent.html', {'agentid': newval, 'data1': ob1, 'data2': ob2})

    if request.method == 'POST' and 'btn3' in request.POST:
        agid = request.POST.get('updatedid')
        agname = request.POST.get('updatedname')
        agaddress = request.POST.get('updatedaddress')
        agcontactno = request.POST.get('updatedphone')
        agemial = request.POST.get('updatedemail')
        ob=Agent.objects.get(agentid=request.POST.get('btn3'))
        ob.agent_name=agname
        ob.address=agaddress
        ob.aget_phone=agcontactno
        ob.agentemail=agemial
        ob.save()
        messages.add_message(request, messages.SUCCESS, "Agent details updated successfully")
        return render(request,'admin/agent.html',{'agentid':newval, 'data1':ob1})
    if request.method == 'POST' and 'btn4' in request.POST:
        Agent.objects.get(agentid=request.POST.get('btn4')).delete()
        messages.add_message(request, messages.SUCCESS, "One agent deleted from your agent list !")
        return redirect(agent)
    return render(request,'admin/agent.html',{'usersession':usersession,'agentid':newval, 'data1':ob1})



def more(request):
    usersession = admin.objects.get(username=request.session['mail'])
    flrob=Floor.objects.all()
    rmctgryob=Roomcategory.objects.all()
    rmtypeob = Roomtype.objects.all()

    if request.method=='POST' and 'btn11' in request.POST:
        flrno=request.POST.get('floorno')
        norooms=request.POST.get('noofrooms')
        Floor.objects.get_or_create(floorno=flrno,noofrooms=norooms)
        messages.add_message(request, messages.SUCCESS, "New floor added successfully")
        return redirect(more)
    if request.method=='POST' and 'btn12' in request.POST:
        floor=request.POST.get('selectfloor')
        ob1=Floor.objects.raw('select * from Registration_floor where floorno = %s',[floor])
        return render(request, 'admin/more.html', {'data11':ob1})
    if request.method=='POST' and 'btn13' in request.POST:
        flrno = request.POST.get('floorno')
        norooms = request.POST.get('norooms')
        ob1=Floor.objects.get(floorno=request.POST.get('btn13'))
        ob1.floorno=flrno
        ob1.noofrooms=norooms
        ob1.save()
        messages.add_message(request, messages.SUCCESS, "Floor details updated successfully")
        return redirect(more)
    if request.method == 'POST' and 'btn14' in request.POST:
        Floor.objects.get(id=request.POST.get('btn14')).delete()
        messages.add_message(request, messages.SUCCESS, "One floor deleted form your floor list")
        return redirect(more)


    if request.method=='POST' and 'btn21' in request.POST:
        category=request.POST.get('category')
        ac = request.POST.get('ac')
        wifi = request.POST.get('wifi')
        beverage = request.POST.get('beverage')
        breakfast = request.POST.get('breakfast')
        area = request.POST.get('area')
        rate = request.POST.get('rate')
        Roomcategory.objects.get_or_create(category=category,ac=ac,wifi=wifi,beverage=beverage,
                                           breakfast=breakfast,area=area,rate=rate)
        messages.add_message(request, messages.SUCCESS, "Successfully added new room category")
        return redirect(more)
    if request.method=='POST' and 'btn22' in request.POST:
        roomcat=request.POST.get('selectedroomcategory')
        ob=Roomcategory.objects.raw('select * from Registration_roomcategory where category=%s',[roomcat])
        return render(request, 'admin/more.html', {'data3':ob})
    if request.method == 'POST' and 'btn23' in request.POST:
        category = request.POST.get('category')
        area = request.POST.get('area')
        wifi = request.POST.get('wifi')
        ac = request.POST.get('ac')
        rate = request.POST.get('rate')
        beverage = request.POST.get('beverage')
        breakfast = request.POST.get('breakfast')
        ob=Roomcategory.objects.get(category=request.POST.get('btn23'))
        ob.category=category
        ob.area=area
        ob.wifi=wifi
        ob.ac=ac
        ob.rate=rate
        ob.beverage=beverage
        ob.breakfast=breakfast
        ob.save()
        messages.add_message(request, messages.SUCCESS, "Room details updated successfully")
        return redirect(more)
    if request.method == 'POST' and 'btn24' in request.POST:
        Roomcategory.objects.get(category=request.POST.get('btn24')).delete()
        messages.add_message(request, messages.SUCCESS, "One category deleted form your room category list")
        return redirect(more)


    if request.method=='POST' and 'btn31' in request.POST:
        roomtype=request.POST.get('roomtype')
        rate = request.POST.get('rate')
        noofbed = request.POST.get('noofbed')
        area = request.POST.get('area')
        Roomtype.objects.get_or_create(type=roomtype,rate=rate,noofbeds=noofbed,area=area)
        messages.add_message(request, messages.SUCCESS, "Successfully created new roomtype")
        return redirect(more)
    if request.method == 'POST' and 'btn32' in request.POST:
        selectedtype=request.POST.get('selectedtype')
        typeob=Roomtype.objects.raw('select * from Registration_roomtype where type=%s',[selectedtype])
        return render(request, 'admin/more.html', {'data1': flrob, 'data2': rmctgryob, 'data4': rmtypeob, 'data5':typeob})
    if request.method == 'POST' and 'btn33' in request.POST:
        roomtype=request.POST.get('type')
        rate = request.POST.get('rate')
        noofbeds = request.POST.get('noofbeds')
        area = request.POST.get('area')
        ob=Roomtype.objects.get(type=request.POST.get('btn33'))
        ob.type=roomtype
        ob.rate=rate
        ob.noofbeds=noofbeds
        ob.area=area
        ob.save()
        messages.add_message(request, messages.SUCCESS, "Room details updated successfully")
        return redirect(more)
    if request.method == 'POST' and 'btn34' in request.POST:
        Roomtype.objects.get(type=request.POST.get('btn34')).delete()
        messages.add_message(request, messages.SUCCESS, "One room type deleted from your room type list !")
    return render(request, 'admin/more.html', {'usersession':usersession,'data1':flrob, 'data2':rmctgryob, 'data4':rmtypeob})

def guest(request):
    usersession = admin.objects.get(username=request.session['mail'])
    ob1=Guest.objects.all()
    if request.method == 'POST' and 'btn1' in request.POST:
        slctdagentid = request.POST.get('selectedguestid')
        ob2 = Guest.objects.raw('select * from Registration_guest where guestid = %s', [slctdagentid])
        return render(request, 'guest.html', context={'data1': ob1,'data2':ob2})
    if request.method == 'POST' and 'btn2' in request.POST:
        ob3=Guest.objects.get(guestid=request.POST.get('btn2'))
        v1=request.POST.get('updatedname')
        v2=request.POST.get('updatedage')
        v3=request.POST.get('updatedgender')
        v4=request.POST.get('updatedmaritalstatus')
        v5=request.POST.get('updatedaddress')
        v6=request.POST.get('updatedcountry')
        v7=request.POST.get('updateddistrict')
        v8=request.POST.get('updatedstate')
        v9=request.POST.get('updatedpincode')
        v10=request.POST.get('updatedphone')
        v11=request.POST.get('updatedemail')
        v12=request.POST.get('updatedid')
        ob3.fname=v1
        ob3.age=v2
        ob3.gender=v3
        ob3.marital_status=v4
        ob3.house_name=v5
        ob3.country=v6
        ob3.district=v7
        ob3.state=v8
        ob3.pincode=v9
        ob3.phone=v10
        ob3.guest_email=v11
        ob3.guestid=v12
        ob3.save()
        messages.add_message(request, messages.SUCCESS, "Guest details updated successfully")
        return render(request, 'guest.html', context={'data1': ob1})
    if request.method == 'POST' and 'btn3' in request.POST:
        Guest.objects.get(guestid=request.POST.get('btn3')).delete()
        messages.add_message(request, messages.SUCCESS, "Delete one guest details")
        return render(request, 'guest.html', context={'data1': ob1})
    return render(request,'guest.html',context={'usersession':usersession,'data1':ob1,})


def guestadmin(request):
    usersession = admin.objects.get(username=request.session['mail'])
    ob1=Guest.objects.all()
    if request.method == 'POST' and 'btn1' in request.POST:
        slctdagentid = request.POST.get('selectedguestid')
        ob2 = Guest.objects.raw('select * from Registration_guest where guestid = %s', [slctdagentid])
        return render(request, 'admin/guest.html', context={'data1': ob1,'data2':ob2})
    if request.method == 'POST' and 'btn2' in request.POST:
        ob3=Guest.objects.get(guestid=request.POST.get('btn2'))
        v1=request.POST.get('updatedname')
        v2=request.POST.get('updatedage')
        v3=request.POST.get('updatedgender')
        v4=request.POST.get('updatedmaritalstatus')
        v5=request.POST.get('updatedaddress')
        v6=request.POST.get('updatedcountry')
        v7=request.POST.get('updateddistrict')
        v8=request.POST.get('updatedstate')
        v9=request.POST.get('updatedpincode')
        v10=request.POST.get('updatedphone')
        v11=request.POST.get('updatedemail')
        v12=request.POST.get('updatedid')
        ob3.fname=v1
        ob3.age=v2
        ob3.gender=v3
        ob3.marital_status=v4
        ob3.house_name=v5
        ob3.country=v6
        ob3.district=v7
        ob3.state=v8
        ob3.pincode=v9
        ob3.phone=v10
        ob3.guest_email=v11
        ob3.guestid=v12
        ob3.save()
        messages.add_message(request, messages.SUCCESS, "Guest details updated successfully")
        return render(request, 'admin/guest.html', context={'data1': ob1})
    if request.method == 'POST' and 'btn3' in request.POST:
        Guest.objects.get(guestid=request.POST.get('btn3')).delete()
        messages.add_message(request, messages.SUCCESS, "One guest deleted from your guest list !")
        return render(request, 'admin/guest.html', context={'data1': ob1})
    return render(request,'admin/guest.html',context={'usersession':usersession,'data1':ob1,})




def settings(request):
    usersession = admin.objects.get(username=request.session['mail'])
    ob1 = admin.objects.all()
    if request.method=='POST' and 'btn1' in request.POST:
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        confirmpswd=request.POST.get('confirmpassword')
        if admin.objects.filter(username=uname).exists():
            messages.add_message(request, messages.SUCCESS, "Username already exists")
            return render(request, 'admin/user.html')
        if pswd==confirmpswd:
            if admin.objects.filter(username=uname).exists():
                messages.add_message(request, messages.SUCCESS, "Username already exists")
                return render(request, 'admin/user.html')
            else:
                admin.objects.get_or_create(username=uname, password=pswd)
                messages.add_message(request, messages.SUCCESS, "User created successfully")
                return render(request, 'admin/user.html')
        else:
            return render(request, 'admin/user.html', {'msg': 'Password mistmatch'})
    if request.method == 'POST' and 'btn2' in request.POST:
        admin.objects.get(username=request.POST.get('btn2')).delete()
        messages.add_message(request, messages.SUCCESS, "One user deleted from your user list !")
        return render(request, 'admin/user.html', {'usersession':usersession,'data1': ob1})
    return  render(request, 'admin/user.html',{'usersession':usersession,'data1':ob1})

def admindashboard(request):
    tdy = datetime.date.today()
    ob=room.objects.filter(status='Available').count()
    ob1 = room.objects.filter(status='Booked').count()
    ob3=Guest.objects.all().count()
    ob4=Agent.objects.all().count()
    formatedDate = tdy.strftime("%B %d, %Y")
    checkintoday = Booking.objects.filter(checkindate=formatedDate).count()
    checkouttoday=Booking.objects.filter(check_out_date=tdy).count()
    usersession =  admin.objects.get(username=request.session['mail'])
    return render(request,'admin/dashboard.html',{'usersession':usersession,'data3':checkintoday,'data4':checkouttoday,'data5':ob,'data6':ob1,'data7':ob3,'data8':ob4})


def changepassword(request):
    username = admin.objects.get(username=request.session['mail'])
    if request.method == 'POST':
        if request.method=='POST' and 'btn1' in request.POST:
            currentusername=request.POST.get('currentusername')
            newusername=request.POST.get('newusername')
            confirmusername=request.POST.get('confirmusername')
            user = request.POST.get('userusername')
            if currentusername==user:
                if newusername==confirmusername:
                    username.username=newusername
                    username.save()
                    request.session['mail'] = newusername
                    messages.add_message(request, messages.SUCCESS, "Username changed successfully")
                    return render(request, 'admin/settings.html')
                else:
                    return render(request, 'admin/settings.html', {'msg': 'Username mistmatch'})
            else:
                return render(request, 'admin/settings.html',{'msg1': 'Enter your current username'})

        if request.method=='POST' and 'btn2' in request.POST:
            print('haii')
            currentpassword=request.POST.get('currentpassword')
            newpassword=request.POST.get('newpassword')
            confirmpassword=request.POST.get('confirmpassword')
            user = request.POST.get('userpassword')
            if currentpassword==user:
                if newpassword==confirmpassword:
                    username.password=newpassword
                    username.save()
                    # request.session['mail'] = newpassword
                    messages.add_message(request, messages.SUCCESS, "Password changed successfully")
                    return render(request, 'admin/settings.html')
                else:
                    return render(request, 'admin/settings.html', {'msg3': 'Password mistmatch'})
            else:
                return render(request, 'admin/settings.html',{'msg2': 'Enter your current password'})
    return render(request,'admin/settings.html',{'usersession':username})



def usersettings(request):
    username = admin.objects.get(username=request.session['mail'])
    if request.method == 'POST':
        if request.method=='POST' and 'btn1' in request.POST:
            currentusername=request.POST.get('currentusername')
            newusername=request.POST.get('newusername')
            confirmusername=request.POST.get('confirmusername')
            user = request.POST.get('userusername')
            if currentusername==user:
                if newusername==confirmusername:
                    username.username=newusername
                    username.save()
                    request.session['mail'] = newusername
                    messages.add_message(request, messages.SUCCESS, "Username changed successfully")
                    return render(request, 'settings.html')
                else:
                    return render(request, 'settings.html', {'msg': 'Username mistmatch'})
            else:
                return render(request, 'settings.html',{'msg1': 'Enter your current username'})

        if request.method=='POST' and 'btn2' in request.POST:
            currentpassword=request.POST.get('currentpassword')
            newpassword=request.POST.get('newpassword')
            confirmpassword=request.POST.get('confirmpassword')
            user = request.POST.get('userpassword')
            if currentpassword==user:
                if newpassword==confirmpassword:
                    username.password=newpassword
                    username.save()

                    messages.add_message(request, messages.SUCCESS, "Password changed successfully")
                    return render(request, 'settings.html')
                else:
                    return render(request, 'settings.html', {'msg3': 'Password mistmatch'})
            else:
                return render(request, 'admin/settings.html',{'msg2': 'Enter your current password'})
    return render(request,'settings.html',{'usersession':username})


def managerooms(request):
    username = admin.objects.get(username=request.session['mail'])
    # ob1 = room.objects.filter(status='Booked').count()
    # ob=room.objects.all('select * from Registration_room inner join Registration_booking where ')
    ob1 = room.objects.raw('select * from Registration_room where status=%s',['Booked'])
    ob2 = Booking.objects.all().raw('select * from Registration_booking where id>42 order by id desc ')
    ob3 = room.objects.raw('select * from Registration_room where status=%s', ['Vacate'])
    if request.method=='POST' and 'vacate' in request.POST:
        ob = room.objects.get(roomnumber=request.POST.get('vacate'))
        ob.status = 'Vacate'
        ob.save()
    if request.method=='POST' and 'availablebtn' in request.POST:
        ob=room.objects.get(roomnumber=request.POST.get('availablebtn'))
        ob.status='Available'
        ob.save()

    return render(request, 'managerooms.html',{'usersession':username,'data1':ob1,'data2':ob2,'data3':ob3})


def manageroomsadmin(request):
    username = admin.objects.get(username=request.session['mail'])
    ob1 = room.objects.raw('select * from Registration_room where status=%s', ['Booked'])
    ob2 = Booking.objects.all().raw('select * from Registration_booking where id>42 order by id desc ')
    ob3 = room.objects.raw('select * from Registration_room where status=%s', ['Vacate'])
    if request.method == 'POST' and 'vacate' in request.POST:
        ob = room.objects.get(roomnumber=request.POST.get('vacate'))
        ob.status = 'Vacate'
        ob.save()
    if request.method == 'POST' and 'availablebtn' in request.POST:
        ob = room.objects.get(roomnumber=request.POST.get('availablebtn'))
        ob.status = 'Available'
        ob.save()
    return render(request,'admin/manageroomsadmin.html',{'usersession':username,'data1':ob1,'data2':ob2,'data3':ob3})


def agentview(request):
    usersession = Agent.objects.get(agentemail=request.session['mail'])
    return render(request,'agent/agent.html')

def allbookings(request):
    usersession = Agent.objects.get(agentemail=request.session['mail'])

    roysuiteval = Roomcategory.objects.filter(category='Royal suite')
    presuiteval = Roomcategory.objects.filter(category='Premium suite')
    exesuiteval = Roomcategory.objects.filter(category='Executive suite')
    tensuiteval = Roomcategory.objects.filter(category='Tent camping')

    bkngid = Booking.objects.all()
    guestid = Guest.objects.all()
    agnid = usersession.agentid
    obb = Booking.objects.all().raw('select * from Registration_booking where agentid=%s', [agnid])

    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    full = 0
    exist = c.fetchone()

    if exist is None:
        full = 0
        Booking.objects.get_or_create(bookingid='SRNTYBKNG100', checkindate='March 07, 2020', room_number=1,
                                      no_of_rooms=1,
                                      guestemail='none@1',
                                      no_of_adults=1, no_of_childrens=1, proof_submitted='none',
                                      check_in_date='March 7, 2020, 11:08 p.m.',
                                      check_out_date='2020-03-06 18:30:00', grc_number=1, total_amount=1,
                                      advance_amount=1,
                                      balance_amount=1, paymentmode='none'
                                      )
    else:
        full = 1
        roomval = Booking.objects.last().room_number
        print(roomval)
        tolist = roomval.split(',')
        for index, i in enumerate(tolist):
            print(index, i)
            v = room.objects.get(roomnumber=i)
            v.status = 'Booked'
            v.save()
            print(v)
            conn.commit()

    lastid = Booking.objects.latest('bookingid').bookingid
    lastidsplt = lastid.rpartition('G')[2]
    lastidsplttoint = int(lastidsplt) + 1
    lastidsplttostr = str(lastidsplttoint)
    newval = 'SRNTYBKNG' + lastidsplttostr

    agentob = Agent.objects.all().raw('select * from Registration_agent where agentid !=%s', ['SRNTYAG100'])

    roomob1 = room.objects.filter(category='Royal suite').filter(status='Available')
    roomob2 = room.objects.filter(category='Premium suite').filter(status='Available')
    roomob3 = room.objects.filter(category='Executive suite').filter(status='Available')
    roomob4 = room.objects.filter(category='Tent camping').filter(status='Available')

    tdy = datetime.date.today()
    formatedDate = tdy.strftime("%B %d, %Y")
    no = Booking.objects.filter(checkindate=formatedDate).values('room_number').count()
    roomob = room.objects.all()
    ob = Booking.objects.all()
    ob1 = Guest.objects.raw(
        "select * from Registration_guest as a inner join Registration_booking  as b on a.guest_email=b.guestemail ORDER BY a.id DESC")
    ob3 = Booking.objects.raw(
        "select * from Registration_agent as a ,Registration_booking  as b where a.agentid=b.agentid ")
    now = datetime.datetime.now()
    # if request.method == 'POST' and 'agentsearchbtn' in request.POST:
    #     val = request.POST.get('agentid')
    #     agntsearchob = Agent.objects.raw('select * from Registration_agent where agentid=%s', [val])
    #     return render(request, 'agent/agentbooking.html',
    #                   context={'bookingid': newval, 'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3,
    #                            'roomob4': roomob4, 'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob,
    #                            'data1': ob1, 'data2': roomob, 'data3': no,
    #                            'data5': agntsearchob, })
    #
    # if request.method == 'POST' and 'btn1' in request.POST:
    #
    #     cv1 = request.POST.get('cfname')
    #     cv2 = request.POST.get('cphone')
    #     cv3 = request.POST.get('cemail')
    #     cv4 = request.POST.get('caddress')
    #     cv5 = request.POST.get('cage')
    #     cv6 = request.POST.get('cgender')
    #     cv7 = request.POST.get('cmaritalstatus')
    #     cv8 = request.POST.get('ccountry')
    #     cv9 = request.POST.get('cstate')
    #     cv10 = request.POST.get('cdistrict')
    #     cv11 = request.POST.get('cpincode')
    #
    #     av12 = request.POST.get('agentid')
    #     av13 = request.POST.get('agentname')
    #     av14 = request.POST.get('agentnumber')
    #     # av15=request.POST.get('aaddress')
    #     # av16=request.POST.get('aage')
    #     # av17=request.POST.get('agender')
    #     # av18=request.POST.get('noofcustomers')
    #
    #     v19 = request.POST.get('numberofrooms')
    #
    #     v55 = request.POST.get('bkid')
    #     # v21=request.POST.get('roomnumber')
    #     # v22=request.POST.get('floornumber')
    #     v23 = request.POST.get('numberofadults')
    #     v24 = request.POST.get('proofsubmitted')
    #     v25 = request.POST.get('grcnumber')
    #     v26 = request.POST.get('checkin')
    #     v27 = request.POST.get('checkout')
    #
    #     v28 = request.POST.get('totalamount')
    #     v29 = request.POST.get('advanceamount')
    #     v30 = request.POST.get('balanceamount')
    #     v31 = request.POST.get('paymentmode')
    #     v32 = request.POST.get('numberofchildrens')
    #     v33 = request.POST.get('checkindate')
    #
        # v200 = request.POST.get('selectedrooms')
        # vvv = v200.split(',')  # string to list split by commas
        # vvvv = set(vvv)  # list to set to avoid duplication
        # vvvvv = list(vvvv)  # set to lst
        # str1 = ','.join(vvvvv)  # list to string to save
        # str2 = str1.lstrip(',')  # remove left comma of string
        # v20 = str2
    #     Guest.objects.get_or_create(guestid=v55, fname=cv1, age=cv5, gender=cv6, marital_status=cv7, house_name=cv4,
    #                                 district=cv10, state=cv9, country=cv8, pincode=cv11, phone=cv2, guest_email=cv3)
    #
    #     Booking.objects.get_or_create(bookingid=v55, agentid=av12, checkindate=v33, room_number=v20, no_of_rooms=v19,
    #                                   guestemail=cv3,
    #                                   no_of_adults=v23, no_of_childrens=v32, proof_submitted=v24, check_in_date=v26,
    #                                   check_out_date=v27, grc_number=v25, total_amount=v28, advance_amount=v29,
    #                                   balance_amount=v30, paymentmode=v31)
    #     roomval = Booking.objects.last().room_number
    #     messages.add_message(request, messages.SUCCESS, "Booking successfull")
    #     tolist = roomval.split(',')
    #     for i in tolist:
    #         if i != '':
    #             print(tolist.index(i), i)
    #             v = room.objects.get(roomnumber=i)
    #             v.status = 'Booked'
    #             v.save()
    #             print(v)
    #     conn.commit()
    #     return redirect(Recieptagent)

    if request.method == 'POST' and 'bookingsearchbtn' in request.POST:
        val = request.POST.get('bookngid')
        gustob = Guest.objects.raw('select * from Registration_guest where guestid=%s ', [val])
        bkngob = Booking.objects.raw('select * from Registration_booking where bookingid=%s ', [val])
        return render(request, 'agent/allbookings.html',
                      context={'bkngob': bkngob, 'gustob': gustob, 'bkngid': bkngid, 'guestid': guestid, 'demo': ob3,
                               'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})
    if request.method == 'POST' and 'updatebtn' in request.POST:
        updateob = Guest.objects.get(guestid=request.POST.get('updatebtn'))
        updateob1 = Booking.objects.get(bookingid=request.POST.get('updatebtn'))
        updatedcv3 = request.POST.get('updatedcemail')

        updatedav12 = request.POST.get('updatedagentid')
        updatedv19 = request.POST.get('updatednumberofrooms')
        # updatedv20 = request.POST.get('updatedselectedrooms')



        updatedv23 = request.POST.get('updatednumberofadults')
        updatedv24 = request.POST.get('updatedproofsubmitted')
        updatedv25 = request.POST.get('updatedgrcnumber')
        updatedv26 = request.POST.get('updatedcheckin')
        updatedv27 = request.POST.get('updatedcheckout')
        updatedv28 = request.POST.get('updatedtotalamount')
        updatedv29 = request.POST.get('updatedadvanceamount')
        updatedv30 = request.POST.get('updatedbalanceamount')
        updatedv31 = request.POST.get('updatedpaymentmode')
        updatedv32 = request.POST.get('updatednumberofchildrens')
        updatedv33 = request.POST.get('updatedcheckindate')

        v200 = request.POST.get('updatedselectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        updatedv20 = str2

        tolist = updatedv20.split(',')
        for i in tolist:
            if i != '':
                print(tolist.index(i), i)
                v = room.objects.get(roomnumber=i)
                v.status = 'Booked'
                v.save()
                print(v)
        conn.commit()




        updateob1.guestemail = updatedcv3
        updateob1.agentid = updatedav12
        updateob1.no_of_rooms = updatedv19
        updateob1.room_number = updatedv20
        updateob1.no_of_adults = updatedv23
        updateob1.proof_submitted = updatedv24
        updateob1.grc_number = updatedv25
        updateob1.check_in_date = updatedv26
        updateob1.check_out_date = updatedv27
        updateob1.total_amount = updatedv28
        updateob1.advance_amount = updatedv29
        updateob1.balance_amount = updatedv30
        updateob1.paymentmode = updatedv31
        updateob1.no_of_childrens = updatedv32
        updateob1.checkindate = updatedv33
        updateob1.save()

        messages.add_message(request, messages.SUCCESS, "Booking details updated successffully")
        return render(request, 'agent/allbookings.html',
                      context={'bkngid': bkngid, 'guestid': guestid, 'demo': ob3,
                               'bookingid': newval,
                               'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3, 'roomob4': roomob4,
                               'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob, 'data1': obb,
                               'data2': roomob, 'data3': no})

    return render(request, 'agent/allbookings.html',
                  context={'usersession': usersession, 'roysuiteval': roysuiteval, 'presuiteval': presuiteval,
                           'exesuiteval': exesuiteval, 'tensuiteval': tensuiteval, 'bkngid': bkngid, 'guestid': guestid,
                           'demo': ob3, 'bookingid': newval, 'roomob1': roomob1, 'roomob2': roomob2, 'roomob3': roomob3,
                           'roomob4': roomob4, 'data4': agentob, 'today': formatedDate, 'time': now, 'bid': ob,
                           'data1': obb, 'data2': roomob, 'data3': no})



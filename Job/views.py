
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Job, Tafs, Location, Expenses
import datetime, re
from django.shortcuts import redirect

fill_out = True
@login_required(login_url='/accounts/login/')
def create_job(request):
    print(request.POST)
    template = loader.get_template('Job/Add.html')
    global fill_out
    if 'fill_out' in request.GET:
        fill_out = True
    else:
        fill_out = False
    if 'fill_out_info' in request.POST:
        if len(request.POST['end_date']) == 0:
            end_date = None
        else:
            end_date = request.POST['end_date']
        if len(request.POST['receipt_date']) == 0:
            receipt_date = None
        else:
            receipt_date = request.POST['receipt_date']
        taf = Tafs.objects.filter(invoice_number=request.POST['invoice'], reference_number=request.POST['reference'],
                                  amount=request.POST['amount'], reserves=request.POST['reserves'], debtor=request.POST['debtor'])
        expenses = Expenses.objects.filter(hotel=request.POST['hotel'], food=request.POST['food'],
                                           gas=request.POST['gas'], other=request.POST['other'])
        start_loc = Location.objects.filter(street=request.POST['start_street'], city=request.POST['start_city'],
                                            state=request.POST['start_state'], zipcode=request.POST['start_zip'])
        pickup_loc = Location.objects.filter(street=request.POST['pickup_street'], city=request.POST['pickup_city'],
                                            state=request.POST['pickup_state'], zipcode=request.POST['pickup_zip'])
        dropoff_loc = Location.objects.filter(street=request.POST['dropoff_street'], city=request.POST['dropoff_city'],
                                            state=request.POST['dropoff_state'], zipcode=request.POST['dropoff_zip'])
        if len(expenses) == 0:
            expenses = Expenses(hotel=request.POST['hotel'], food=request.POST['food'],
                                           gas=request.POST['gas'], other=request.POST['other'])
            expenses.save()
            expenses = [expenses]
            print("expenses: ", expenses)
        if len(start_loc) == 0:
            start_loc = Location(street=request.POST['start_street'], city=request.POST['start_city'],
                                            state=request.POST['start_state'], zipcode=request.POST['start_zip'])
            start_loc.save()
            start_loc = [start_loc]
            print("start_loc: ", start_loc)
        if len(pickup_loc) == 0:
            pickup_loc = Location(street=request.POST['pickup_street'], city=request.POST['pickup_city'],
                                            state=request.POST['pickup_state'], zipcode=request.POST['pickup_zip'])
            pickup_loc.save()
            pickup_loc = [pickup_loc]
            print("pickup_loc: ", pickup_loc)
        if len(dropoff_loc) == 0:
            dropoff_loc = Location(street=request.POST['dropoff_street'], city=request.POST['dropoff_city'],
                                            state=request.POST['dropoff_state'], zipcode=request.POST['dropoff_zip'])
            dropoff_loc.save()
            dropoff_loc = [dropoff_loc]
            print("dropoff_loc: ", dropoff_loc)
        if len(taf) == 0:
            taf = Tafs(invoice_number=request.POST['invoice'], reference_number=request.POST['reference'],
                                  amount=request.POST['amount'], reserves=request.POST['reserves'], debtor=request.POST['debtor'])
            taf.save()
            taf = [taf]
            print("taf ", taf)
        job = Job(comp_name=request.POST['company'], rpm=request.POST['rpm'], distance=request.POST['distance'],
                           taf=taf[0], start_date=request.POST['start_date'], end_date=end_date,
                           receipt_date=receipt_date, notes=request.POST['notes'], expenses=expenses[0],
                           start_loc=start_loc[0], pickup_loc=pickup_loc[0], dropoff_loc=dropoff_loc[0])
        job.save()
        print("submit button hit")
    context = {'fill_out': fill_out}
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from .models import *

# Create your views here.


# the main vue
def reservations(request):
    '''
    getting all reservation and by date of creation in the table
    '''
    All_reservations = Reservation.objects.all().order_by('rental')
    for key, value in enumerate(All_reservations):
        if key == 0 or All_reservations[key-1].rental != value.rental:
            value.prev = "--"
            continue
        value.prev = str(All_reservations[key-1].id)

    return render(request, 'index.html', context={"result": All_reservations})




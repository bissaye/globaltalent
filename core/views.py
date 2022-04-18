from django.shortcuts import render
from .models import *

# Create your views here.


# the main vue
def reservations(request):
    '''
    getting all reservation and by date of creation in the table
    '''
    All_reservations = Reservation.objects.all().order_by('rental')

    sorting = {}
    previous = "-"

    '''
    sort all reservation in a dictiannary by adding the previous id
    '''
    for reservation in All_reservations:
        if reservation.rental in sorting.keys():
            sorting[reservation.rental].append([reservation.id, reservation.checkin, reservation.checkout, previous])
            previous = reservation.id
        else:
            sorting[reservation.rental] = [[reservation.id, reservation.checkin, reservation.checkout, '-']]
            previous = reservation.id

    '''
    formatting for display
    '''
    Sorting = []
    for key, value in sorting.items():
        for val in value:
            item = [key]
            item.extend(val)
            print(item)
            Sorting.append(item)
    for i in Sorting:
        print(i)
    return render(request, 'index.html', context={"result": Sorting})




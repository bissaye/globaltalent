# globaltalent
# TEST CODE TASK - Mid Python Django Engineer - Remote

superuser info:
- username: root
- password: root

topic:
Lets we have a django project.
With models:

Rental
 - name

Reservation
- rental_id
- checkin(date)
- checkout(date)


Add the view with the table of Reservations with "previous reservation ID".
Previous reservation is a reservation that is before the current one into same
rental.


Example:<br>
Rental-1  <br>
Res-1(2022-01-01, 2022-01-13) <br>
Res-2(2022-01-20, 2022-02-10) <br>
Res-3(2022-02-20, 2022-03-10) <br>

Rental-2 <br>
Res-4(2022-01-02, 2022-01-20) <br>
Res-5(2022-01-20, 2022-02-11) <br>


|Rental_name|ID      |Checkin    |Checkout  |Previous reservation, ID| <br>
|rental-1   |Res-1 ID| 2022-01-01|2022-01-13| -                      | <br>
|rental-1   |Res-2 ID| 2022-01-20|2022-02-10| Res-1 ID               | <br>
|rental-1   |Res-3 ID| 2022-02-20|2022-03-10| Res-2 ID               | <br>
|rental-2   |Res-4 ID| 2022-01-02|2022-01-20| -                      | <br>
|rental-2   |Res-5 ID| 2022-01-20|2022-01-11| Res-4 ID               | <br>

Also, add a tests.

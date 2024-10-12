from train import Train
from customer import Customer

n = int(input("enter the number of trains to be schedules : "))
trains = []
for i in range (n):

    date = str(input(f"enter the date on which the train {i+1} has to be scheduled : "))
    train_obj = Train(date)
    trains.append(train_obj)


def cancelticket(customer_id , train_id):

    customer_obj = None
    train_obj = None
    for i in trains:
        if i.train_id == train_id:
            train_obj = i
            break
    if not train_obj:
        print("No train with such id is scheduled !")
    else:
        for j in train_obj.cust_details.values() :
            if j.cust_id == customer_id:
                customer_obj = j
                break
        if not customer_obj:
            print(f"No such customer id found against the train {train_id} bookings")
        else:
            left_index = train_obj.stations.index(customer_obj.start)
            right_index = train_obj.stations.index(customer_obj.end)
            if customer_obj.ticket_type == 'P':
                for k in range(left_index , right_index):
                    train_obj.premium_tickets[k] += customer_obj.No_of_tickets

                reduced_amount = (customer_obj.No_of_tickets * 20)

                train_obj.revenue-= reduced_amount
                del train_obj.cust_details[customer_obj.cust_id]
                print("The ticket has been successfully cancelled !")

                train_obj.printdetails()

            if customer_obj.ticket_type == 'N':
                for k in range(left_index, right_index):
                    train_obj.normal_tickets[k] += customer_obj.No_of_tickets
                reduced_amount = (customer_obj.No_of_tickets * 10)
                train_obj.revenue -= reduced_amount
                del train_obj.cust_details[customer_obj.cust_id]

                print("The ticket has been successfully cancelled !")

                train_obj.printdetails()

            else:

                print("please enter a valid ticket type")




def booktickets(start , end , typeoftickets , no_of_tickets , date ):

    my_train = None
    for i in trains:
        if i.start_date == date:
            my_train = i
            break
    if not my_train:
        print("no trains have been scheduled for the given date")
    else:
        #checking if tickets are available
        start_index = my_train.stations.index(start)
        end_index = my_train.stations.index(end)
        if typeoftickets == "P":
            flag = True
            for i in range(start_index , end_index):
                if my_train.premium_tickets[i] >= no_of_tickets:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                customer_obj = Customer(no_of_tickets , typeoftickets , start , end , my_train.train_id )
                for i in range(start_index, end_index):
                    my_train.premium_tickets[i] = my_train.premium_tickets[i] - no_of_tickets
                my_train.revenue = my_train.revenue + ((my_train.premium_price)*no_of_tickets)
                customer_obj.price_paid = ((my_train.premium_price) * no_of_tickets)
                my_train.premium_price += (5*no_of_tickets)
                my_train.cust_details[customer_obj.cust_id] = customer_obj

                print("the ticket has been successfully booked :)")
                print(f"your customer id is {customer_obj.cust_id}")
                my_train.printdetails()

            else:
                print("Sufficient tickets not available")

        elif typeoftickets == "N":

            flag = True
            for i in range(start_index, end_index):
                if my_train.normal_tickets[i] >= no_of_tickets:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                customer_obj = Customer(no_of_tickets, typeoftickets, start, end, my_train.train_id)
                for i in range(start_index, end_index):
                    my_train.normal_tickets[i] = my_train.normal_tickets[i] - no_of_tickets
                my_train.revenue = my_train.revenue + (10 * no_of_tickets)
                customer_obj.price_paid = (10 * no_of_tickets)
                my_train.cust_details[customer_obj.cust_id] = customer_obj
                print("the ticket has been successfully booked :)")
                print(f"your customer id is {customer_obj.cust_id}")
                my_train.printdetails()

            else:
                print("Sufficient tickets not available")



def mainnn():
    while True:
        option = int(input('''
        enter your option  : 
        0 - > book tickets
        1 - > view train details
        2 - > cancel trains
        '''))

        match option:
            case 0 :
                start = str(input("enter starting location : "))
                end  = str(input("enter frop off location : "))
                ticket_type = str((input("enter the type of tickets you would like to book(P/N) : ")))
                no_tickets = int(input("enter the number of tickets : "))
                date = str(input("please specify the date of travel : "))
                booktickets(start , end , ticket_type , no_tickets , date)
                break

            case 1 :
                for i in trains:
                    i.printdetails()
                break

            case 2:
                transaction_id = int(input("enter the transaction id : "))
                train_id = int(input("enter the train id : "))
                cancelticket(transaction_id , train_id)
                break

while True:
    mainnn()

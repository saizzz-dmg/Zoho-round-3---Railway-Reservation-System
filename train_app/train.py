class Train:
    No_trains = 0
    def __init__(self , date):
        Train.No_trains+=1
        self.train_id = Train.No_trains
        self.start_date = date
        self.stations = ['Chennai' , 'Chengalpet' , 'Tindivanam' , 'Viluppuram' , 'Trichy']
        self.premium_tickets = [5,5,5,5]
        self.premium_price = 20
        self.normal_tickets = [10,10,10,10]
        self.cust_details = dict()
        self.revenue = 0


    def printdetails(self):
        print(f"             train id  : {self.train_id}                revenue : {self.revenue}")
        print(" customer id      no of tickets            ticket_type            start                      end                 price_paid ")
        for i in self.cust_details.values():
            print(f"   {i.cust_id}                  {i.No_of_tickets}                        {i.ticket_type}                {i.start}                       {i.end}                 {i.price_paid}")




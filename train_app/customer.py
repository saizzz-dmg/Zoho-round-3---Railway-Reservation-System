class Customer:
    customer_id = 0
    def __init__(self , no_tickets , ticket_type , start ,  end , train_id):
        Customer.customer_id +=1
        self.cust_id = Customer.customer_id
        self.No_of_tickets = no_tickets
        self.ticket_type = ticket_type
        self.start = start
        self.end = end
        self.train_id = train_id





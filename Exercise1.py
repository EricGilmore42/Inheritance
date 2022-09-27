import PersonClass as p 

def main(): 
    name = 'John'
    address = '123 Baylor'
    phone_number = '1234324325'
    cust_number = 123 
    on_list_flag = False 

    person1 = p.person(name,address,phone_number)

    cust1 = p.customer(name,address,phone_number,cust_number,on_list_flag)

    person1.print_person()

    cust1.print_person()

main()
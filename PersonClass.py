class person: 
    def __init__(self,name,address,telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_number(self):
        return self.__telephone

    def print_person(self):
        print('Name: ',self.__name)
        print('Addr: ',self.__address)
        print('Phone: ',self.__telephone)

class customer(person):
    def __init__(self,name,address,telephone,custnumb,mailing):
        person.__init__(self,name,address,telephone)

        self.__custnumb = custnumb
        self.__mailing = mailing

    def print_person(self): 
        person.print_person(self)

        print('Cusotmer Number: ', self.__custnumb)
        if self.__mailing:
            print('On Mailing Yes')
        else:
            print('No')
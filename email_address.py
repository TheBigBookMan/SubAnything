import APIs

class Person:
    def __init__(self, name, address, content):
        self.name = name
        self.address = address
        self.content = content

    # ? Need a function here for calling the API
    def check_api(self):
        APIs.check_api_calls(self.content)


    # ? Need a function for creating the email message



# ? Andy
andy = Person("Andy Kyriakou", 'andykyriakou95@gmail.com', [{'house': ['Plympton']}, {'business': ['wellbeing', 'wellness']}])
# andykyriakou95@gmail.com
# financial wellbeing and wellness startup news
# house prices
andy.check_api()

# ? Mum
denise = Person("Denise Darling", "d.darling@adam.com.au", {'house': ['Torrens Park', 'Brompton', 'Port Elliot']})
# d.darling@adam.com.au
# torrens park house prices

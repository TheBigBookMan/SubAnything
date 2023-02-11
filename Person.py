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
    def create_email(self):
        print(self.check_api())



import APIs
import email_functions

class Person:
    def __init__(self, name, address, content):
        self.name = name
        self.address = address
        self.content = content

    # ? Need a function here for calling the API
    def check_api(self):
        api_content = APIs.check_api_calls(self.content)
        return api_content

    # ? Need a function for creating the email message
    def create_email(self):
        content = self.check_api()
        email_functions.create_email_content(content)



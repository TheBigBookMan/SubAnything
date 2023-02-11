
# ? App that webscrapes date/uses API data 
# ? can be stock prices, business news, housing info/markets
# ? Will have peoples emails and then have a select criteria of what they want to be sent to them
# ? WIll need to create a new gmail to send the automatic emails ebcause it will be a lot
# ? Creates a pdf with the info
# ? Send weekly pdfs with the info

# ? Python course section 28 has the info on how to set it up as a 24 hour running program

# ? Maybe have a CLI for me for easier input when creating newer people


# * This main page will go through calling the person functions to start the process of it all

from Person import Person


# ? Andy
andy = Person("Andy Kyriakou", 'andykyriakou95@gmail.com', [{'house': ['Plympton']}, {'news': ['global wellbeing', 'global wellness']}])
# andy.create_email()
# andy.check_api()

# ? Mum
denise = Person("Denise Darling", "d.darling@adam.com.au", [{'house': ['Torrens Park', 'Brompton', 'Port Elliot']}, {'news': ['Australian HOUSE', 'us election']}])
denise.create_email()


# * create a function herer that can just loop through and use that new Person.create_email() dynamically
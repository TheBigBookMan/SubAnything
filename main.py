
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

# * For news have first index of the country, second have keyword (australia economy)

# ? Andy
andy = Person("Andy Kyriakou", 'andykyriakou95@gmail.com', [{'house': [{"suburb": "Plympton", "postcode": '5038', 'state': 'sa'}]}, {'news': ['global wellbeing', 'global wellness']}])

andy.create_email()
# * below is proper call
# andy.send_email()

# ?? mum wants stocks for WEBJET and FLIGHTCENTRE
# ?? do crypto for ETH, QNT, SOL and AVAX i think
# ? Mum
denise = Person("Denise Darling", "d.darling@adam.com.au", [{'house': [{"suburb": "Torrens Park", "postcode": "5062", "state": "sa"}, {"suburb": "Brompton", "postcode": "5007", "state": "sa"}, {"suburb": "Port elliot", "postcode": "5212", "state": "sa"}]}, {'news': ['Australian HOUSE', 'us ukraine', 'global archaeology']}])

# denise.create_email()
# * below is proper call
# denise.send_email()


# * create a function herer that can just loop through and use that new Person.create_email() dynamically
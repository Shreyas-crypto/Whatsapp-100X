import pywhatkit

phone_number=input("Enter your phone number: ")
pywhatkit.sendwhatmsg(phone_number,"All Is Well."*100,19,52)
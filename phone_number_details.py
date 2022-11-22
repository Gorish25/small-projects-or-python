import phonenumbers

# timezone tells the time of that mobile no. location
# geocoder tells location
# carrier tells about sim type
from phonenumbers import timezone, geocoder, carrier

# asking user to input phone number to check
number=input("Enter the phone number to check: ")

#giving indian code 
number='+91'+number

# parse() gives all the details of phone number
phone=phonenumbers.parse(number)

# give timezone of phone number 
time=timezone.time_zones_for_number(phone)

# gives details about carrier of phone number (en means in english)
car=carrier.name_for_number(phone,'en')

# registration details
reg=geocoder.description_for_number(phone,'en')

print(phone)
print(time)
print(car)
print(reg)
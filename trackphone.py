import phonenumbers
from phonenumbers import geocoder
phonenumber1=phonenumbers.parse("+254 113114970")
phonenumber1=phonenumbers.parse("+254 725055588")
phonenumber1=phonenumbers.parse("+254 717199307")
phonenumber1=phonenumbers.parse("+254 721752916")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phonenumber1,"en"))
print(geocoder.description_for_number(phonenumber1,"en"))
print(geocoder.description_for_number(phonenumber1,"en"))
print(geocoder.description_for_number(phonenumber1,"en"))
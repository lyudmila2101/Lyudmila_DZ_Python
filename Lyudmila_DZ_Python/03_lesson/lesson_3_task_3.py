from Address import Address
from Mailing import Mailing

to_address = Address('428027', 'Москва', 'Мира', 25 , 148)
from_address = Address('127345', 'Чебоксары', 'Гагарина', 148 , 25 )   
cost = "1500"
trak = "123456789"

mailing = Mailing(to_address, from_address, cost, trak)

print(mailing)






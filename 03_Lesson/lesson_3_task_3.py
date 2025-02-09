from Address import Address
from Mailing import Mailing

from_address = Address("424800", "йошкар-ола", "Ленина", "24", "52")
to_address = Address("424887", "Казань", "Комсомольская", "24", "10")

mailing = Mailing ("589632", from_address, to_address, 5200)

print(mailing)

#           დავალება1
password=input("პაროლი: ")
password_confirm=input("საბოლოო პაროლი: ")

while password != password_confirm:
  password_confirm=input("პაროლი არ ემთხვევა სცადეთ ახლიდან: ")

print("correct!")
#                       დავალება2
number=input("გამოიცანი ციფრი: ")
confirm_number=input("ციფრი არ ემთხვევა სცადეთ ახლიდან: ")


while number != number_confirm:
  number_confirm=input("ციფრი არ ემთხვევა სცადეთ ახლიდან: ")

print("შენ ციფრი გამოიცანი!")

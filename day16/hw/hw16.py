#                დავალება1
i = 1
while i < 11:
  print(i)
  i += 1

#                დავალება2
password=input("პაროლი: ")
password_confirm=input("საბოლოო პაროლი: ")

while password != password_confirm:
  password_confirm=input("პაროლი არ ემთხვევა სცადეთ ახლიდან: ")

print("პაროლი ემთხვევა!")



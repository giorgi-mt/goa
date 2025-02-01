#homework1
number=int(input("enter number: "))

if number % 2 == 0:
    print("რიცხვი არის ლუწი")
else:
    print("რიცხვი არის კენტი")
#homework2
age=int(input("enter age: "))

if age % 18 == 0:
    print("შენ ხარ სრულწლოვანი")
else:
    print("შენ არ ხარ სრულწლოვანი")
#homework3
score=int(input("enter your score : "))

if score >= 90:
    print("you got A")
elif score >=80:
    print("you got B")
elif score >= 70:
    print("you got C")
else:
    print("your score is lowe")
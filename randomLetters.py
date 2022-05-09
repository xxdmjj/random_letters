import random

alphabet = ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
Max_value = 50
User_amount = input("select a number 1-50")

while int(User_amount) < Max_value:
    print(random.sample(alphabet, int(User_amount)))


while int(User_amount) > Max_value:
    print('Try a smaller value')
    input("select a number 1-50")
    continue

















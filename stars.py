#1.yıldız
number = 5
for i in range(1, number + 1):
  print(" "*(number-i) +"* "*i )

#2.yıldız
number = 5
for i in range(0, number + 1):
    for j in range(1, (number + 1 - i)):
        print("* ", end=" ")
    print()

#3.yıldız
number = 5
for i in range(1, number + 1):
    for j in range(1, (i + 1)):
        print("* ", end=" ")
 
    print()
        
for x in range(1, number + 1):
    for j in range(1, (number + 1 - x)):
        print("* ", end=" ")
 
    print()
response = int(input("Combien de nombre voulez-vous mettre dans la liste ? : "))
my_lyst = []


for i in range(response):
    number = int(input("Entrer une valeur: "))
    my_lyst.append(number)

print("Here is my Lis of Number", my_lyst)

sum_list = sum(my_lyst)
print("The sum of the list of elements: ", sum_list)
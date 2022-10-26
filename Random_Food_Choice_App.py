import random
print("Hi, Welcome to Random Food Choice App\n")
value = int(input("Please enter number to select food category choice:\n 1. Fruits\n 2. Vegetables\n 3. Grains\n 4. Protein Foods\n 5. Dairy\n"))
if value == 1:
    Fruits_list = ['Pineaple', 'Orange', 'Banana', 'Mango', 'Water Mellon', 'Guava']
    print("Your food choice is:" + (random.choice(Fruits_list)))
elif value == 2:
    Vegetables_list = ['Kale', 'Cabbage', 'Tomatoes', 'Onions', 'Green pepper', 'Spinach']
    print("Your food choice is:" + (random.choice(Vegetables_list)))
elif value == 3:
    Grains_list = ['Brown Rice', 'Popcorn', 'Oatmeal', 'Pretzels', 'English Muffins', 'Corn Tortilla']
    print("Your food choice is:" + (random.choice(Grains_list)))
elif value == 4:
    Proteins_list = ['Beef', 'Chicken', 'Pork', 'Eggs', 'Tilapia', 'Groundnuts']
    print("Your food choice is:" + (random.choice(Proteins_list)))
elif value == 5:
    Dairy_list = ['Milk', 'Yorghut', 'Kefir', 'Cheese', 'Cottage Cheeze', 'Calcium-fortified Soymilk']
    print("Your food choice is:" + (random.choice(Dairy_list)))
else:
    print("Sorry, the category you selected does not exist")
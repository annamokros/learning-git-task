count = 0
shopping_dictionary ={
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}
for shop, food in shopping_dictionary.items():
    print(f"Idę do {shop.title()}, kupuję tu następujące rzeczy: {str(food).title()}")
    for i in food:
        count +=1
print(f"W sumie kupuję {count} produktów")
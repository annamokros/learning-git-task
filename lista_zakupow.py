shopping_dictionary ={
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}
for shop, food in shopping_dictionary.items():
    print(f"Idę do {shop.title()}, kupuję tu następujące rzeczy: {str(food).title()}")
shopping_cart = len(food)*2
print(f"W sumie kupuję {shopping_cart} produktów")
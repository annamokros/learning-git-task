shopping_dictionary ={
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}
for shop, food in shopping_dictionary.items():
    print(f"Idę do {shop.title()}, kupuję tu następujące rzeczy: {str(food).title()}")
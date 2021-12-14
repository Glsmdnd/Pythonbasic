""" Doğru çalışan bu!!!! """
fruits = [["apple", "umbrella","cherry"],["apple", "banana","tomato"]]
for fruit in fruits:
  if 'banana' in fruit:
    fruit.remove("banana")
    print(fruit)
  else:
    print(fruit)
   
   

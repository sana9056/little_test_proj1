list1 = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]
list2 = []
for i in list1:
    if "Apple" in i:
        list2.append(i)
print("Есть исходный список", list1)
print("В этом списке есть следующая продукция APPLE:")
print(list2)

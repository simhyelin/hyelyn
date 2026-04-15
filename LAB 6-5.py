fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 4000}
print(list(fruits_dic.keys()))   
print(list(fruits_dic.values()))
print(f"fruits_dic 딕셔너리의 항목의 개수 : {len(fruits_dic)}")
print("apple is in fruits_dic." if 'apple' in fruits_dic else "apple is not in fruits_dic.")
print("mango is in fruits_dic." if 'mango' in fruits_dic else "mango is not in fruits_dic.")

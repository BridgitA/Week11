elem = open("elements1_20.txt","r")

elem_temp = elem.readline()

while elem_temp:
    element_names = elem_temp.strip().lower()
    elem_temp = elem.readline()

correct_list = []
incorrect_list = []
element_list = []

def get_names():
    count = 0
    while count <= 4:
        element = input("Enter the name of an element:")
        if element.lower() in element_list:
            print(element,"already entered in list. <- no duplicates allowed")
        elif len(element) > 0:
            element_list.append(element.lower())
            count += 1
    return element_list

get_names()

for i in element_list:
    if i in element_names:
        correct_list.append(i)
    else: 
        incorrect_list.append(i)
    
num = len(correct_list)

correct_num = num * 20

print(correct_num,"%","correct")
print("Found: ",correct_list)
print("Not Found: ",incorrect_list)

print(element_names)
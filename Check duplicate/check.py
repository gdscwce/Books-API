import json

file_name = 'data.json'

options = (input("Do you want to delete duplicate items (y/n) - "))
if options == 'y':
    mylist = []
    with open(file_name, 'r', encoding='utf-8') as f:
        my_list = json.load(f)
    dupItems = []
    uniqueItems = []
    for my in my_list:
        if my not in dupItems:
            dupItems.append(my)
            uniqueItems.append(my)

    with open(file_name, 'w', encoding='utf-8') as writejson:
        json.dump(dupItems, writejson, indent=4)
    f.close()
    writejson.close()  
    print("Done")

elif options == 'n':
    print("ok")

# You can check the python program by running
# it locally on 'test.json' just change the file_name to 'test.json'
# When checked you can change file_name to 'data.json' don't forget to specify the path - 'D:/Books-API/data.json'

# Currently data.json has many duplicate values
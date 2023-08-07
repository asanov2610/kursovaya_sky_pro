from list_class import ListClass
from data_class import Data

our_list = ListClass().get_slice_list()


for item in our_list:
        if item.get('from') != None:
                operation = Data(item['date'], item['to'], item['description'], item["operationAmount"]["amount"],
 item["operationAmount"]["currency"]["name"], item["from"])
                print(operation)
                print()
        else:
                operation = Data(item['date'], item['to'], item['description'], item["operationAmount"]["amount"],
item["operationAmount"]["currency"]["name"])
                print(operation)
                print()

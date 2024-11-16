import json as js
import time

#class for Expenses
class Expense:
    def __init__(self, id, description, amount):
        self.id  = id
        self.date = time.strftime("%y-%m-%d", time.localtime())
        self.description  = description 
        self.amount  = amount 
#--------------------------------------------------------------------------------------------------------------------------------
#add new expense
def add(value):
    try:
        amount = int(value.split()[-1])
    except ValueError:
        print("the amount isn't a number")
        main()
    description = " ".join(value.split()[:-1])
    with open("data.json", 'r') as file:
        data = js.load(file)
        data.append(Expense( (lambda x: x + 1)(int(data[-1]["id"])) if data[-1]["id"] != "ID" else 1, description, amount).__dict__)
    with open("data.json", 'w') as file:
        js.dump(data, file)
        print(f"expense added succsessful id: {data[-1]['id']}", "\n")
#--------------------------------------------------------------------------------------------------------------------------------
#updating expenses
def update(value):
    id = int(value.split()[0])
    try:
        amount = int(value.split()[-1])
    except ValueError:
        print("the amount isn't a number")
        main()
    description = " ".join(value.split()[1:-1])

    with open("data.json", 'r') as file:
        data = js.load(file)
        data[id]["description"], data[id]["amount"] = description, amount
    with open("data.json", 'w') as file:
        js.dump(data, file)
        print(f"expense updated succsessful id: {data[-1]['id']}", "\n")

#--------------------------------------------------------------------------------------------------------------------------------
#deleting expenses
def delete(value):
  try:
    if int(value) > 0:
        with open('data.json', "r+") as file:
            data = js.load(file)

            if data == [] or len(data) == 1:
                print("list is empty")
                main()  
        data.pop(int(value)) 

        for i in range(int(value), len(data)):
          data[i]["id"] = data[i]["id"] - 1

        with open('data.json', "w") as file:
            js.dump(data, file)
            print("the expense was successful delete \n")

    main()

  except (IndexError, ValueError):
    print("invalid index")
    main()
#--------------------------------------------------------------------------------------------------------------------------------

def main():
    comma = input("Write command: ").split(maxsplit=1)
    try:
        if len(comma) == 1:
            func = comma[0]
            value = None
        else:
            func, value = comma
        globals()[func](value)
    except (KeyError, TypeError):
        print("wrong command")
    except AttributeError:
        print("attribute wasn't given")
    except TypeError:
        print("wrong attribute")

    main()


def WakeUp():
    try:
        with open('data.json', 'r') as file:
            print("data file exist")
    except FileNotFoundError:
        print("no data file\n\nmaking data file")
        with open('data.json', 'w') as file:
            js.dump([{'id': 'ID', 'date': "Date", "description": 'description', "amount": "amount"}], file)
    main()

    

WakeUp()

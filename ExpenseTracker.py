import json as js
import time

#class for Expenses
class Expense:
    def __init__(self, id, description, amount):
        self.id  = id
        self.date = time.strftime("%d-%m-%y", time.localtime())
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

def align(data, id, current, column):
    Gap = [0, 0]
    Gap[0], Gap[1] = " " * ((round(len(str(data[id][column])) / 2)) - round(len(str(data[current][column])) / 2 )), " " * ((len(str(data[id][column])) - round(len(str(data[id][column])) / 2)) - (len(str(data[current][column])) - round(len(str(data[current][column])) / 2 ))) 
    return Gap
#--------------------------------------------------------------------------------------------------------------------------------
def list():
    with open("data.json", "r") as file:
        data = js.load(file)
        gap = " "*11
        id = 0
        amount = 0
        for i in data[1:]:
            if len(i["description"]) > len(data[id]["description"]):
                id = int(i["id"])
            if len(str(i["amount"])) > len(str(data[amount]["amount"])):
                amount = int(i["id"])
        print(f"{ data[0]['id'] }{gap}{ data[0]['date'] }{gap}{align(data, id, 0, 'description')[0]}{ data[0]['description'] }{align(data, id, 0, 'description')[1]}{gap}{align(data, 0, int(i['id']), 'amount')[0]}{ data[0]['amount'] }{align(data, 0, int(i['id']), 'amount')[1]}")
        for i in data[1:]:
            print(f"{ i['id'] }{gap[(len(str(i['id'])) - 1):]}{ i['date'] }{gap[2:]}{align(data, id, int(i['id']), 'description')[0]}{ i['description'] }{align(data, id, int(i['id']), 'description')[1]}{gap}{align(data, amount, int(i['id']), 'amount')[0]}{ i['amount'] }{align(data, amount, int(i['id']), 'amount')[1]}")


#--------------------------------------------------------------------------------------------------------------------------------

def summary(month = 0):
    with open("data.json", "r") as file:
        data = js.load(file)
        summary = 0
        if int(month) == 0:
            for i in data[1:]:
                summary += int(i["amount"])
        elif 1 <= int(month) <= 12:
            for i in data[1:]:
                if i["date"].split("-")[1] == month:
                    summary += int(i["amount"])
        else:
            print("wrong month \n")
            main()
        print("Total expenses: ", summary)

#--------------------------------------------------------------------------------------------------------------------------------

def main():
    comma = input("Write command: ").split(maxsplit=1)
    try:
        if len(comma) == 1:
            func = comma[0]
            globals()[func]()
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
            js.dump([{'id': 'ID', 'date': " Date", "description": 'description', "amount": "amount"}], file)
    main()

    

WakeUp()

import json 

try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)


except FileNotFoundError:

    expenses = {
        "items" : [],
        "amount": []
    }

while(True):
    response = input("enter item ( or 'done' to finish ): ")
    if response == "done":

        break

    expenses["items"].append(response)
    expenses["amount"].append(int(input("enter amount: ")))

print("Expenses:")

for i in range(len(expenses['items'])):
    print(f"{expenses['items'][i]} - Rs{expenses['amount'][i]}")

while(True):
    response = input("Want to delete an item? (yes/no): ")
    if response == "no":
        break
    else: 
        removeitem = input("enter item to delete: ")
        for i in range(len(expenses["items"])):
            if expenses["items"][i] == removeitem :
                expenses["items"].remove(expenses["items"][i])
                expenses["amount"].remove(expenses["amount"][i])
                break


with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)



for i in range(len(expenses['items'])):
    print(f"{expenses['items'][i]} - Rs{expenses['amount'][i]}")




print(f"TOTAL : Rs{sum(expenses['amount'])}")








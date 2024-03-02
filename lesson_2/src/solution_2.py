import json

inventory: dict = {
  "inventory": [
    {
      "item": "Кисти",
      "category": "Инструменты",
      "quantity": 5,
      "minimum_required": 10
    },
    {
      "item": "Краска акриловая",
      "category": "Материалы",
      "quantity": 20,
      "minimum_required": 15
    }
  ]
}

with open('inventory.json', 'w', encoding='utf-8') as file:
    json.dump(inventory, file)


def inventory_check(dct: dict[str: str|int]) -> None:
    if "item" in dct and "quantity" in dct and "minimum_required" in dct:
        if dct["quantity"] < dct["minimum_required"]:
            print(f'Необходимо закупить: {dct["item"]} {dct["minimum_required"] - dct["quantity"]} шт.')


with open('inventory.json', 'r', encoding='utf-8') as file:
    json.load(file, object_hook=inventory_check)
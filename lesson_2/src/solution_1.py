import json

sales: dict = {
  "sales": [
    {
      "product": "Футболка",
      "category": "Одежда",
      "quantity": 3,
      "total_price": 1500
    },
    {
      "product": "Чашка",
      "category": "Посуда",
      "quantity": 2,
      "total_price": 700
    }
  ]
}


def calculation_revenue(dct: dict) -> None:
    if "category" in dct and "quantity" in dct and "total_price" in dct:
        print(f'Выручка по категории "{dct["category"]}": {dct["quantity"] * dct["total_price"]}')


with open('sales.json', 'w', encoding='utf8') as file:
    json.dump(sales, file)

with open('sales.json', 'r', encoding='utf8') as file:
    sales = json.load(file, object_hook=calculation_revenue)
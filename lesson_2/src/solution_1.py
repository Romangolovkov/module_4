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
    },
    {
      "product": "Тарелка",
      "category": "Посуда",
      "quantity": 3,
      "total_price": 300
    }
  ]
}

with open('sales.json', 'w', encoding='utf-8') as file:
    json.dump(sales, file)

revenue_by_category: dict[str: int] = dict()


def calculation_revenue(dct: dict[str: str|int]) -> None:
    if "category" in dct and "quantity" in dct and "total_price" in dct:
        if dct["category"] in revenue_by_category:
            revenue_by_category[dct["category"]] += dct["quantity"] * dct["total_price"]
        else:
            revenue_by_category[dct["category"]] = dct["quantity"] * dct["total_price"]
        

with open('sales.json', 'r', encoding='utf-8') as file:
    json.load(file, object_hook=calculation_revenue)

for category, revenue in revenue_by_category.items():
    print(f'Выручка по категории "{category}": {revenue}')
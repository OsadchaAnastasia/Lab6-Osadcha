import Connection
from prettytable import PrettyTable

# Словник з відповідностями англійських та українських заголовків
ukrainian_headers = {
    "warehouse_number": "Номер складу",
    "warehouse_address": "Адреса складу",
    "warehouse_manager": "Менеджер складу",
    "warehouse_phone_number": "Номер телефону складу",
    "goods_code" : "Код товару",
    "goods_type" : "Тип товару",
    "goods_name" : "Назва товару",
    "goods_manufacturer" : "Виробник товару",
    "goods_warehouse_number" : "Номер складу",
    "goods_warehouse_quantity" : "Кількість товару на складі",
    "goods_price" : "Ціна товару",
    "customer_code" : "Код клієнту",
    "customer_name" : "Назва клієнту",
    "customer_address" : "Адреса клієнта",
    "customer_phone_number" : "Номер телефону клієнта",
    "contact_person" : "Контактна особа",
    "sales_code" : "Код покупки",
    "sales_date" : "Дата покупки",
    "sales_customer_code" : "Код покупця",
    "sales_goods_code" : "Код купленого товару",
    "sales_cloth_quantity" : "Кількість купленого товару",
    "discount" : "Знижка"
}

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    def print_table(name_table, table_label):
        cursor.execute("SELECT * FROM " + name_table)
        data = cursor.fetchall()
        table = PrettyTable()
        table.title = table_label
        table.field_names = [ukrainian_headers[description[0]] for description in cursor.description if description[0] in ukrainian_headers]
        for row in data:
            table.add_row(row)
        print(table)

    print_table("Warehouse", "Склад")
    print_table("Goods", "Товари")
    print_table("Customer", "Клієнти")
    print_table("Sales", "Продажі")

except Exception as e:
    print(f"Помилка при виводі таблиць в консоль: {e}")

finally:
    cursor.close()
    connection.close()

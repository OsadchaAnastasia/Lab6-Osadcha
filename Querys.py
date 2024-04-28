import Connection
import psycopg2
from prettytable import PrettyTable

def outputTable(data):
    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in data:
        table.add_row(row)
    print(table)

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    #------------------------------------------------Запит1
    query1 = """
    SELECT 
        Sales.sales_date AS "Дата",
        Goods.goods_name AS "Назва",
        Customer.customer_name AS "Клієнт",
        Sales.sales_cloth_quantity AS "Кількість",
        Goods.goods_price AS "Ціна"
    FROM 
        Sales
    JOIN 
        Goods ON Sales.sales_goods_code = Goods.goods_code
    JOIN 
        Customer ON Sales.sales_customer_code = Customer.customer_code
    ORDER BY 
        Customer.customer_name;
    """

    # Виконання запиту
    cursor.execute(query1)

    # Виведення результатів
    outputTable(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Помилка при роботі з PostgreSQL", error)

finally:
    # Закриття курсора та з'єднання з базою даних
    if connection:
        cursor.close()
        connection.close()
        print("Підключення до PostgreSQL закрито")

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    # ------------------------------------------------------------Запит
    # Перевірка правильності введеного типу одягу
    valid_clothing_types = ['Чоловічий', 'Жіночий', 'Дитячий']
    clothing_type = input("Введіть тип одягу (чоловічий, жіночий, дитячий): ").capitalize()
    while clothing_type not in valid_clothing_types:
        print("Ви ввели неправильний тип одягу. Спробуйте ще раз.")
        clothing_type = input("Введіть тип одягу (чоловічий, жіночий, дитячий): ").capitalize()

    # SQL-запит
    query = """
            SELECT 
                goods_code AS "Код товару",
                goods_type AS "Тип товару",
                goods_name AS "Назва товару",
                goods_manufacturer AS "Виробник товару",
                goods_warehouse_number AS "Номер складу",
                goods_warehouse_quantity AS "Кількість на складі",
                goods_price AS "Ціна товару"
            FROM 
                Goods
            WHERE 
                goods_type = %s;
            """

    # Виконання запиту
    cursor.execute(query, (clothing_type,))

    # Виведення результатів
    outputTable(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Помилка при роботі з PostgreSQL", error)

finally:
    # Закриття курсора та з'єднання з базою даних
    if connection:
        cursor.close()
        connection.close()
        print("Підключення до PostgreSQL закрито")

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    #------------------------------------------------------------Запит
    query = """
    SELECT
        Customer.customer_name AS "Клієнт",
        COUNT(Sales.sales_code) AS "Кількість покупок"
    FROM
        Customer
    LEFT JOIN
        Sales ON Customer.customer_code = Sales.sales_customer_code
    GROUP BY
        Customer.customer_name
    ORDER BY
        Customer.customer_name;
    """

    # Виконання запиту
    cursor.execute(query)

    # Виведення результатів
    outputTable(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Помилка при роботі з PostgreSQL", error)

finally:
    # Закриття курсора та з'єднання з базою даних
    if connection:
        cursor.close()
        connection.close()
        print("Підключення до PostgreSQL закрито")


try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    #------------------------------------------------------------Запит з урахуванням знижки
    query_with_discount = """
    SELECT
        Customer.customer_name AS "Клієнт",
        SUM(Sales.sales_cloth_quantity * Goods.goods_price * (1 - Sales.discount)) AS "Ціна покупки зі знижкою"
    FROM
        Customer
    LEFT JOIN
        Sales ON Customer.customer_code = Sales.sales_customer_code
    LEFT JOIN
        Goods ON Sales.sales_goods_code = Goods.goods_code
    GROUP BY
        Customer.customer_name
    ORDER BY
        Customer.customer_name;
    """

    # Виконання запиту з урахуванням знижки
    cursor.execute(query_with_discount)

    # Виведення результатів
    print("З урахуванням знижки:")
    outputTable(cursor.fetchall())

    #------------------------------------------------------------Запит без урахування знижки
    query_without_discount = """
    SELECT
        Customer.customer_name AS "Клієнт",
        SUM(Sales.sales_cloth_quantity * Goods.goods_price) AS "Ціна покупки без знижки"
    FROM
        Customer
    LEFT JOIN
        Sales ON Customer.customer_code = Sales.sales_customer_code
    LEFT JOIN
        Goods ON Sales.sales_goods_code = Goods.goods_code
    GROUP BY
        Customer.customer_name
    ORDER BY
        Customer.customer_name;
    """

    # Виконання запиту без урахування знижки
    cursor.execute(query_without_discount)

    # Виведення результатів
    print("\nБез урахування знижки:")
    outputTable(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Помилка при роботі з PostgreSQL", error)

finally:
    # Закриття курсора та з'єднання з базою даних
    if connection:
        cursor.close()
        connection.close()
        print("Підключення до PostgreSQL закрито")


try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    #------------------------------------------------------------Запит
    query = """
    SELECT
        Customer.customer_name AS "Клієнт",
        SUM(Sales.sales_cloth_quantity * Goods.goods_price * (1 - Sales.discount)) AS "Загальна сума витрат"
    FROM
        Customer
    LEFT JOIN
        Sales ON Customer.customer_code = Sales.sales_customer_code
    LEFT JOIN
        Goods ON Sales.sales_goods_code = Goods.goods_code
    GROUP BY
        Customer.customer_name
    ORDER BY
        Customer.customer_name;
    """

    # Виконання запиту
    cursor.execute(query)

    # Виведення результатів
    outputTable(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Помилка при роботі з PostgreSQL", error)

finally:
    # Закриття курсора та з'єднання з базою даних
    if connection:
        cursor.close()
        connection.close()
        print("Підключення до PostgreSQL закрито")

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    #------------------------------------------------------------Запит
    query = """
    SELECT
        Warehouse.warehouse_number AS "Номер складу",
        Goods.goods_type AS "Тип одягу",
        SUM(Goods.goods_warehouse_quantity) AS "Кількість одягу"
    FROM
        Warehouse
    LEFT JOIN
        Goods ON Warehouse.warehouse_number = Goods.goods_warehouse_number
    GROUP BY
        Warehouse.warehouse_number, Goods.goods_type
    ORDER BY
        Warehouse.warehouse_number, Goods.goods_type;
    """

    # Виконання запиту
    cursor.execute(query)

    # Виведення результатів
    outputTable(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Помилка при роботі з PostgreSQL", error)

finally:
    # Закриття курсора та з'єднання з базою даних
    if connection:
        cursor.close()
        connection.close()
        print("Підключення до PostgreSQL закрито")
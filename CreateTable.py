import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Таблиця склад
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Warehouse (
        warehouse_number integer PRIMARY KEY,
        warehouse_address varchar(255),
        warehouse_manager varchar(255),
        warehouse_phone_number varchar(13)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Warehouse: {e}")

try:
    # Таблиця Товар
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Goods (
        goods_code integer PRIMARY KEY,
        goods_type varchar(9),
        goods_name varchar(255),
        goods_manufacturer varchar(255),
        goods_warehouse_number integer,
        goods_warehouse_quantity integer,
        goods_price decimal,
        FOREIGN KEY (goods_warehouse_number) REFERENCES Warehouse(warehouse_number)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Goods: {e}")

try:
    # Таблиця Клієнт
    create_table_query = """
        CREATE TABLE IF NOT EXISTS Customer (
            customer_code integer PRIMARY KEY,
            customer_name varchar(255),
            customer_address varchar(255),
            customer_phone_number varchar(13),
            contact_person varchar(255)
        )
        """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Customer: {e}")

try:
    # Таблиця Продаж
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Sales (
        sales_code integer PRIMARY KEY,
        sales_date DATE,
        sales_customer_code integer,
        sales_goods_code integer,
        sales_cloth_quantity integer,
        discount decimal,
        FOREIGN KEY (sales_customer_code) REFERENCES Customer(customer_code),
        FOREIGN KEY (sales_goods_code) REFERENCES Goods(goods_code)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Sales: {e}")

cursor.close()
connection.close()

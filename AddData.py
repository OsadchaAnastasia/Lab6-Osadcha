import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:


    # Додавання складів
    warehouse_data = [
        ("001", "м.Київ, ул. Шевченка, 10", "Олексій Ковальов", "+380671234567"),
        ("002", "м.Львів, пр. Свободи, 20", "Ірина Петренко", "+380682345678"),
        ("003", "м.Одеса, ул. Дерибасовська, 30", "Володимир Сидоренко", "+380633456789")
    ]

    insert_query = """
    INSERT INTO Warehouse (warehouse_number, warehouse_address, warehouse_manager, warehouse_phone_number)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (warehouse_number) DO NOTHING
    """

    for record in warehouse_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Warehouse: {e}")



try:
    # Додавання товарів
    goods_data = [
        ("001", "Чоловічий", "Сорочка", "Hugo Boss", "001", 50, 1500),
        ("002", "Жіночий", "Сукня", "Zara", "002", 100, 2000),
        ("003", "Дитячий", "Штанці", "Gap Kids", "003", 75, 800),
        ("004", "Чоловічий", "Куртка", "Calvin Klein", "001", 60, 3000),
        ("005", "Жіночий", "Блузка", "H&M", "002", 40, 1200),
        ("006", "Дитячий", "Комбінезон", "Carter's", "003", 90, 1500),
        ("007", "Чоловічий", "Джинси", "Levi's", "002", 70, 1800),
        ("008", "Жіночий", "Плаття", "Mango", "003", 55, 2500),
        ("009", "Чоловічий", "Світшот", "Adidas", "002", 80, 1600),
        ("010", "Жіночий", "Юбка", "Topshop", "001", 45, 1500),
        ("011", "Дитячий", "Піжама", "Marks & Spencer", "002", 65, 1000),
        ("012", "Чоловічий", "Костюм", "Hugo Boss", "003", 55, 5000),
        ("013", "Жіночий", "Кардиган", "H&M", "002", 70, 1200),
        ("014", "Дитячий", "Курточка", "Next", "003", 80, 1700),
        ("015", "Чоловічий", "Плащ", "Burberry", "001", 40, 6000),
        ("016", "Жіночий", "Штани", "Mango", "002", 60, 1800),
        ("017", "Дитячий", "Спортивні штани", "Nike", "003", 55, 2000)
    ]

    insert_query = """
    INSERT INTO Goods (goods_code, goods_type, goods_name, goods_manufacturer, goods_warehouse_number, goods_warehouse_quantity, goods_price)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (goods_code) DO NOTHING
    """

    for record in goods_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Goods: {e}")

try:
    # Додавання клієнтів
    customer_data = [
        ("001", "Мода Імперія", "г. Киев, ул. Ломоносова, 12", "380991234567", "Петров Петр Петрович"),
        ("002", "Елегант Фешн", "г. Львов, ул. Франка, 23", "380997654321", "Іванова Іванна Іванівна"),
        ("003", "Дива Стилю", "г. Харків, ул. Сумская, 45", "380993214578", "Сидоренко Сергій Сидорович"),
        ("004", "Модний Тренд", "г. Одеса, ул. Дерибасовская, 67", "380998745632", "Новикова Надія Михайлівна"),
        ("005", "Гарний Вигляд", "г. Дніпро, просп. Карла Маркса, 89", "380999876543", "Петренко Олександр Петрович"),
        ("006", "Шик Одяг", "г. Запоріжжя, ул. Вокзальна, 34", "380995678945", "Гончарова Анна Ігорівна"),
        ("007", "Мода та Стиль", "г. Черкаси, ул. Шевченка, 56", "380994567389", "Коваленко Віталій Володимирович")
    ]

    insert_query = """
    INSERT INTO Customer (customer_code, customer_name, customer_address, customer_phone_number, contact_person)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (customer_code) DO NOTHING
    """

    for record in customer_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Customer: {e}")

try:
    # Додавання продажів
    sales_data = [
        ('001', '2023-04-27', '001', '001', 100, 0.05),
        ('002', '2023-04-28', '002', '002', 50, 0.03),
        ('003', '2023-04-29', '003', '003', 80, 0.07),
        ('004', '2023-04-30', '004', '004', 120, 0.10),
        ('005', '2023-05-01', '005', '005', 70, 0.05),
        ('006', '2023-05-02', '006', '006', 90, 0.08),
        ('007', '2023-05-03', '007', '007', 110, 0.06),
        ('008', '2023-05-04', '001', '008', 60, 0.04),
        ('009', '2023-05-05', '002', '009', 85, 0.07),
        ('010', '2023-05-06', '003', '010', 100, 0.09),
        ('011', '2023-05-07', '004', '011', 40, 0.03),
        ('012', '2023-05-08', '005', '012', 75, 0.06),
        ('013', '2023-05-09', '006', '013', 95, 0.08),
        ('014', '2023-05-10', '007', '014', 65, 0.05),
        ('015', '2023-05-11', '001', '015', 110, 0.10),
        ('016', '2023-05-12', '002', '016', 55, 0.04),
        ('017', '2023-05-13', '003', '017', 80, 0.07),
        ('018', '2023-05-14', '004', '001', 120, 0.10),
        ('019', '2023-05-15', '005', '002', 70, 0.05),
        ('020', '2023-05-16', '006', '003', 90, 0.08),
        ('021', '2023-05-17', '007', '004', 110, 0.06),
        ('022', '2023-05-18', '001', '005', 60, 0.04)
    ]

    insert_query = """
    INSERT INTO Sales (sales_code, sales_date, sales_customer_code, sales_goods_code, sales_cloth_quantity, discount)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (sales_code) DO NOTHING
    """

    for record in sales_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Sales: {e}")
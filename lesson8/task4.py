# Lesson 8 task 4 _5 _6

"""
#Lesson 8 task 4
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

"""
#Lesson 8 task 5
 Продолжить работу над первым заданием. Разработать методы,
 отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
 Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру, например словарь
"""

"""
#Lesson 8 task 6
Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class NotFoundEquipmentType(Exception):
    def __init__(self, message):
        self.message = message


class InvalidSkuNumber(Exception):
    def __init__(self, message):
        self.message = message


class Warehouse:
    # здесь будет хранится вся техника
    __office_equipment_collection = {
        'printer': [],
        'xerox': [],
        'scan': []
    }

    # здесь будет поструктурно хранится учтенная техника
    """
    EXAMPLE MAP
        {
            'бухгалтерия':{
                xerox:['xe-12-23', 'xe-22-11'],
                scan:[],
                printer:['pr-123']
            },

            'ресепшн':{
                printer:['pr-123']
            }
        }
    """
    __structure_assigned_equipment = {

    }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Warehouse, cls).__new__(cls)
        return cls.instance

    # добавляем единицу в общий список
    def add_equipment(self, equipment_type: str, equipment: dict):
        try:
            if not self.__office_equipment_collection.get(equipment_type):
                raise NotFoundEquipmentType(f'Оборудование {equipment_type} не учитывается')

            self.__office_equipment_collection[equipment_type].append(equipment)
        except NotFoundEquipmentType as error:
            print(error.message)

    # закрепляем по артикулу единицу за соответствующей структурой
    def assign_equipment_to_structure(self, structure: str, equipment_type: str, equipment_sku_number: str):
        try:
            if not self.__office_equipment_collection.get(equipment_type):
                raise NotFoundEquipmentType(f'Оборудование {equipment_type} не учитывается')

            if not self.__validate_sku(equipment_sku_number, equipment_type):
                raise InvalidSkuNumber(f'Артикул {equipment_sku_number} не найден в раздее {equipment_type}')

            self.__structure_assigned_equipment[structure][equipment_type].append(equipment_sku_number)

        except NotFoundEquipmentType as error:
            print(error.message)
        except InvalidSkuNumber as sku_error:
            print(sku_error.message)

    def __validate_sku(self, equipment_sku_number: str, equipment_type: str):
        for item in self.__office_equipment_collection[equipment_type]:
            if item['sku'] == equipment_sku_number:
                return True
            else:
                return False

    # полное количество техники
    def get_full_qty(self):
        result = {}
        for eq_type, eq_list in self.__office_equipment_collection:
            result[eq_type] = len(eq_list)
        return result

    # оставшаяся на складе техника. Из полного перечня удалим зарезервированное кол-во
    def get_in_stock_qty(self):
        full_qty = self.get_full_qty()
        assigned_qty = self.get_assigned_qty()
        result = {}
        for key, value in full_qty:
            result[key] = value - assigned_qty[key]

        return result

    # техника в подразделениях
    def get_assigned_qty(self):
        result = {}
        for structure, equipment in self.__structure_assigned_equipment:
            for eq_type, eq_sku_list in equipment:
                result[eq_type] += len(eq_sku_list) if result.get(eq_type) is not None else len(eq_sku_list)
        return result


class OfficeEquipment:
    name: str
    sku: str
    eq_type: str

    def add_item(self, **kwargs):
        self.__dict__.update(kwargs)


class Xerox(OfficeEquipment):
    eq_type = 'xerox'
    is_color: bool


class OnlyNumericPrinterSku(Exception):
    def __init__(self, message):
        self.message = message


class Printer(OfficeEquipment):
    is_color: bool
    sku: int
    eq_type = 'printer'

    def add_item(self, **kwargs):
        try:
            if not kwargs['sku'].isnumetic():
                raise OnlyNumericPrinterSku('Sku для принтера только числовые!')
            kwargs['sku'] = int(kwargs['sku'])
        except OnlyNumericPrinterSku as error:
            print(error)


class Scan(OfficeEquipment):
    dpi: int
    eq_type = 'scan'


Printer().add_item(
    name='epson',
    is_color=False,
    sku='123'
)

Warehouse().add_equipment(Printer.eq_type, Printer.__dict__)

Scan().add_item(
    name="hp",
    dpi=123,
    sku='h-11-22-32'
)

Warehouse().add_equipment(Scan.eq_type, Scan.__dict__)

Xerox().add_item(
    name='xerox',
    is_color=True,
    sku='xe-11-22'
)

Warehouse().add_equipment(Xerox.eq_type, Scan.__dict__)

Warehouse().get_full_qty()
Warehouse().get_assigned_qty()
Warehouse().get_in_stock_qty()
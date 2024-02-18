class Employee:
    vacation_days = 28
# remaining_vacation_days = None

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days
# Сюда добавьте новый атрибут remaining_vacation_days

    def consume_vacation(self, days_gone):

# self.remaining_vacation_days = Employee.vacation_days
        self.remaining_vacation_days -= days_gone

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

    # Сюда добавьте методы consume_vacation и get_vacation_details.

# Пример использования класса:


employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(12)
print(employee.get_vacation_details())

employee1 = Employee('John', 'Smith', 'м')
employee1.consume_vacation(7)
print(employee1.get_vacation_details())

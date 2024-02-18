class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

    def get_unpaid_vacation(self, beginning_date: str, day_quantity: int):
        return f'Начало неоплачиваемого отпуска: {beginning_date}, \
            продолжительность: {day_quantity} дней.'


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee.

# Пример использования:


full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')

full_time_employee.consume_vacation(7)
print(full_time_employee.get_vacation_details())

print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')


print(part_time_employee.get_vacation_details())

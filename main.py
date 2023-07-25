import sqlite3

connection = sqlite3.connect("mydatabase.db")
sql = connection.cursor()
# sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, age INTEGER, grade TEXT);')
# sql.execute('INSERT INTO students (id, name, age, grade) VALUES (4, "Sashaa", 21, "10A");')
# connection.commit()
def get_student_by_name(name):
    print(sql.execute(f"SELECT name, age, grade  FROM students WHERE name='{name}';").fetchall())
def update_student_grade(name, grade):
    sql.execute(f'UPDATE students SET grade="{grade}" WHERE name="{name}";')
    connection.commit()
def delete_students(name):
    sql.execute(f'DELETE FROM students WHERE name="{name}";')
    connection.commit()

while True:
    name = str(input('Введи имя: '))
    get_student_by_name(name)
    grade = str(input('Введи новый класс: '))
    update_student_grade(name, grade)
    delete = str(input('Введите имя студента для удаления: '))
    delete_students(delete)
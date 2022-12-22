from student_database import save_db, load_db
from teacher import add_student, put_rating
from student import see_rating

def controller():
   load_db()                                                # Выгрузка данных из файла db_student.json
   case = input('Укажите себя. 1 - учитель, 2 - ученик: ')
   if case == '1':                                          # Блок кода учителя
      flag = 1
      while flag == 1:
         print('что хотите сделать?')
         act = input('1 - записать ученика, 2 - выставить оценку, 0 - выйти из программы\nВвод: ')
         if act == '1':
            add_student()
         elif act == '2':
            put_rating()
         elif act == '0':
            flag = 0
      else:
         save_db()                                          # Сохранение данных в файл db_student.json
   elif case == '2':                                        # Блок кода ученика
      flag = 1
      while flag == 1:
         last_name = input('Введите фамилию ученика или 0 для выхода из программы\nВвод: ')
         if last_name == '0':
            flag = 0
         else:
            see_rating(last_name)
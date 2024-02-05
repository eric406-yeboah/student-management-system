from student import Student
from tabulate import tabulate
# database
student_database=[]


def wellcome_screen():
    user_response=int(input('*****student management system*****\n 1.add student \n 2.view all student\n 3.update student info\n '
          '4.delete student info\n 5.search for student\n 6.exit app\n provide valid option:'))
    
    # calling a function to determine user choose option
    user_choosen_option(user_response)
    
def user_choosen_option(user_response):
    if user_response==1:
        add_student()
        
    elif user_response==2:
        view_student()
        
    elif user_response==3:
        update_student()
    
    elif user_response==4:
        delete_student_info()
        
    elif user_response==5:
        search_student()
        
    elif user_response==6:
        exit
        
    else:
        print('invalid option,try again!!!')
    wellcome_screen()
        
        
# function to handle adding student
def add_student():
    print('**** provide new student information ****\n')
    while True:
     student_id=input('enter student id :')
     if student_id :
         break
     else:
         print('student id cannot be empty, please enter student id \n')
         
    while True:
      first_name=input('enter first name :')
      if first_name:
           break
      else:
          print('first name cannot be empty,please enter your first name')

    while True:
     last_name=input('enter last name :')
     if last_name:
         break
     else:
         print('last_name cannot be empty,enter your last name')
         
    while True:
     age=int(input('enter age  :'))
     if age:
         break
     else:
         print('please enter your age')
         
    while True:
     gender=input('enter gender :')
     if gender:
         break
     else:
         print('please enter gender')
        
    # create instance of class ,which will make us get an objsct
    student = Student(student_id,first_name,last_name,age,gender) 
     
    student_database.append(student)  
    print(f'{first_name} {last_name} has been saved successfully \n')
    
def view_student(): 
    print('**** student information ****')
    if len(student_database)==0:
        print('no information to view')
    else:
        student_table=[]
        for student in student_database:
            student_table.append([student.student_id,f'{student.first_name},{student.last_name}',student.age,student.gender])
        headers=['student id' ,'full name', 'age','gender']
        print(tabulate(student_table,headers=headers,tablefmt='grid'))
    
    
def update_student():
    if len(student_database)>0:
       user_id=input('enter student id:')
       for student in student_database:
           if student.student_id==user_id:
              print('***choose data to change ***\n firstName(f)\n lastName(l)\n age(a)\n gender(g)')
              user_change=input('enter what to change :')
              
              if user_change=='f':
                nfname=input('enter new first name :')
                student.first_name=nfname
              elif user_change=='l':
                nlname=input('enter new last name :')
                student.last_name=nlname
              elif user_change=='a':
                nage=input('enter new age :')
                student.age=nage
              elif user_change=='g':
                ngender=input('enter new gender :')
                student.gender=ngender
              print('student information updated successfully')
              return
           else:
                print('student id not found')  
    else:
        print('No student record to update')
    
    
def delete_student_info():
    if len(student_database)>0:
        user_id=input('enter student id:')
        for student in student_database:
           if student.student_id==user_id:
               print('Are you sure? Y/N')
               user_option=input('enter your choice :')
               
               if user_option=='Y':
                   student_database.remove(student)
                   print('deleted successfully')
               elif user_option=='N':
                   print('record intact')
           else:
                print('student id not found')       
    else:
       print('no student record to delete')            
     
def search_student():
    if len(student_database)>0:
     user_id=input('enter student id:')
     for student in (student_database):
        if student.student_id==user_id:
            print(f'student id:{student.student_id}\n firstname:{student.first_name}\n lastname:{student.last_name}\n age:{student.age}\n gender:{student.gender}')
        
        else:
         print('student not found')          
    else:
        print('no student record to search for')
                
wellcome_screen()
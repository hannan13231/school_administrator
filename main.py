import csv

#function to write or enter details in csv file
def write_into_csv(list1) :
    with open('student_info.csv', 'a', newline='') as csv_file :
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0 :
            writer.writerow([" NAME ", " AGE ", " ROLL NO ", " PHONE NO ", " EMAIL ID "])

        writer.writerow(list1)

#From here the code begins
if __name__ == '__main__':
    condition = True
    student_num = 1

    #enter details of students
    while (condition) :
        print("Enter student information for #{} student :".format(student_num))

        list1 = []

        #appending details in the list
        student_name = input("Name : ")
        list1.append(student_name)
        student_age = input("Age : ")
        list1.append(student_age)
        student_roll = input("roll no : ")
        list1.append(student_roll)
        student_no = input("Phone no. : ")
        list1.append(student_no)
        student_email = input("email id : ")
        list1.append(student_email)

        print("The entered information is - \nName: {}\nAge: {}\nROll no: {}\nPhone no: {}\nEmail id: {}"
              .format( list1[0], list1[1], list1[2], list1[3], list1[4]))

        check = input("Is the entered  information is correct (yes \ no) : ")
        if check == 'yes' :

            write_into_csv(list1)
            student_num = student_num + 1
            continue_check = input("If you want to enter another students information (yes / no) : ")
            if continue_check == 'yes' :
                condition = True
            elif continue_check == 'no' :
                condition = False
        elif check == 'no' :
            print("Please re enter the values!")

    #Show details of the students
    show_csv = input("Show detail of each students ? (yes / no) : ")
    if show_csv == 'yes' :
        file = open("student_info.csv", "r")
        for x in file :
            print(x)
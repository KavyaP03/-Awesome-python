if __name__=="__main__":
  condition=True
  student_num=1
  while(condition):
     student_info=input("Enter the student information in the following format (s.no, roll_number, name,class,DOB, contact_number, E-Mail_ID:)")
     print("Entered information:"+student_info)
     student_info_list=student_info.split(' ')
     print("Entered split up information is: "+str(student_info_list))
     print("The entered information is: \ns.no: {}\nroll_number: {}\nname: {}\nclass: {}\nDOB: {}\ncontact_number: {}\nE-Mail.ID: {}".format(student_info_list[0],student_info_list[1],
       student_info_list[2],student_info_list[3],student_info_list[4],student_info_list[5],
       student_info_list[6]))

     choice_check=input("Is entered information correct ?(yes/no)")
     if choice_check=="yes":
       condition_check=input("Enter (yes/no)if you want to enter the another student information: ")
       if condition_check=="yes":
             condition =True
       elif condition_check=="no":
              condition =False
     elif choice_check=="no":
          print("Please re-enter the correct information ")

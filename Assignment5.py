#Exercise 1
# filename=open("C:\\Users\\hp\\PycharmProjects\\D42_PythonProject\\Assignment5.txt",'r')
# print(filename.read())

#Exercise 2
# source_file=open("C:\\Users\\hp\\PycharmProjects\\D42_PythonProject\\Assignment5.txt",'r')
# destination_file=open("C:\\Users\\hp\\PycharmProjects\\D42_PythonProject\\CopiedAssignment5.txt",'w')
# destination_file.write(source_file.read())
# source_file.close()
# destination_file.close()
# print("File copied successfully")
# #reading the contents in the destination file
# destination_file=open("C:\\Users\\hp\\PycharmProjects\\D42_PythonProject\\CopiedAssignment5.txt",'r')
# print(destination_file.read())
# destination_file.close()

#Exercise 3
# with open("C:\\Users\\hp\\PycharmProjects\\D42_PythonProject\\Assignment5.txt",'r') as filename:
#     data = filename.read()
#     print(data)
#     print(data.split())
#     print(len(data.split()))

#Exercise 4
# user_input=input("Enter a string to convert to an integer: ")
# try:
#     number=int(user_input)
#     print("The integer value is: ",number)
# except ValueError:
#     print("Error:The input is not a valid integer.")

#Exercise 5
# user_input=input("Enter a list of integers separated by spaces: ")
# string_list=user_input.split()
# integers=[int(num) for num in string_list]
# try:
#     for num in integers:
#         if num < 0:
#             raise ValueError("Negative integers are not allowed.")
#     print("All integers are valid. ")
# except ValueError as e:
#     print(f"Error: {e}")

#Exercise 6
# user_input=input("Enter a list of integers separated by spaces: ")
# numbers= [int(num) for num in user_input.split()]
# try:
#     if len(numbers)==0:
#         print("The list can not be empty.")
#     else:
#         average=sum(numbers)/len(numbers)
#         print("The average is: ",average)
# except ValueError:
#     print("Error: Invalid input.Please enter only integers. ")

#Exercise 7
filename=input("Enter the filename: ")
try:
    with open(filename,'w') as file:
        file.write("Hello,world!")
    print("The string has been written to the file successfully.")
    with open(filename,'r') as file:
        print("Contents of the file:",file.read())
except Exception as e:
    print(f"Error: {e}")








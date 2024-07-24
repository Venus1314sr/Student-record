# Write a program to count the occurrence of word "INDIA" in a text file India.txt
print("This is a program to count the occurrence of word 'INDIA' in a text file India.txt ")
def count_occurrences_of_india(file_path):
    word_to_count = "INDIA"
    count = 0
    with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word == word_to_count:
                        count += 1
        
    print(f"The word '{word_to_count}' occurs {count} times.") 



file_path1= "c:\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\India.txt"
count_occurrences_of_india(file_path1)

print("-------------------------------------------------------------------------------------")


# Write a program to count and display the lines starting with "T" in a text file story.txt
print("This is a program to count and display the lines starting with 'T' in a text file story.txt")
def count_and_display_lines_starting_with_t(file_path):
    count = 0

    with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('T'):
                    print(line.strip())  # Display the line
                    count += 1
        
    print(f"Total number of lines starting with 'T': {count}")

file_path2 = 'c:\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\story.txt'  
count_and_display_lines_starting_with_t(file_path2)


print("---------------------------------------------------------------------------")









# Write a program to count the number of vowels and Consonants in a file "Myfile.txt"
print("This is a program to count the number of vowels and Consonants in a file Myfile.txt")
def count_vowels_and_consonants(file_path):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    

    with open(file_path, 'r') as file:
            text = file.read()
            
            for char in text:
                if char in vowels:
                    vowel_count += 1
                elif char in consonants:
                    consonant_count += 1
        
    print(f"Total number of vowels: {vowel_count}")
    print(f"Total number of consonants: {consonant_count}")


file_path3 = 'c:\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\Myfile.txt'  
count_vowels_and_consonants(file_path3)



print("----------------------------------------------------------------------------")




# Write a program to count and display number of words starting with "I" in a file Word.txt
print("This is program to count and display number of words starting with 'I' in a file Word.txt")

def count_and_display_words_starting_with_i(file_path):
    count = 0
    
    with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word.startswith('I'):
                        print(word)
                        count += 1
        
    print(f"Total number of words starting with 'I': {count}")

file_path4 = ':\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\Word.txt'  
count_and_display_words_starting_with_i(file_path4)




print("-----------------------------------------------------------------------------------")





# Write a program to display the lines having more than five words in a text file Notes txt
print("This is a program to display the lines having more than five words in a text file Notes txt")
def display_lines_with_more_than_five_words(file_path5):
     with open('file_path','r') as file:
          for line in file:
               words = line.split()
               if words.count>5:
                    print(line.strip())
        




file_path5=':\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\Notes.txt'
display_lines_with_more_than_five_words(file_path5)



print("---------------------------------------------------------------------------------------")






# Write a program to create a binary fine "Stu dat" and Enter students rollno. Name and Marks till the user wants.
print("This is a program to create a binary fine 'Stu.dat' and Enter students rollno. Name and Marks till the user wants")
import pickle

def get_student_data():
    rollno = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    return {"rollno": rollno, "name": name, "marks": marks}

def write_student_data_to_file(file_path):
    student_data = []
    
    while True:
        student_data.append(get_student_data())
        more = input("Do you want to add another student? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(student_data, file)
        print("Student data written to file successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = 'Stu.dat'  # Binary file to store student data
    write_student_data_to_file(file_path)

if __name__ == "__main__":
    main()



print("------------------------------------------------------------------")


# Write a program to read a binary file "Stu dat" and display the record of students having marks greater than 81
print("This is a program to read a binary file 'Stu.dat' and display the record of students having marks greater than 81")
import pickle

def read_student_data_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            student_data = pickle.load(file)
            return student_data
    except FileNotFoundError:
        print(f"File at {file_path} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def display_students_with_high_marks(students, threshold):
    print(f"Students with marks greater than {threshold}:")
    for student in students:
        if student['marks'] > threshold:
            print(f"Roll No: {student['rollno']}, Name: {student['name']}, Marks: {student['marks']}")

def main():
    file_path = 'Stu.dat' 
    students = read_student_data_from_file(file_path)
    if students:
        display_students_with_high_marks(students, 81)

if __name__ == "__main__":
    main()

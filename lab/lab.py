# First1: write the function in python  to read the contents  from  a text file "ABC.txt", line  by line and display the same on the screen.
print("This is the function in python  to read the contents  from  a text file 'ABC.txt', line  by line and display the same on the screen.")
def read_and_display_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())


file_path = "c:\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\ABC.txt"
read_and_display_file(file_path)


print("----------------------------------------------------------------------------------------")

# Second: write the function in python to count and display  the total number of words in a txt file 'ABC.txt'
print("This is the function in python to count and display  the total number of words in a txt file 'ABC.txt' ")
def count_and_display_words(file_path):
    with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
        
    print(f"Total number of words: {word_count}")



file_path2= "c:\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\ABC.txt"
count_and_display_words(file_path)


print("-------------------------------------------------------------------------------------------")




# third: write the function in python to count uppercase characters in text file 'ABC.txt
print("This is the function in python to count uppercase characters in text file 'ABC.txt ")
def count_uppercase_characters(file_path):
     uppercase_count = 0
     with open(file_path,'r') as file:
        text = file.read() 
        for char in text:
            if char.isupper():
                    uppercase_count += 1
     print(f"Total number of uppercase characters: {uppercase_count}")


file_path3= "c:\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\ABC.txt"
count_uppercase_characters(file_path)

print("-------------------------------------------------------------------------")



# fourth: write the function display_words() in python to read lines from a text file "story.txt,display, those words. which are less than 4 characters"

print("This is the he function display_words() in python to read lines from a text file 'story.txt',display, those words. which are less than 4 characters")
def display_words(file_path):
     with open(file_path,'r') as file:
          for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)



file_path4= "c:\\Users\\aj\\Documents\\Data-visualization\\Python\\20july-LabAssignment\\ABC.txt"
display_words(file_path)
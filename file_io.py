# writing to a file

with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is an example of writing to a file.\n')


# reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print('File content:')
    print(content)

# Taking user input from the console and writing it to a file
user_input = input("Enter some text to write to the file: ")
print("you entered:", user_input)

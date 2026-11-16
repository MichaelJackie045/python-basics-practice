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

# appending user input to the file
user_input = input("Enter some text to append to the file: ")
with open('example.txt', 'a') as file:
    file.write(user_input + '\n')

# reading the updated file content
with open('example.txt', 'r') as file:
    content = file.read()
    print('Updated file content:')
    print(content)

print('Enter lines of text (type "exit" to finish):')
with open('user_input.txt', 'w') as file:
    while True:
        line = input()
        if line.lower() == 'exit':
            break
        file.write(line + '\n')

with open('user_input.txt', 'r') as file:
    content = file.read()
    print('Content of user_input.txt:')
    print(content)
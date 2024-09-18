print('Welcome to Elite 101 Chatbot!')

name = input('Please enter your name: ')

print(f'Nice to meet you {name}!')

age = input('How old are you?: ')

print(f'Welcome {name}! Oh to be {age} again! How can I help you today?\n')

def display_menu():
  print("Please Choose from the following options:")  
  print("1. Placeholder Option 1") 
  print("2. Placeholder Option 2")   
  print("3. Placeholder Option 3")  
  print("4. Exit the conversation\n")  

display_menu()

def user_selection():
  user_choice = int(input('Enter a number between 1-4: '))
  if user_choice == 1:
    print('Placeholder Option 1')
  elif user_choice == 2:
    print('Placeholder Option 2')
  elif user_choice == 3:
    print('Placeholder Option 3')
  elif user_choice == 4:
    print(f'Goodbye {name}! Have a great day!') 
    exit()

user_selection()
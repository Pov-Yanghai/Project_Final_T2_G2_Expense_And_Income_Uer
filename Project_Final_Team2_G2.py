#User _Login 

   
def user_login():
    print("Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Mock user data
    users = {
        "admin": "password123",
        "user1": "user1password",
        "user2": "user2password"
    }
    
    if username in users and users[username] == password:
        print("Login successful")
        return True
 
#test 
hello
   
user_login()

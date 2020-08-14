class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print("Hello，" + self.first_name.title() + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('le', 'xiaoyuan')
user.describe_user()
user.greet_user()

user2 = User('乐', '小猿')
for i in range(5):
    user2.increment_login_attempts()

print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)

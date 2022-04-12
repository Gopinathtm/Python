class User:
    """Desceibe user"""
    def __init__(self, full_name):
        self.full_name = full_name
        self.login_attempt = 0

    def greet_user(self):
        print(f"Welcome {self.full_name.title()}")

    def login_attempts(self):
        print(f"The user has {self.login_attempt} login attempts ")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0


class Privilages:
    """Desceibe privilages of user"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can be a user", "and so on..."]

    def show_privileges(self):
        print("The privileges of admin are as follows")
        for x in self.privileges:
            print(f"\t{x}")


class Admin(User):
    """Created a child class Admin and added special attributes to it"""
    def __init__(self, fullname):
        super().__init__(fullname)
        self.privileges = Privilages()

    def greet_user(self):
        print(f"Welcome admin Mr.{self.full_name.title()}")


user = User("subin")
admin = Admin("gopi")
admin.greet_user()
admin.privileges.show_privileges()


"""
Output
user = User("subin")
admin = Admin("gopi")
admin.greet_user()
admin.privileges.show_privileges()

"""

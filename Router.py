class Router:
    def __init__(self, users, password=''):
        self.users = users
        self.password = password

    def add_user(self, new_user):
        if isinstance(new_user, str):
            if len(self.users) < 10:
                self.users.append(new_user)
            else:
                print('Router already has maximum users.')
        else:
            print('Name of user must be a string.')

    def change_pw(self, new_password):
        if isinstance(new_password, str):
            if len(new_password) > 6:
                self.password = new_password
            else:
                print('Password must have more than 7 characters.')
        else:
            print('Password must be a string.')

    def __str__(self):
        return f'Users:{self.users} Password: {self.password}'

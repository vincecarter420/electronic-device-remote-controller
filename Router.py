class Router:
    def __init__(self, name: str, users: list, password: str, status: str):
        '''creates name, users, password and status values'''
        self.__name = name
        self.users = users
        self.__password = password
        self.status = status

    @property
    def name(self):
        '''getter'''
        return self.__name

    @property
    def password(self):
        '''getter'''
        return self.__password

    def change_pw(self, new_password):
        '''changing password function
        new password must be string if not print 'Password must be a string'
        and new password must have more than 7 character
        if not print 'Password must have more than 7 characters.' '''
        if isinstance(new_password, str):
            if len(new_password) > 6:
                self.__password = new_password
            else:
                print('Password must have more than 7 characters.')
        else:
            print('Password must be a string.')

    def open_close(self, oc):
        '''simple open and close function'''
        self.status = oc

    def add_user(self, new_user):
        '''adding user function
        new user name must be string if not print 'Name of user must be a string'
        and users that use a router must has less than 11 users
        if not print 'Router already has maximum users.' '''
        if isinstance(new_user, str):
            if len(self.users) < 10:
                self.users.append(new_user)
            else:
                print('Router already has maximum users.')
        else:
            print('Name of user must be a string.')

    def __str__(self):
        '''print out router status
        example Router1-User: ['mom','dad','bro','sis'] Password: abc123123-
        Status: open'''
        return f'{self.name}-Users: {self.users} Password: ' \
               f'{self.__password} Status: {self.status}'

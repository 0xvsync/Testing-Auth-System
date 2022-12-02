import hashlib
from Exceptions.handler import *

"""
    Create a Initiator, for the authentication.
"""
class My_AuthenticationSystem:
    """
     My_AuthenticationSystem DATA TYPE.
    """
    D_TYPE: None = None
    """
    - ARGUMENTS
     - username[str],
     - password[str]
    -> None[Type]
    
    - DATABASE
     - Create a temporary database in a array[:list]
    """
    def __init__ (self, username: str, password: str) -> None:
        self.AUTH_VERSION: int = 1
        self.__DB__: list = ["Test:532eaabd9574880dbf76b9b8cc00832c20a6ec113d682299550d7a6e0f345e25"]
        self.username: str = username
        self.password: str = password

    #def types (self) -> dict[dict[str,str], str]:

    """
        Call the hash function within the initiator variable.
         - Return a dictionary polluted with the username(self.username) hashed
           - password(self.password) hashed
        
         - Return dict containing a dict, value of the variable in dict being[str, str]
    """
    def hash (self) -> dict[dict[str, str], str]:
        try:
            return {
                "ARGS_" :
                    {
                        "Username": self.username,
                        "Password": self.password
                    },
                    "Username": hashlib.sha256(self.username.encode()).hexdigest(),
                    "Password" : hashlib.sha256(self.password.encode()).hexdigest()
                    }
        except:
            raise CantHashError("Couldn't hash polluted credentials.")

    """
        Authenticate.
    """
    def AUTHENTICATE (self, _hash_dict_: dict) -> None:
        for _ in self.__DB__:
            if self.username == _.split(":")[0] and _hash_dict_['Password'] == _.split(":")[1]:
                return True
            else:
                pass
        raise InvalidCredentialsError("Authentication has not passed.")

if __name__ == '__main__':
    """
        TestMy_AuthenticationSystem Documentation.
    """
    user_input: str = input(":")
    password_input: str = input(":")

    constructor: My_AuthenticationSystem.D_TYPE = My_AuthenticationSystem(user_input, password_input)
    hash_constructor: My_AuthenticationSystem.D_TYPE = constructor.hash()
    authenticate: My_AuthenticationSystem.D_TYPE = constructor.AUTHENTICATE(hash_constructor)

    #Example
    if authenticate:
        print("Authentication passed.")
    else:
        print("Authentication has not passed.")

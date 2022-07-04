"""
    File for Password Generation
"""

# Import libraries
import random
import string


# Character dictionary
characters = {
    "letters": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers":   "0123456789",
    "specialChars": "!#$%&*+-?@|"

}

# Password generator class
class PasswordGenerator:
    """
    Class to generate password or a list of passwords
    Args:
        min_length: (int) minimum password length.
        schars_num: (int) number of special characters in the password.
        numbers_num: (int) number of numbers in the password.
        count: (int) number of passwords that must be created.
    """
    def __init__(self, min_length = 6, schars_num = 1, numbers_num = 1, count = 1):
        self.min_length = min_length
        self.schars_num = schars_num
        self.numbers_num = numbers_num
        self.count = count

    def generate_password(self):

        """
        Method to generate a secure random password.
        :return
            (string): unique string password.
        """
        
        # Create a list for random letters with the minimum password length
        letters = []
        for i in range(self.min_length):
            char = random.choice(characters["letters"])
            letters.append(char)
        
        # Create a list for special characters
        specialChars = random.sample(characters["specialChars"], self.schars_num)

        # Create a list for random number
        numbers = random.sample(characters["numbers"], self.numbers_num)

        # Create a list of the desired chars
        password_list = letters + specialChars + numbers

        # Shuffle the password
        random.shuffle(password_list)

        # Join the password list to a string
        password = "".join(password_list)

        # Return a password string
        return password

    
    def generate_passwords_list(self):
        """
        Method to generate a passwords list.
        :return
            (list): list of passwords.
        """

        # Create a passwords list
        passwords_list = []
        for i in range(1, self.count+1):
            password = self.generate_password()
            passwords_list.append({i:password})

        # Return a password string
        return passwords_list






import random, string
'''generate a strong password that has all the characters - diamondrichie'''

class PasswordGenerator:
    def __init__(self):
        self.range = range   #set the range of the characters

        self.Generate()  #fires up automatically from here
        
    def Generate(self):
        lower = ''.join(random.choice(string.ascii_lowercase) for _ in self.range(4))
        upper = ''.join(random.choice(string.ascii_uppercase) for _ in self.range(2))
        digit = ''.join(random.choice(string.digits) for _ in self.range(3))
        punc = ''.join(random.choice(string.punctuation) for _ in self.range(2))

        print("Generated password:", lower + upper + digit + punc)

PasswordGenerator()
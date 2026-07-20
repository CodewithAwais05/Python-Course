# making methods or attributes private for security
# we can make private by putting (__) before name
# private members are only accessible within the class

class Person:
    __name = "anonymous"  # private name

    def __hello(self):  # private function
        print("Hello World!")
    
    def welcome(self):  # public function
        print("Welcome buddy!!")
        self.__hello()

p1 = Person()
# p1.__hello()  # this shows error as we make this function private
p1.welcome()  # ths runs as this function is public
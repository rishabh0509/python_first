class Dog(object):
    def __init__(self,name):
        self.nam = name
        
    
    def speak(self):
        print('Hi I am', self.nam)

    def change_name(self, name):
        self.nam = name

tim = Dog('Tim')
fred = Dog('Fred')
tim.change_name('John')
tim.speak()
fred.speak()

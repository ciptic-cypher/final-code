# polymorphism is expressing anytjhing in various forms 

# data types can be treated for the same purpose 

# for example 
# in built functions 
# the len function

import pyttsx3
def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

print(len("123"))
print(len([1,2,3]))
print(len((1,2,3)))

# for user defined
def hello(a=0,b=1,c=2,*var):
    print("a= %d, b=%d, c=%d",a,b,c,var)

hello()
hello(1)
hello(1,2)
hello(1,2,3,4)

# using class

class Kailash:
    def hello(self):
        print("hello Kailash!")

    def bye(self):
        print("Bye Kailash!")

class speak(Kailash):
    def say(self):
        Speak("I can say!")

hello = speak()
hello.hello()
hello.say()
hello.bye()

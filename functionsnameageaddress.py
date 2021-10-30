def getName():
    _name = input("Please enter your full name: ")
    return _name
def getAge():
    _age = int(input("Please enter your age: "))
    return _age
def getAddress():
    _address = input("Please enter your full address: ")
    return _address
def display(nameF, ageF, addressF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF} .")

#1 ask for name and save to variable
name = getName() 
#2 ask for age and save to variable
age = getAge()
#3 ask for address and save to variable
address= getAddress()
#4 add display for name, age, and address
display(name,age,address)
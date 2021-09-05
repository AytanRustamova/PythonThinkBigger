class User():
    def __init__(self):
        self.ad= 'Ayten'
        self.soyad = 'Rustemova'
        self.age = 22
        self.password = 'ayten12345'
        self.email = 'aytn1973@gmail.com'


    a = 5
    b = 6
    def login(a,b):
        c = a+b
        print(c)

    login(a, b)
    ad = "Ayten"
    soyad = "Rustemova"

    def register(ad, soyad):
        checkIn = ad + soyad

        print(checkIn)

    register(ad, soyad)



user = User()

userProperties = vars(user) #  obyektin icindeki dictionary'ni return edir

# - hansı property-ləri olduğunu və onların value-sunu
for item in userProperties:
    print(item, ':' , userProperties[item])



# dir() methodu istifade olunan butun methodlarin listin cixardir.Buna built in functionlarda daxildir. 
# - hansı metodlarının olduğunu və nə return etdiyini
# 1.Yol
methodInObject = [ method for method in dir(User) if method.startswith('__') is False]
print(methodInObject)
# 2.Yol
newArray = []
for method in dir(User):
    if method.startswith('__'):
        method = dir(User).remove(method)
    newArray.append(method)

print(newArray)
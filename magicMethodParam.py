class User():
    def __init__(self,ad,soyad,age):
        self.ad= ad
        self.soyad = soyad
        self.age = age


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

# Bu prosesi if'in icinde yaza bilmedim. Return edenden sonra print ede bilmediyim ucun yeni function yaradiram.
def Str(param):
    newrArray = []
    for i in range(len(param)):
        if i % 2 == 1:
            newrArray.append(param[i].upper())
        else:
            newrArray.append(param[i].lower())
    return ''.join(newrArray)


user = User('Ayten', 'Rustemova', 22)

typeofObj = type(user)

def magicMethod(param):
    if type(param)is list:
        for item in param:
         print(item)
    elif type(param) is int:
        param = param * param 
        print(param)
    elif type(param) is typeofObj:
        for property, value in vars(param).items():
            print(property, ":", value)
    elif type(param) == str:
        print(Str(param))
        
        
           





# magicMethod([2,3,4,5])
# magicMethod(12)
# magicMethod(user)
magicMethod('ayten')







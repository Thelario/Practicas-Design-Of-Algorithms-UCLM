import math

# Esta función se tiene que implementar porque la función pow de ser en el lenguaje puede tener errores de redondeo.
def ExpMod(a, n, z):
    usePythonPowMethod = False
    if (usePythonPowMethod):
        return pow(a, n, z)
    else:
        i = n
        x = a
        r = 1

        while (i > 0):
            if (i % 2 != 0):
                r = r * x % z
            x = x * x % z
            i = int(i / 2)
        
        return r
       
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Alice:

    def __init__(self, dh, x):
        self.x = x 
        self.dh = dh
        self.b = 0

    def SetBob(self, bob):
        self.bob = bob

    def ComputePublicValue(self):
        self.z1 = int(ExpMod(self.dh.GetN(), self.x, self.dh.GetP()))

    def ComputePrivateKey(self):
        self.ka = int(ExpMod(self.b, self.x, self.dh.GetP()))
        print("Secret key for Alice is: " + str(self.ka))

    def SendPublicValue(self):
        self.dh.SendMessage(self.z1, self.bob)

    def ReceiveMessage(self, message):
        self.b = message
        print("Alice received from Bob message: " + str(message))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Bob:

    def __init__(self, dh, y):
        self.y = y 
        self.dh = dh
        self.a = 0
        
    def SetAlice(self, alice):
        self.alice = alice

    def ComputePublicValue(self):
        self.z2 = int(ExpMod(self.dh.GetN(), self.y, self.dh.GetP()))

    def ComputePrivateKey(self):
        self.kb = int(ExpMod(self.a, self.y, self.dh.GetP()))
        print("Secret key for Bob is: " + str(self.kb))

    def SendPublicValue(self):
        self.dh.SendMessage(self.z2, self.alice)

    def ReceiveMessage(self, message):
        self.a = message
        print("Bob received from Alice message: " + str(message))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Diffie_Hellman:

    # Establecemos el primo p y el generador n al crear un objeto de tipo Diffie_Hellman
    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.z1 = 0
        self.z2 = 0

    def GetP(self):
        return self.p

    def GetN(self):
        return self.n

    def SendMessage(self, message, destiny):

        # La siguiente estructura if/else la utilizamos para guardar los valores de z1 y z2 para poder comprobar 
        if (isinstance(destiny, Alice)):
            self.z1 = message
        else:
            self.z2 = message

        destiny.ReceiveMessage(message)

    def BruteForceAttack(self, z1, z2):

        for i in range(0, 999999999999):
            if (int(ExpMod(self.n, i, self.p)) == z1):
                print("x: " + str(i))
                z = ExpMod(z2, i, self.p)
                print("Secrete Key: " + str(z))
                return i
            if(int(ExpMod(self.n, i, self.p)) == z2):
                print("y: " + str(i))
                z = ExpMod(z1, i, self.p)
                print("Secrete Key: " + str(z))
                return i
        
        print("No key found")
        return -1

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

dh = Diffie_Hellman(313213323123, 52313)

print("")
dh.BruteForceAttack(73034832664, 999999999999999)
print("")

onlyTestAttack = True

if (onlyTestAttack == False):

    alice = Alice(dh, 20236125)
    bob = Bob(dh, 2930957)

    alice.SetBob(bob)
    bob.SetAlice(alice)

    print("")

    alice.ComputePublicValue()
    alice.SendPublicValue()

    bob.ComputePublicValue()
    bob.SendPublicValue()

    print("")
    
    alice.ComputePrivateKey()
    bob.ComputePrivateKey()


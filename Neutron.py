class Number:
    def __init__(self,atomic_number,atomicmass_number):
        self.Z = atomic_number
        self.A = atomicmass_number


    def NuclearNotation(self):
        N = self.A - self.Z #N is neutron number
        return N

Z = int(input("enter Atomic number : "))
A = int(input("enter Atomicmass :"))

s1 = Number(Z,A)
print("total neutron : ",s1.NuclearNotation())

class kendaraan:
    kecepatan = 0
    cc = 0

    #constractor
    def __init__(self):
        self.roda = 0
    
    def nyala(self):
        print('Boooom')
    
    def maju(self):
        if self.roda > 0:
            self.kecepatan = self.kecepatan + 10
    
    def mundur(self):
        pass

#inheritance
class Motor(kendaraan):
    pass

m1 = Motor()
m1.nyala()
m1.roda = 3
print(m1.roda)
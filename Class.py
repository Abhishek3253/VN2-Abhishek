class Computer():
    def __init__(self , cpu ,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(" configuration is ",self.cpu ,self.ram)

cmp1=Computer("i5",16)
cmp2=Computer("i3" ,8)

cmp1.config()
cmp2.config()
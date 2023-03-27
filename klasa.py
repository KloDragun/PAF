class cestica:
    def __init__(c,mass,x,velocity):
        c.masa=mass
        c.polozaj=x
        c.brzina=velocity

    def print(c):
        print(c.masa)
        print(c.polozaj)
        print(c.brzina)

    def changevel(c,v):
        c.brzina=c.brzina+v

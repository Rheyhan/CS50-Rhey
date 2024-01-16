from project import imagedownloader

def testurl():
    a=imagedownloader("T-34")
    assert type(a.googleimageURL)==str

def stringthing():
    a=imagedownloader("T-72B")
    assert str(a)=="You're looking for T-72B."

#idk i use jupyter for debug.
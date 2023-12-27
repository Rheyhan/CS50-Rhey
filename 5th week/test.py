namelist=[]
string="Adieu, adieu, to "
while(True):
    try:
        a=str(input("Name: "))
        namelist.append(a)
        
    except EOFError:
        if len(namelist)==1:
            print(string+namelist[0])
        elif len(namelist)==2:
            print(f'{string}{namelist[0]} and {namelist[1]}')
        elif len(namelist)>2:
            string+=' '.join(i for i in [f'{j},' for j in namelist[:-1]])
            print(f'{string} and {namelist[-1]}')

        break
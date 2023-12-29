def main():
    plate = is_valid(input("Plate: "))
    print(f'Output: {plate}')


def is_valid(s):
    firstcond=False
    secondcond=False
    thirdcond=False
    fourthcond=True

    if len(s) >=2 and len(s) <=6:
        secondcond=True
        if s[:2].isalpha(): firstcond=True
        
        numindex=[i for i in range(len(s)) if s[i].isnumeric()]

        if numindex==[]: thirdcond=True
        else: 
            idk=True
            for i in range(len(numindex)-1):
                if -int(numindex[i])+int(numindex[i+1]) !=1:idk=False
            if s[numindex[0]]!="0" and numindex[-1]+1==len(s) and idk: thirdcond=True
        
        for i in s:
            if i.isalnum(): pass
            else: fourthcond=False
            
    if firstcond and secondcond and thirdcond and fourthcond:
        return ("Valid")
    else:
        return ("Invalid")

if __name__ == "__main__":
    main()

main()
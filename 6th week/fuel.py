def main():
    idk=str(input("Fraction: "))
    idk=convert(idk)
    print(gauge(idk))

def convert(fraction):
    x, y=fraction.split("/")
    z= round(int(x)/int(y), 2)*100
    return int(z)

def gauge(percentage):
        if percentage>=99 and percentage<=100:
            return ("F")
        elif percentage>=0 and percentage<=1: return ("E")
        elif percentage> 0 and percentage<100:
            return (f'{percentage}%')

if __name__ == "__main__":
    main()

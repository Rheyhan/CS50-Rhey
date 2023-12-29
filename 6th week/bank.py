
def main():
    a=value(str(input("Input: ")))
    print(f'Output: {a}')

def value(greeting):
    a=str(greeting).lower()
    a=''.join(i for i in a if i.isalpha() or i.isspace()).split(" ")
    a=[i for i in a if i.isalpha()]

    if a[0]=="hello":
        return 0

    elif a[0].startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

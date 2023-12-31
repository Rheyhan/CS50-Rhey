forbidden=[]
for i in ["a", "i", "u", "e", "o"]: forbidden.append(i.upper()); forbidden.append(i.lower())

def main():    
    a=shorten(str(input("Input: ")))
    print(f'Output: {a}')
       
def shorten(word):    
    return ''.join([i for i in word if i not in forbidden])

if __name__ == "__main__":
    main()
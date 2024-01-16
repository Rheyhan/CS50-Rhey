from bs4 import BeautifulSoup
import requests
from PIL import Image
import os
import re
from tqdm import tqdm

class imagedownloader:
    def __init__(self, whatyouwannasearch: str=None):
        if whatyouwannasearch==None: raise ValueError("Input what you gonna search!")
        
        self.whatyouwannasearch=whatyouwannasearch
        self.getURL()
        self.r=self.getrequest()
    
    def getURL(self):
        googlesearch="https://www.google.com/search?q="
        googleimagething="&tbm=isch&ved=2ahUKEwiyq5mu396DAxWqwaACHWsuC6IQ2-cCegQIABAA&oq=t34&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6DggAEIAEEIoFELEDEIMBOggIABCABBCxA1CeBFinCmDlC2gAcAB4AYABR4gByAGSAQEzmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=1c2kZfLsG6qDg8UP69yskAo&bih=675&biw=1396"
        self.googleimageURL=f'{googlesearch}{self.whatyouwannasearch}{googleimagething}'
    
    def getrequest(self):
        self.header = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

        try:
            r=requests.get(self.googleimageURL, headers=self.header, timeout=20)
            if r.status_code == 200:
                return r
        except ConnectionError:
            print("Check Your Connection")
    
    def start(self, 
              n: int=1, 
              savepath: str=""):
        '''
        n: int on range of 1 to 75.\n
        savepath: location of where the images are gonna be downloaded. Default on current directory.
        '''
        if n<1 or n>=75: raise ValueError("Womp womp!")
        self.n=n
        self.savepath=savepath
        self.getimagelink()
        self.saveimage()

    def getimagelink(self):
        soup=BeautifulSoup(self.r.content, "html5lib").prettify()
        temp=re.findall(r'\[\"https://encrypted[^,]+\",\d{1,10},\d{1,10}],\[\"https://[^,]+,\d{1,10},\d{1,10}]', soup)
        self.targeturl=[re.findall(r'https://[^\"]+', i)[1] for i in temp]
    
    def saveimage(self):
        counter=0
        index=-1
        idkbro=f'{self.savepath}/{self.whatyouwannasearch}'
        try:
            os.makedirs(idkbro)
        except:
            pass

        progress_bar = tqdm(total=self.n, desc="Processing")
        
        while self.n>counter:
            index+=1
            extensiontype=None
            for extension in [".jpg", ".png", ".jpeg"]:
                if re.search(extension, self.targeturl[index]):  
                    extensiontype=extension; break
                    
            if extensiontype==None: continue
            r_image=requests.get(self.targeturl[index], headers=self.header, timeout=10)
            if r_image.status_code==200:    
                with open(f'{idkbro}/{counter}{extensiontype}',"wb") as br:
                    br.write(r_image.content)
            else: print(f'Failed to download {str(self.targeturl[index])}')
            counter+=1
            progress_bar.update(1)

        progress_bar.close()
    
    def __str__(self):
        return f'You\'re looking for {self.whatyouwannasearch}.'
    
if __name__=="__main__":
    #i can use argparse in here, but idc tbh.
    whatyogonnasearch=str(input(f'Search for     : '))
    quantity= int(input(f'How many images: '))
    downloadpath= str(input(f'Download path  : '))
    imagedownloader(whatyogonnasearch).start(quantity, downloadpath)
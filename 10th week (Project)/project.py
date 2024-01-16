from bs4 import BeautifulSoup
import requests
import os
import re
from tqdm import tqdm
import argparse


class imagedownloader:
    def __init__(self, whatyouwannasearch: str=None):
        if whatyouwannasearch==None: raise ValueError("Input what you gonna search!")
        if a:=re.search(r'\S.+\S', whatyouwannasearch)[0]:
            self.whatyouwannasearch=a
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
              savepath= None):
        '''
        n: int on range of 1 to 75.\n
        savepath: location of where the images are gonna be downloaded. Default on current directory.
        '''
        if not re.search(r'\w', savepath): savepath=None
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
        if self.savepath:
            idkbro=f'{self.savepath}/{self.whatyouwannasearch}'
        else: idkbro=f'{self.whatyouwannasearch}'
        try:
            os.makedirs(idkbro)
        except:
            pass

        progress_bar = tqdm(total=self.n, desc="Processing")
        
        while self.n>counter:
            index+=1
            extensiontype=None
            for extension in [".jpg", ".png", ".jpeg"]:
                try:
                    if re.search(extension, self.targeturl[index]):  
                        extensiontype=extension; break
                except IndexError:
                    print("Can't find any image!")
                    
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
    parser = argparse.ArgumentParser(description=f'Hi! :3',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-s", "--search", help="what you gon search for")
    parser.add_argument("-n", "--quantity", default=1, help="How many images are gonna be downloaded?")
    parser.add_argument("-p", "--path", default="", help="Folder Destination")
    args = vars(parser.parse_args())
    search=args["search"]
    imagedownloader(args["search"]).start(int(args["quantity"]), args["path"])
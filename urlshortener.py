import pyshorteners
import validators

# variables 
choices = [
    "Adf.ly", 
    "Bit.ly", 
    "Chilp.it", 
    "Clck.ru", 
    "Cutt.ly", 
    "Da.gd",  
    "Is.gd", 
    "NullPointer",  
    "Os.db", 
    "Qps.ru", 
    "TinyURL.com",
    "Git.io",
]
choices1 = ""


for i in choices:
    choices1 += i + ""

choices2 = choices1.lower()

# class to apply shortener link on
class shorteners:
    @classmethod
    def adfly(cls, link):
        s = pyshorteners.Shortener(api_key='8b08bc51eab09e99796aaa0c389792b4', user_id='24364179',
                                    domain='test.us', group_id=12, type='int')
        return s.adfly.short(link)                            
    @classmethod
    def bitly(cls, link):
        s = pyshorteners.Shortener(api_key='0d902b7cbd43df9ee34d1f6b646fe671b7570c83')
        return s.bitly.short(link)
    @classmethod
    def chilpit(cls, link):
        s = pyshorteners.Shortener()
        return s.chilpit.short(link)
    @classmethod
    def clckru(cls, link):
        s = pyshorteners.Shortener()
        return s.clckru.short(link)
    @classmethod
    def cuttly(cls, link):
        s = pyshorteners.Shortener(api_key='b2425ab72c5114492d95ae6e06e4e0126ce21')
        return s.cuttly.short(link)
    @classmethod
    def dagd(cls, link):
        s = pyshorteners.Shortener()
        return s.dagd.short(link)
    @classmethod
    def gitio(cls, link):
        s = pyshorteners.Shortener()
        return s.gitio.short(link)
    @classmethod
    def isgd(cls, link):
        s = pyshorteners.Shortener()
        return s.isgd.short(link)
    @classmethod
    def nullpointer(cls, link):
        s = pyshorteners.Shortener(domain='https://0x0.st')
        return s.nullpointer.short(link)
    @classmethod
    def osdb(cls, link):
        s = pyshorteners.Shortener()
        return s.osdb.short(link)
    @classmethod
    def qpsru(cls, link):
        s = pyshorteners.Shortener()
        return s.qpsru.short(link)
    @classmethod
    def tinyurl(cls, link):
        s = pyshorteners.Shortener()
        return s.tinyurl.short(link)

#validates input to see if link is enter correctly
def linkValidate(link):
    pass

def shortenerChoice():
    global selection
    print("choose shortener type: ")
    for i in choices:
        print(i)
    selection = input()


def switch(selection):
    if selection.lower() == "adf.ly":
        print(shorteners.adfly(link))
    if selection.lower() == "bit.ly":
        print(shorteners.bitly(link))
    if selection.lower() == "chilp.it":
        print(shorteners.chilpit(link))
    if selection.lower() == "clck.ru":
        print(shorteners.clckru(link))
    if selection.lower() == "cutt.ly":
        print(shorteners.cuttly(link))
    if selection.lower() == "da.gd":
        print(shorteners.dagd(link))
    if selection.lower() == "git.io":
        print(shorteners.gitio(link))
    if selection.lower() == "is.gd":
        print(shorteners.isgd(link))
    if selection.lower() == "nullpointer":
        print(shorteners.nullpointer(link))
    if selection.lower() == "os.db":
        print(shorteners.osdb(link))
    if selection.lower() == "qps.ru":
        print(shorteners.qpsru(link))
    if selection.lower() == "tinyurl.com":
        print(shorteners.tinyurl(link))

if __name__ == "__main__":
    global link
    print('what link would you like to shorten? or type "exit" to exit')
    link = input()
    if link.lower() == "exit":
        exit()
    shortenerChoice()
    switch(selection)
    





# from bs4 import BeautifulSoup
# import os

# html = "<div>This is a DIV</div>"

# soup = BeautifulSoup(html,"html.parser")
# print(soup.div.text)


# from bs4 import BeautifulSoup
# import os
# html= "<div>ini adalah dokumen div</div><p>ini adalah paragraf halaman luar</p>"

# soup = BeautifulSoup(html,"html.parser")
# print(soup.div.text)

# from bs4 import BeautifulSoup
# import os
# html= "<div>ini adalah dokumen div</div><p>ini adalah paragraf halaman luar</p><div>y</div>"

# soup = BeautifulSoup(html,"html.parser")
# print(soup.findAll("div"))
# print(soup.findAll("div")[1])

# soup = BeautifulSoup(html,"html,parser")
# print(soup.findAll("div",{'class':'bold'}))

# [<div class="bold">ini adalah paragraf ke dua Div</div>]

# print 

from bs4 import BeautifulSoup
import os

# html="""
#         <div id="d1" class="wide">
#         <p id='p1'>ini adalah sintag paragraf</p>
#         <img src=""/>
#         <a id="a1"></a>
#         </div>
#         <div id="d2" class="small">
#         <p id='p2'>ini adalah sintag paragraf 2</p>
#         <img src=""/>
#         <a id="a2"></a>
#         </div>
# """
# soup= BeautifulSoup(html,"html.parser")
# print(soup.findAll('div',{'id':'d2'})[0].p)


# html4="""
#         <div id="d1" class="wide">
#         <p id='p1'>this is a</p>
#         <div><p>OK</p></div>
#         <img src=""/>
#         <a id="a1"></a>
#         </div>
#         <div id="d1" class="small">
#         <p id='p1'>this is a p</p>
#         <div><p>KO</p></div>
#         <img src=""/>
#         <a id="a1"></a>
#         </div>
# """
# soup=BeautifulSoup(html4,"html.parser")
# print(soup.findAll("div",{'class':'small'})[0].div.p.text)

html4="""
    <div>div1</div>
    <div>div2</div>
    <div>div3</div>
    <div>div4</div>
    <div>div5</div>
    <div>div6</div>
    <div>div7</div>
    <div>div8</div>
    <div>div9</div>
    <div>div10</div>
"""
soup=BeautifulSoup(html4,"html.parser")
# print(soup.findAll("div")[1::2])
for index,div in enumerate(soup.findAll("div")):
    if(index +1 )% 2 ==0:
        print(div)
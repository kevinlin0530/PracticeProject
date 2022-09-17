import urllib.request as req
def getData(url):
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4

    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]


pageURL="https://www.ptt.cc/bbs/movie/index.html"
count=0
getData(pageURL)
while count<2:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1


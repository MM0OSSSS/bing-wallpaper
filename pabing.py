def pa():
    import requests
    import bs4
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        } 
    url = "https://cn.bing.com/"

    res = requests.get(url, headers=head)
    res.encoding = res.apparent_encoding

    soup = bs4.BeautifulSoup(res.text, "lxml")

    tags = soup.find_all("div", class_="img_cont")

    a = tags[0]
    b = str(a)
    c = b[51:276]
    c = c[:-151]
    print(c)
    r = requests.get(c)
    pic = r.content
    with open("img.jpg","wb") as file:
       file.write(pic)

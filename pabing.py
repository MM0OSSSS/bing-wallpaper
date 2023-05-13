def pa():
    import requests
    url = "https://cn.bing.com/HPImageArchive.aspx?n=1&format=js&idx=0"
    res = requests.get(url)
    res.encoding = "UTF-8"
    a = res.text
    b = a.split(",")
    web = b[4]
    web = web.split(":")
    web = web[1]
    web = web[1:-1]
    print(web)
    f = "https://s.cn.bing.net"
    b = "_1920x1080.jpg"
    newweb = f + web + b
    print(newweb)
    res = requests.get(newweb)
    pic = res.content
    with open("img.jpg","wb") as file:
       file.write(pic)

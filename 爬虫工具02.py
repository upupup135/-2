import requests
from bs4 import BeautifulSoup
import re

def Download(url, file_path="./img/"):
    origin_url = "https://pic.netbian.com"  #给了一个原始的url，目的是和后面的img_url[0]进行拼接，得到图片地址，以便访问图片地址
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Referer": ""
    }
#得到响应体
    res = requests.get(url=url, headers=headers)
    #print(res)
    if res.status_code != 200:
        print("请求失败")
        return 0
    else:
        preg = r'<img src="(.*?)" alt="(.*?)">'
        img_urls = re.findall(preg, res.text)   #正则筛选后的得到的数据，存入img_urls列表中，得到的是列表
        for img_url in img_urls:                #对列表进行循环，取出img_urls列表中的第一位数据，使用img_urls[0],给到另一个列表img_url
#打印图片地址,用原始的origin_url = "https://pic.netbian.com" 和 img_url[0]
#进行拼接，得到https://pic.netbian.com/uploads/allimg/231111/010350-16996358300785.jpg
            print(f"{origin_url}{img_url[0]}")   #拼接为图片的地址，如https://pic.netbian.com/uploads/allimg/231111/010350-16996358300785.jpg
            #或者下面这种
            #print("{}{}".format(origin_url, img_url[0]))
#让img_url等于拼接的图片地址
            img_url2 = f"{origin_url}{img_url[0]}"  #拼接得到图片地址
            #或者下面这种
            #img_url = "{}{}".format(origin_url, img_url[0])
            #拿响应体，通过图片地址的访问，拿到图片地址的响应数据，第一个requests.get只是拿到整个网页的响应数据，第二个requests.get则是对图片拿到响应数据
            res_img = requests.get(url=img_url2, headers=headers)
            #print(res_img)
            #res_img是一个网络请求的响应对象
            #content是响应对象中的二进制数据，即图片数据。
            #将图片数据赋值给img_data变量。
            img_data = res_img.content
            #print(img_data)
#通过二进制方式 ，将图片写入img目录下， file_path + img_url.split("/")[-1] 其中 file_path为./img/
# with open(file_path + img_url.split("/")[-1], "wb") as f 就是将图片通过二进制的方式，写入img目录下，如./img/003759-17193334791f15.jpg
            with open(file_path + img_url.split("/")[-1], "wb") as f:
                f.write(img_data)

#通过img_url.split("/")[-1]获取图片的文件名；
#使用open()函数以二进制写入模式"wb"打开文件；
#使用write()方法将图片数据写入文件；
#使用with语句确保文件写入完成后自动关闭文件。
#img_url.split("/")[-1]只是为图片命名，也可以改为  with open(file_path + "1.jpg", "wb") as f


if __name__ == '__main__':     #if __name__ == '__main__'表示如果这个脚本被直接运行，那么执行以下缩进的代码块
#换句话说，当一个Python文件作为主程序运行时，__name__这个特殊变量会被设置为'__main__'。就是执行下面的循环，当调用方法时，才执行上面的方法。
#因此，只有当该文件不是被其他文件导入（import）作为模块使用时，这段代码才会被执行。
#这种结构常用于编写可以独立运行或作为模块导入的脚本，确保其中的某些代码（如测试代码、主函数等）仅在直接运行脚本时才执行，
#而不会在被其他脚本导入时意外执行。
    for i in range(11, 13):     #循环对url的index_后面的值进行循环，i从11到12
        if i == 2:
            url = "https://pic.netbian.com/index_2.html"
            print(Download(url))     #打印调用的方法，url是这个 url = "https://pic.netbian.com/index_2.html"
        else:
            url = "https://pic.netbian.com/index_{}.html".format(i)
            print(Download(url))    #打印调用的方法，url是这个 url = "https://pic.netbian.com/index_{}.html".format(i)




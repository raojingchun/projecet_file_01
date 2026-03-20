# import time
# from selenium.webdriver import Chrome
#
# # 创建一个驱动对象
# driver = Chrome()
# # 隐式等待()
# driver.implicitly_wait(10)
# print(driver)
# # 访问百度
# driver.get('https://www.baidu.com')
# # 截取百度页面图片
# print(driver.save_screenshot('baidu.jpg'))
# # 保持浏览器10秒状态(显示等待)
# # time.sleep(10)
# # 退出驱动装置
# driver.quit()
import base64

with open('baidu.jpg', 'rb') as fr:
    data = fr.read()
    # print(base64.b64encode(data).decode())

encode = base64.b64encode(data).decode()  # 将字节的形式b'0x11\x00\xb1'转换成网络间可以传播的字符
byte_data = base64.b64decode(encode)
print(byte_data)
with open('01.jpg', 'wb') as fw:
    fw.write(byte_data)

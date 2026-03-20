import os


# 关闭所有ChromeDriver进程（Windows版）
def close_chromedriver():
    os.system('taskkill /F /IM chromedriver.exe /T')
    print("已尝试关闭所有ChromeDriver进程")


if __name__ == "__main__":
    close_chromedriver()

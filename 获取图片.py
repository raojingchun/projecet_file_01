# url = "http://gips2.baidu.com/it/u=1674525583,3037683813&fm=3028&app=3028&f=JPEG&fmt=auto?w=1024&h=1024"
# import requests
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
#     # "Cookie": "BIDUPSID=A1DFFBC2775F86645A440F54B563B447; PSTM=1751552910; BAIDUID=A1DFFBC2775F8664E585D51FB4FEE6A4:FG=1; H_PS_PSSID=62325_62831_63143_63325_63582_63637_63691_63724_63729_63275_63777_63801_63828_63881_63918_63896_63936; delPer=0; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=8lah00a08g8h0k048h21a021aha40g1k6d4sg24; H_WISE_SIDS=62325_62831_63582_63691_63729_63777_63801_63828_63918_63896_63936; arialoadData=false"
# }
# resp = requests.get(url, headers=headers)
# print(resp.ok)
# print(resp.content)
# with open('图片.jpg', 'wb') as fw:
#     fw.write(resp.content)

a = "abcd"
s = a[-1:-3:-1]
print(s)
import requests
import os

url="https://orig00.deviantart.net/2d1d/f/2018/150/7/e/winter_by_natsumoka-dcd08wo.png"
root="D:\\pictures\\"
path=root+url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		kv={"user-agent":"Google Chrome 67.0.3396.62"}
		r=requests.get(url, headers=kv, timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		with open (path,"wb") as f:
			f.write(r.content)
			f.close()
			print("Completed!")
	else:
		print("Already exists!")
except:
	print("Failed!")
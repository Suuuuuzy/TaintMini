#!/media/dataj/wechat-devtools-linux/testing/myenv/bin/python
import json, os, sys
filename = sys.argv[1]
num = sys.argv[2]
# "/media/dataj/wechat-devtools-linux/testing/auto-testing/miniapp_data/appid_file/random_100_no_error_appids.json"
with open(filename) as f:
    content = json.load(f)
pkgs = content["pkgs"]
unpackpath = content["unpackpath"]
pkgs = [os.path.join(unpackpath, pkg) for pkg in pkgs]
with open(f"random_{num}.txt", 'w') as f:
    f.write('\n'.join(pkgs))
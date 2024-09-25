#!/media/dataj/wechat-devtools-linux/testing/myenv/bin/python
import os, csv, json, sys
output_dir = sys.argv[1]
files = os.listdir(output_dir)
files = [i for i in files if not i.endswith("bench.csv")]
res = {}
for file in files:
    file_path = os.path.join(output_dir, file)
    if os.path.isfile(file_path):
        data = set()
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # print(row)
                if "page_name" in row[0]:
                    continue
                data.add(row[0])
        data = list(data)
        data.sort()
        if data!=[]:
            res[file] = data
            print("\n".join(res[file]))
        
print(len(res))
with open(os.path.join(output_dir, "summary/sum.json"), "w") as f:
    json.dump(res, f, indent = 2)

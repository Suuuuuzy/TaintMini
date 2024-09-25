import sys, os
# python main.py -i random_all.txt -o ./random_all_results -j $(nproc) -c config.json
num = sys.argv[1]
total_file = f"random_{num}.txt"
with open(total_file) as f:
    content = f.read()
lines = content.split("\n")
appids = [i.split("/")[-1] for i in lines]
prefix = lines[0].replace(appids[0], "")
reports = os.listdir(f"random_{num}_results")
reports_ids = [i.replace("-result.csv", "") for i in reports]
with open("tmp.txt", "w") as f:
    left = list(set(appids)-set(reports_ids))
    for i in left:
        f.write(prefix+i+"\n")
print(len(left))

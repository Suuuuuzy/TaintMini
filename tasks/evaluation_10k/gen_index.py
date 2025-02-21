import json, os
result_path = "/media/dataj/wechat-devtools-linux/prework/TaintMini/tasks/evaluation_10k/evaluation_10k_results"
unpack_path = "/media/dataj/wechat-devtools-linux/testing/auto-testing/data/newcrawl/pkg_unpack"
id_file = "evaluation_10k.txt"
with open(id_file, 'r') as f:
    ids = f.readlines()
ids = [i.strip() for i in ids]
ids = [i.split('/')[-1] for i in ids]
results = [ i.replace('-result.csv', '') for i in os.listdir(result_path) if i.endswith('csv')]
with open('evaluation.txt', 'w') as f:
    for oneid in ids:
        if oneid not in results:
            f.write(f'{unpack_path}/{oneid}\n')
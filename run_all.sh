rm -rf ./random_all_results
mkdir random_all_results
cd ./random_all_results
mkdir summary
cd ..
./gen_index.py /media/dataj/wechat-devtools-linux/testing/auto-testing/miniapp_data/appid_file/42w_large_scale_run_appids.json all
# start analysis
python main.py -i tmp.txt -o ./random_all_results -j 10 -c config.json
# ./get_result_sum.py random_all_results
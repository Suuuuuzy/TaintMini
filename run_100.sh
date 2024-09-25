rm -rf ./random_100_results
mkdir random_100_results
cd ./random_100_results
mkdir summary
cd ..
./gen_index.py /media/dataj/wechat-devtools-linux/testing/auto-testing/miniapp_data/appid_file/random_100_no_error_appids.json 100
# start analysis
python main.py -i random_100.txt -o ./random_100_results -j 10 -c config.json
./get_result_sum.py random_100_results
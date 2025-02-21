PREFIX=newcrawl
# rm -rf ./"${PREFIX}_results"
# mkdir "${PREFIX}_results"
# cd ./"${PREFIX}_results"
# mkdir summary
# cd ..
# find /media/dataj/wechat-devtools-linux/testing/auto-testing/data/newcrawl/pkg_unpack -maxdepth 1 -type d -name "wx*" > "${PREFIX}.txt"
python update_newcrawl_txt.py
# start analysis
nohup python main.py -i "${PREFIX}.txt" -o ./"${PREFIX}_results" -j 10 -c config.json & 
./get_result_sum.py "${PREFIX}_results"
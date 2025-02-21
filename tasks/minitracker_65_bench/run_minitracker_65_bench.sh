rm -rf ./minitracker_benchmark_results
mkdir minitracker_benchmark_results
cd ./minitracker_benchmark_results
mkdir summary
cd ..
./gen_index_4_minitracker.sh
# start analysis
python main.py -i minitracker_benchmark.txt -o ./minitracker_benchmark_results -j 10 -c config-MiniTracker.json
./get_result_sum.py minitracker_benchmark_results
rm -rf ./demo_results
mkdir demo_results
python main.py -i demo -o ./demo_results -j $(nproc) -c config.json
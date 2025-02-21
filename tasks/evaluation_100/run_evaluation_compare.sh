CURRENT_DIR=$(pwd)

PREFIX=evaluation_10k
CURRENT_DIR=$(pwd)

if [ ! -d "./${PREFIX}_results" ]; then
    mkdir "./${PREFIX}_results"
fi
cd "./${PREFIX}_results"

if [ ! -d "summary" ]; then
    mkdir "summary"
fi

cd ../../..

# start analysis
python main.py -i "${CURRENT_DIR}/${PREFIX}.txt" -o "${CURRENT_DIR}/${PREFIX}_results" -j 10 -c config.json
./get_result_sum.py "${CURRENT_DIR}/${PREFIX}_results"
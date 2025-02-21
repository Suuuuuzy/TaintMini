python gen_index.py 

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

INPUT_FILE="${CURRENT_DIR}/evaluation.txt"
OUTPUT_DIR="${CURRENT_DIR}/${PREFIX}_results"

# start analysis
python main.py -i "${INPUT_FILE}" -o "${OUTPUT_DIR}" -j 12 -c config.json

# analyze results
./get_result_sum.py "${OUTPUT_DIR}"
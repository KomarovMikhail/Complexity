# !/bin/bash
OUTPUT=$1
EPSILON=$2
LENGTH=$3

touch ${OUTPUT}
python3 ./main.py -o ${OUTPUT} -e ${EPSILON} -n ${LENGTH}
cat ${OUTPUT}
rm ${OUTPUT}


read N
start=1
answer=0

while (($start <= $N)); do
    read number
    answer=$(($answer+$number))
    start=$(($start+1))
done

printf "%.3f" $(echo "scale=5;$answer/$N" | bc)
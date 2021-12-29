declare -a countries=(`cat`)
declare -a remaining=( ${countries[@]/*[aA]*/} )

echo "${remaining[@]}"

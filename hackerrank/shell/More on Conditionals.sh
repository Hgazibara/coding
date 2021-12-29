read x
read y
read z

if [[ ($x != $y) && ($x != $z) && ($y != $z) ]]
then
    echo "SCALENE"
elif [[ ($x == $y) && ($x == $z) && ($y == $z) ]]
then
    echo "EQUILATERAL"
else
    echo "ISOSCELES"
fi
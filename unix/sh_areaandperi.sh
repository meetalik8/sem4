echo "Enter the length of rectangle : "
read L
echo "Enter the breadth of rectangle :"
read B
ARA=`expr $L \* $B`
PER=`expr $(($L + $B)) \* 2`
echo "Area is "
echo $ARA
echo "Perimeter is "
echo $PER

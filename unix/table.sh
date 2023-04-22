echo "Enter your roll number: "
read ROLL
echo "Power table of $ROLL"
for((i=1;i<=5;i++))
do
        power=`expr $ROLL \* $i`
        echo "$ROLL * $i = $power"
done

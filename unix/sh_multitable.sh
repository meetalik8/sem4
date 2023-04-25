echo "Enter a number:"
read A
for((i=1;i<=10;i++)){
        PROD=`expr $(($A*$i))`
        echo "$A x $i = $PROD"
}

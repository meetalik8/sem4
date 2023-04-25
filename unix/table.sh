echo "Enter a number: "
read NO
for ((i=1;i<=5;i++)){
        res=`expr $(($NO ** $i))`
        echo "$NO raised to $i= $res"
}

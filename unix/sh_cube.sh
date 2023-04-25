echo "Enter a number: "
read A
CUB=`expr $A \* $A \* $A`
echo "The cube is : "
echo $CUB

OR
echo "Enter the stupid number"
read NUMBER
CUBES=`expr $(($NUMBER *  $NUMBER * $NUMBER))`
echo "Cube is :$CUBES"

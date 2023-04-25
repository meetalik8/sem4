echo "Enter principle amt: "
read P
echo "Enter the rate of interest: "
read R
echo "Enter the no. of years: "
read N
S=`echo "scale=2; ( $P * $R * $N)/100"|bc`
echo "The simple interest is: "
echo $S

OR
echo "Enter principle amt"
read PA
echo "Enter the rate"
read RA
echo "Enter the no of years"
read NA
SI=`expr $(($PA *$RA * $NA))`
echo "The simple interest is $SI"

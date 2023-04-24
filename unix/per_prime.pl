print "Enter a number: ";
$num = <>;
$count =0;
for ($i=2; $i<$num;$i++)
{
        if($num%$i==0)
        {
                $count +=1;
                break;
        }
}
if($count >1){
        print "Not a Prime Number\n";
}
else {
        print "Prime Number\n";
}

print "Enter a base :";
$b= <>;
print  "Enter a power :";
$p = <>;
$res = $b ** $p;
print "The result is : $res\n";

print "Enter your first name: ";
$fname = <>;
print "Enter your last name: ";
$lname =<>;
$nplate = $fname. $lname;
print "The name plate is $nplate\n";

print "Enter the cost price: ";
$cost =<>;
print "Enter the selling price: ";
$sell =<>;
if ($cost <= $sell){
        $pr = $sell - $cost;
        print "The profit is $pr \n";
}
else {
        $loss =$cost -$sell;
        print "The loss is $loss \n";
}

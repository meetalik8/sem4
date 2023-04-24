@weekdays =('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday');
print "Enter a number: ";
$num =<>;
if($num>=1 && $num<=7) {
        print("$weekdays[$num-1]\n");
}
else {
        print "Invalid number\n";
}

@weekdays = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday');
print "Enter a number to print the weekday: ";
$num = <>;
if ($num >=1 && $num <=7){
        $day = $weekdays[$num-1];
        print "The weekday is $day\n";
}
else {
        print "Invalid number\n";
}

print "Enter your roll number :";
$roll =<>;
print "Enter your name: ";
$name =<>;
print "Name: $name\nRoll: $roll\n";

%students = (7,'Ella',13, 'Taylor', 22,'Jude');
print "Enter a num: ";
$n = <>;
if( exists $students {int($n)}) {
        print "Student Name: $students{int($n)}\n";
}
else {
        print "Student data unavailable\n";
}

print "Enter a number for table: ";
$tn = <>;
for ($i =1; $i<=10;$i++){
        $ans = int($tn*$i);
        print "$tn * $i = $ans\n";
}

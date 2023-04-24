#print weekday by index
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

#Print i/p data
print "Enter your roll number :";
$roll =<>;
print "Enter your name: ";
$name =<>;
print "Name: $name\nRoll: $roll\n";

#Check student data
%students = (7,'Ella',13, 'Taylor', 22,'Jude');
print "Enter a num: ";
$n = <>;
if( exists $students {int($n)}) {
        print "Student Name: $students{int($n)}\n";
}
else {
        print "Student data unavailable\n";
}

#Multiplication table
print "Enter a number for table: ";
$tn = <>;
for ($i =1; $i<=10;$i++){
        $ans = int($tn*$i);
        print "$tn * $i = $ans\n";
}

#PRIME
print "Enter a number to check for prime :";
$p = <>;
$c=0;
for ($i=2;$i<=$p;$i++){
        if($p%$i==0){
                $count++;
}
}
if($count>=2){
        print"Not prime\n";
}
else {
        print"Prime\n";
}

#area of rectangle
print "Enter length of rectangle :";
$len = <>;
print "Enter breadth of rectangle :";
$bre = <>;
$area =$len * $bre;
$peri = 2*($len + $bre);
print "Area of rectangle = $area\n";
print "Perimeter of rectangle = $peri\n";

#!/bin/bash
echo "insert number cycles"
read cycles

echo "insert output name"
read output_name

mg5 <<-EOF
define q = u c d s u~ c~ d~ s~
generate p p > q q
output $output_name
launch
1
0
set nevents 10
set ptj 1000
set ptjmax 1100
0
EOF

for ((i = 1; i < cycles; i++))
do
mg5 <<-EOF
launch output_name
0
set nevents 10
set ptj 1000
set ptjmax 1100
0
EOF

done


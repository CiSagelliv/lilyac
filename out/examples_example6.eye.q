#,OPERATOR,OP1,OP2,RESULT
0,=,A,,1
1,=,B,,1
2,=,C,,1
3,<,C,10000000000,.R1
4,JF,.R1,,11
5,write,,,C
6,+,A,B,.R2
7,=,C,,.R2
8,=,A,,B
9,=,B,,C
10,JI,,,3

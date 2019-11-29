#,OPERATOR,OP1,OP2,RESULT
0,=,i,,1
1,>,i,10,.R1
2,JT,.R1,,7
3,read,,,i
4,+,i,1,.R2
5,=,i,,.R2
6,JI,,,1

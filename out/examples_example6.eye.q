#,OPERATOR,OP1,OP2,RESULT
0,=,A,,9
1,=,B,,6
2,>,A,B,.R1
3,JT,.R1,,7
4,+,B,2,.R2
5,=,B,,.R2
6,JI,,,2

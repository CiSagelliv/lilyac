#,OPERATOR,OP1,OP2,RESULT
0,write,,,"Hola Mundo!!"
1,enter,,,
2,read,,,A
3,read,,,B
4,>,A,B,.R1
5,JF,.R1,,14
6,<,A,25,.R2
7,JF,.R2,,16
8,*,3,40,.R4
9,=,res,,133
10,JI,,,16
11,*,A,B,.R7
12,=,res,,.R7
13,write,,,"Resultado = "

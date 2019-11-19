#,OPERATOR,OP1,OP2,RESULT
0,write,,,"Hola Mundo!!"
1,enter,,,
2,read,,,A
3,read,,,B
4,>,A,B,R1
5,JF,R1,,11
6,<,A,25,R2
7,JF,R2,,13
8,+,A,B,R3
9,=,res,,R3
10,JI,,,13
11,*,A,B,R4
12,=,res,,R4
13,write,,,"Resultado = "

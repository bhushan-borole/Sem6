%option noyywrap

%{
#include <stdio.h>
int op = 0;
float a,b;
%}

dig [0-9]+|([0-9]*)"."([0-9]+)
add "+"
sub "-"
mul "*"
div "/"
ln \n

%%

{dig} {digi();}
{add} {op = 1;}
{sub} {op = 2;}
{mul} {op = 3;}
{div} {op = 4;}
{ln} {printf("\n Result = %2f", a);}

%%
int digi(){
    if (op == 0){
        a = atof(yytext);
    }
    else{
        b = atof(yytext);
        switch(op){
            case 1: a = a + b; break;
            case 2: a = a - b; break;
            case 3: a = a * b; break;
            case 4: a = a / b; break;
        }
        op = 0;
    }
}

int main(){
    printf("Enter Expression: ");
    yylex();
    return 0;
}

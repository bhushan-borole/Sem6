%option noyywrap
%{
	#include<stdio.h>
	int lower = 0;
	int upper = 0;
%}

%%
[A-Z] {printf("Upper case\t\n"); upper++;}
[a-z] {printf("Lower case\t\n"); lower++;}
\n {printf("Upper case = %d and lower case = %d", upper, lower);}
%%

int main(){
	printf("Enter the string of your choice: \n");
	yylex();
	return 0;
}
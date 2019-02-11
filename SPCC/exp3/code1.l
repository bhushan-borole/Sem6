%option noyywrap
%{
	#include<stdio.h>
%}

%%
\n { printf("Welcome"); }
%%

int main(){
	printf("Enter key is to be pressed!");
	yylex();
	return 0;
}
#include<stdio.h>
#include<conio.h>
void main()
{
float n,g,a,d;
printf("Enter gross salary \n");
scanf("%f",&g);
a=0.1*g;
d=0.03*g;
n=g+a-d;
printf("%f is your net salary\n",n);
}

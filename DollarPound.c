#include<stdio.h>
#include<conio.h>
void main()
{
float a,b,c;
printf("Enter dollar \n");
scanf("%f",&a);
b=a*48; //b is rupee
c=b/70; //c is pound
printf("%f dollar = %f pound\n",a,c);
}

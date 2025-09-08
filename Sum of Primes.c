#include<stdio.h>
void main()
{
int i,sum=0;
for(i=1;i<=500;i++)
{
if(i%2!=0)
sum=sum+i;
}
printf("Sum of prime number between 1 to 500 is %d",sum);
}

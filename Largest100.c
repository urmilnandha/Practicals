#include<stdio.h>
#include<conio.h>
void main()
{
int i,largest;
int num[100];
printf("Enter 100 numbers\n");
//scanf("%d",&n);
for(i=0;i<100;i++)
{
scanf("%d",&num[i]);}
largest=num[0];
for(i=0;i<100;i++)
{
    if(num[i]>largest)

    largest=num[i];}

printf("Largest number is %d\n",largest);
}

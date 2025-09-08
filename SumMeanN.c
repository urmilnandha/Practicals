#include<stdio.h>
void main()
{
int i,n,sum=0,avg,num;
printf("Enter the number of values\n");
scanf("%d",&n);
printf("Enter these %d values\n",n);
for(i=0;i<n;i++)
{
scanf("%d",&num);
sum=sum+num;
}
avg=sum/n;
printf("Sum of %d value is %d\n",n,sum);
printf("Mean of %d value is %d\n",n,avg);
}

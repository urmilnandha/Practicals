#include<stdio.h>
void main()
{
int i,n,sum=0;
printf("Enter the limit\n");
scanf("%d",&n);

for(i=0;i<=n;i++)
{
if(i%13==0)
sum=sum+i;
}
printf("Sum is %d\n",sum);

}

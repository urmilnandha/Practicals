#include<stdio.h>
void main()
{
int i,n;
char name[100];
printf("Enter your name\n");

scanf("%s",&name);
printf("How many times u need to print your name?\n");
scanf("%d",&n);


for(i=1;i<=n;i++)


printf("%s\n",name);

}

#include<stdio.h>
#include<conio.h>
void main()
{
float a,b,c,d;
printf("Enter bytes \n");
scanf("%f",&a);
b=a/1024; //b is KB
printf("%f byte = %f KB\n",a,b);
c=b/1024;
printf("%f byte = %f MB\n",a,c);
d=c/1024;
printf("%f byte = %f GB\n",a,d);
}

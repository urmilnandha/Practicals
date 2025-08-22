#include<stdio.h>
void main()
{
float a,b,c;
scanf("%f %f %f",&a,&b,&c);
if((a>b)&&(a>c))
    printf("%f is the largest number",a);
if((b>a)&&(b>c))
  printf("%f is the largest number",b);
if((c>b)&&(c>a))
printf("%f is the largest number",c);
if((a==b)&&(b==c))
    printf("All numbers are equal");
}

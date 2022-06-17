#include<stdio.h>
#include<conio.h>

void main()
{
    char ch;
    printf("\n Enter any charater:--");
    scanf("%c",&ch);
    if ((ch>='a' && ch<='z') || (ch>='A' && ch<='Z'))
    {
        printf("\n This is a charater is a alphabet:--%c");
    }
    else
    {
        printf("\n This is a charater is NOT an alphabet:--%c");
    }
    getch();
}
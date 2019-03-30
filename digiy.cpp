#include <iostream>
#include<string.h>
using namespace std;

int main()
{
    char a[100];
    int k,i,j;
    cin>>a>>k;
    j=strlen(a);
    for(i=k;i<j;i++)
    {
    cout<<a[i];
    }
    return 0;
}

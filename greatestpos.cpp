#include <iostream>
using namespace std;

int main()
{
    int a[100];
    int k,i,j,c,n;
    cin>>k>>n;
    for(i=0;i<k;i++)
    {
    cin>>a[i];
    }
    for(i=0;i<k;i++)
    {
        for(j=i+1;j<k;j++)
        {
            if(a[i]<a[j])
            {
                c=a[i];
                a[i]=a[j];
                a[j]=c;
            }
        }
    }
        cout<<a[n-1];
    return 0;
}

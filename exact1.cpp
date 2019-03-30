#include <iostream>
using namespace std;
int main()
{
    int a[100];
    int k,i,j,c=0;
    cin>>k;
    for(i=0;i<k;i++)
    {
    cin>>a[i];
    }
    for(i=0;i<k;i++)
    {
        for(j=0;j<k;j++)
        {
            if(a[i]==a[j])
            {
                c++;
            }
        }
        if(c!=2)
        cout<<a[i];
        c=0;
    }
    return 0;
}

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"no.s in series";
    cin>>n;
    int a=0;
    int b=1;
    int sum;
    cout<<a<<","<<b<<",";
    for(int i=1;i<=n;i++)
    {
       sum=a+b;
       cout<<sum<<",";
       a=b;
       b=sum;
    }
    return 0;
}

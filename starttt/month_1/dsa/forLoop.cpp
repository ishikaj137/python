#include<iostream>
using namespace std;
int main()
{  //FIBONACCI SERIES

    /*int n;
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
    }*/

//PRIME NUM
int n;
cout<<"numbers";
cin>>n;
for(int i=0;i<=n;i++)
{
    int num=0;
    if(num%i!=0)
    {
        cout<<num;
    }
    num++;
}
    return 0;
}

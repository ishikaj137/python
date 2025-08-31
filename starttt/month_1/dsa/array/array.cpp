#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
int arr[5]={1,2,3,4,5};
/*for(int i=0;i<5;i++)
{
cin>>arr[i];
}
for(int i=0;i<5;i++)
{
cout<<arr[i]<<endl;
}
return 0;
}*/
for(int i=0;i<5;i++)
{
    for(int j=1;j<5;j++)
    {
        if(arr[i]+arr[j]==5)
        {
            cout<<"("<<arr[i]<<","<<arr[j]<<")"<<endl;
        }
    }
}
    return 0;
}
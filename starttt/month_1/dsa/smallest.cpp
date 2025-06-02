#include<iostream>
#include<climits>
using namespace std;
int main()
{
  int i,n;
  cout<<"no. of elements";
  cin>>n;
    int arr[n];
    cout<<"enter";
for(int i=0;i<n;i++)
{
    cin>>arr[i];
}
int smallest= INT_MAX;
for(int i=0;i<n;i++)
{
if(smallest>arr[i])
{
    smallest=arr[i];
}
}
cout<<"smallest no is "<< smallest;
return 0;
}
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
int largest= INT_MIN;
for(int i=0;i<n;i++)
{
if(largest<arr[i])
{
    largest=arr[i];
}
}
cout<<"largest no is "<< largest;
return 0;
}
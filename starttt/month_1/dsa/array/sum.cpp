#include<iostream>
using namespace std;
int main()
{
    int arr[50], size;
    cout<<"size?";
    cin>>size;
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }
    for(int i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
    int i=0,sum=0;
    do{
        sum=sum+arr[i];
        i++;
    }    
    while(i<size);

cout<<"sum="<<sum;
}
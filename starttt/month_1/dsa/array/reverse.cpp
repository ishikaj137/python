#include<iostream>
using namespace std;
void reverse(int arr[],int size, int start,int end)
{
   do{
    swap(arr[start], arr[end]);
    start++;
    end--;
    }
    while(start<end);
    for(int i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
}

int main()
{
    int size, arr[10];
    cout<<"size";
    cin>>size;
    cout<<"enter array";
    for(int i=0;i<size;i++)
    {
        cin>>arr[i];
    }
    int start=0;
    int end=size-1;
    reverse(arr, size, start, end);
}
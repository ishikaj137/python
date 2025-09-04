#include<iostream>
using namespace std;
int linear(int arr[], int size,int key)
{
    for(int i=0; i<size; i++)
    {
        if(arr[i]==key)
        {
            cout<<"Found at "<<i<<" position";
        }
       else
       return 0;
    }
}
int main()
{
    int arr[10], size, key;
    cout<<"size of array";
    cin>>size;
    for(int i=0; i<size; i++){
    cin>>arr[i];
    }
    cout<<"key element";
    cin>>key;
    linear(arr,size,key);
}

#include<iostream>
#include <climits>
using namespace std;
int arr[100];
void PrintArray(int arr[], int size)
{
for(int i=0;i<size;i++)
{
    cin>>arr[i];
}
}
/*int main()
{
    int A1[5]={0,9,8,7,6};
    PrintArray(A1,5);
    int A2[3]={0,4,6};
    PrintArray(A2,3); 
}*/

int getMin(int arr[],int size){
    int min= INT_MAX;
    for(int i=0;i<size;i++){
    if(arr[i]<min){
        min=arr[i];
    }  
}
  return min; 
}

int getMax(int arr[],int size){
    int max= INT_MIN;
    for(int i=0;i<size;i++){
    if(arr[i]>max){
        max=arr[i];
    }  
}
  return max; 
}

int main(){
int size;
cout<<"size of array?";
cin>>size;
PrintArray(arr,size);
cout<<"minimum value="<<getMin(arr,size)<<endl;
cout<<"maximum value="<<getMax(arr,size)<<endl;
}
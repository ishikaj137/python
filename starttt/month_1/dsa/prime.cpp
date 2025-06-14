#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"value of n";
    cin>>n;
    int i;
    for(i=2;i<n;i++)
    { 
        if(n%i==0)
        {
            cout<<"is not prime";
            break;
        }
        else if(n%i!=0){
            cout<<"is prime";
            break;
        }
        else if(n==1){
            cout<<"is prime";
    }
}

return 0;
}
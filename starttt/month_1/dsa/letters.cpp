#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int row=1; row<=n; row++){
        for(int col=1; col<=n; col++){
            char c='A'+ col-1;
            cout<<c<<" ";
        }
        cout<<endl;
    }
}
#include<iostream>
using namespace std;
int main()
{
    float a,b,c;
    cout<<"enter A";
    cin>>a;
    cout<<"enter B";
    cin>>b;
    char op;
    cout<<"enter an operation";
    cin>>op;
switch(op){
case '+':

    c=a+b;
    cout<<"addition= "<<c;
    break;

case '-':

    c=a-b;
    cout<<"subtraction= "<<c;
    break;

case '*':

    c=a*b;
    cout<<"multiplication= "<<c;
    break;

case '/':

    c=a/b;
    cout<<"divison= "<<c;
    break;

default:
cout<<"enter a valid choice";
}
}
#include<iostream>
using namespace std;

int main()
{
    int a=4;
    int b=6;
    cout<<"a&b="<< (a&b)<<endl; // & is for AND operator
    cout<<"a|b="<< (a|b)<<endl; // | for or operator
    cout<<"~a="<< (~a)<<endl; // ~ for not
    cout<<"a^b="<< (a^b)<<endl; // ^ forr xor

    cout<<(17>>1) <<endl; //left shift 1 baar
    cout<<(17>>2) <<endl; //Left shift 2 baar
    cout<<(19<<1) <<endl; //Rigt shift 1 baar
    cout<<(21<<2) <<endl; //Right shift 2 baar

return 0;
}

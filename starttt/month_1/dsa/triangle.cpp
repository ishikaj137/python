#include<iostream>
using namespace std;
int main()
{
  int n;
  int num=1;
  cout<<"n?";
  cin>>n;
  for(int i=1;i<=n;i++){    
   for(int j=1;j<=i;j++){
    cout<<num<<"";
    num++;
   }
   cout<<endl;
  }
  return 0;
}
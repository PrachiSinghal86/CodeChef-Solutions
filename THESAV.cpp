#include <iostream>
#include<string.h>
using namespace std;

int main() {
	long int n;
	cin>>n;
	while(n--)
	{
	    char x[100000];
	    long long int i=1,l;
	    int f=0;
	    cin>>x;
	    l=strlen(x);
	    if(x[0]!='*')
	    {
	        cout<<"NO"<<"\n";
	        continue;
	    }
	    for(i=1;i<l-2;i++)
	    {
	        if(x[i]=='0' && x[i+1]=='0'&& x[i+2]=='0')
	        {
	            f=1;
	            cout<<"NO"<<"\n";
	            break;
	        }
	    }
	    if(f==0)
	    {
	        cout<<"YES\n";
	    }
	    
	}
	return 0;
}

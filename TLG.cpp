#include <iostream>
using namespace std;

int main() {
	long int n,i;
	long long int s1=0,s,t1=0,t,w,l=0;
	cin>>n;
	for(i=0;i<n;i++)
	{
	    cin>>s>>t;
	    s1=s1+s;
	    t1=t1+t;
	    if (s1-t1>l)
	    {
	        l=s1-t1;
	        w=1;
	        
	    }
	    else if(t1-s1>l)
	    {
	        l=t1-s1;
	        w=2;
	    }
	}
	cout<<w<<" "<<l;
	
	return 0;
}

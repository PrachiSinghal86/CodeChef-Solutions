#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,k;
	    cin>>n>>k;
	    int a[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>a[i];
	    }
	    int m=-1,i,f=-1;
	    for(i=0;i<n;i++)
	    {
	        if(a[i]<=k)
	        {
	            int l=(k-a[i]);
	            if(l%a[i]==0)
	            {
	                if(m==-1)
	                {
	                    m=l/a[i];
	                    f=a[i];
	                }
	                else
	                {
	                    if(m>(l/a[i]))
	                    {
	                        m=l/a[i];
	                        f=a[i];
	                    }
	                }
	            }
	        }
	    }
	    cout<<f<<endl;
	}
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int>v(7,0);
        int arr[n],i,h=0;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        for(i=0;i<=n/2;i++)
        {
            if(arr[i]!=arr[n-1-i]||arr[i]<1||arr[i]>8)
            {
                h=1;
                break;
            }
            v[arr[i]-1]++;
        }
        if(h==1)
        {
            cout<<"no"<<endl;
            
        }
        else
        {
            for(i=0;i<7;i++)
            {
                if(v[i]==0)
                {
                    h=1;
                    break;
                }
            }
            if(h==1)
            cout<<"no"<<endl;
            else
            cout<<"yes"<<endl;
        }
        
    }
    
    return 0;
}
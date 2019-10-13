#include <iostream>
using namespace std;
 
int main() {
	int t;
	cin>>t;
	while(t--){
		int M,i;
		string S;
		char a;
		cin>>M;
		cin>>S;
		for(i=0;i<M-1;i=i+2){
			a=S[i];
			S[i]=S[i+1];
			S[i+1]=a;
 
		}
		for(i=0;i<M;i=i+1){
			S[i]= char(219-int(S[i]));
		}
		cout<<S<<"\n";
	}
	return 0;
}

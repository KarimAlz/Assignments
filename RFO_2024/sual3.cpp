#include<bits/stdc++.h>

using namespace std;

int main() {

    cin.tie(0);
    cout.tie(0);

    int t;
    cin>>t;
    while(t--) {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int one = 0, zero = 0;
        for(int i = 0; i < n; i++) {
            if(s[i] == '1') {
                one++;
            }
            else {
                zero++;
            }
        }
        if(one == 0) {
            cout<<0<<endl;
        }
        else if(one == zero) {
            cout<<one<<endl;
        }
        else if(zero > one) {
            cout<<one<<endl;
        }
        else {
            cout<<zero + 1<<endl;
        }
    }

    return 0;
}
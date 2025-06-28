
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>
/* problem description:
Given an array of n numbers, our task is to calculate the maximum subarry sum, i.e,
the lagest possible sum of a sequence of consecutive values in the array.
example: [ -1, 2, 4, -3, 5, 2 , -5, 2 ]
answer: [2, 4, -3, 5, 2]
We assume that an empty subarray is allowed, so the maxmum subarray sum is always at 
least 0
*/

using namespace std;
//shorten the code
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int alg1(vector<int> & arr) {
    //O(n^3)
    int best = 0;
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            int sum = 0;
            for (int k = i; k <= j; ++k) {
                sum += arr[k];
            }
            best = max(best, sum);
        }
    }
    return best;
}

int alg2(vi &arr) {
    //O(n^2)
    int best = 0;
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        int sum = 0;
        for (int j = i; j < n; ++j) {
            //calculate the sum at the same time when the right end of the subarray moves
            sum += arr[j];
            best = max(best, sum);
        }
    }
    return best;
}

int alg3(vi &arr) {
    //O(n)
    int best = 0, sum = 0;
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        //for each array pos, get the max sum of sub-arry that ends at that pos
        sum = max(arr[i], sum + arr[i]);
        best = max(best, sum);
    }
    return best;
}

int main() {
    //solution
    vi arr { -1, 2, 4, -3, 5, 2, -5, 2};
    //cout << "best solution is: " << alg1(arr) << endl;
    cout << "best solution is: " << alg3(arr) << endl;
    cout << "best solution is: " << alg2(arr) << endl;
    cout << "best solution is: " << alg1(arr) << endl;
    /*
    int a,b;
    string x,s;
    int x1 = 1, y1 = 2, x2 = 3, y2 = 4;
    vector<pair<int, int> > myVec = {{-1, -1}, {2, 5}, {3, 10}};
    vector<pi> v(10);
    // input example:
    // user input from stdio:
    // cin >> a >> b >> x;
    // to read the whole line from stdin containing spaces:
    // getline(cin, s)
    // read from a file io:
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    cout << a << " " << b << " " << x << "\n";
    cout << x1 << " " << y1 << " " << x2 << "\n";
    
    v.push_back(make_pair(y1,x1));
    v.push_back(make_pair(y2,x2));
    int d = v[0].first + v[0].second;
    cout<< v[0].first << v[0].second << v[1].first << v[1].second << endl;
    */


}
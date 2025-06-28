
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;
//shorten the code
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

int main()
{
    //solution
    int a, b;
    string x, s;
    int x1 = 1, y1 = 2, x2 = 3, y2 = 4;
    vector<pair<int, int>> myVec = {{-1, -1}, {2, 5}, {3, 10}};
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

    v.push_back(make_pair(y1, x1));
    v.push_back(make_pair(y2, x2));
    int d = v[0].first + v[0].second;
    cout << v[0].first << v[0].second << v[1].first << v[1].second << endl;
}
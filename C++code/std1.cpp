#include <bits/stdc++.h>
using namespace std;

// Pair 
int main(){
pair <int , int> p1= {1,2};
cout << p1.first << " " << p1.second << endl;

pair <int , pair <int , int>> p2 = {1,{2,3}};
cout << p2.first << " " << p2.second.first << " " << p2.second.second << endl;
}


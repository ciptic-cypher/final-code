#include <bits/stdc++.h>
using namespace std;


int main(){
    int a;
    // input and outputs
    cin >> a;
    cout<< "The value of a entered is :"<< a << endl;

    // 7 datatypes in C++
    // int | long | long long | float | double | string | char 

    //declarations
    long b;
    long long c;
    float d;
    double e;
    string f;
    char g;

    // if else statements 

    if (a<5){
        cout << "entered value is less than 5!"<< endl; 
    }
    else if (a==5){
        cout << "entered value is equal to 5!" << endl;
    }
    else {
        cout << "entered value is greater than 5!" << endl;
    }

    // The Switch Statement
    switch(a){
        case 1:
        cout << "entered value is 1!" << endl;
        break;
        case 2:     
        cout << "entered value is 2!" << endl;
        break;
        case 3:
        cout << "entered value is 3!" << endl;
        break;
        default:
        cout << "entered value is not 1,2 or 3!" << endl;
    }
    
    return 0;
}
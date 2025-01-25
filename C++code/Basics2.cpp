// loosps inside concepts

#include <bits/stdc++.h>
using namespace std;

// defining the functions 

int add(int a , int b ){ // pass by value or pass by address
    return a+b;
}

int main()

{
    int i;
    // for loop
    for (i =0; i<5; i++){
        cout<< i << endl;

    }

    cout << "-----------------" << endl;

    // while loop

    while (i>0){
        cout << i << endl;
        i--;

    }
    cout << "-----------------" << endl;
    do{
        cout << i << endl;
        i++;
    }while(i<0);

    cout<< add(2,3) <<endl; // calling the function 
}
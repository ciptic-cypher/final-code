// here we are going to malke a menu based login 

#include<bits/stdc++.h>
using namespace std;


class temp {
    string username , password , Email ;
    string searchName , searchPass;
    fstream file ;
    public :
    void login();
    void signup();
    void forget();

}obj;
int main(){
    int a ;
    while(1){
        cout<<"1. Login"<< endl <<"2. Register"<<endl << "3. Forget password"<<endl<<"4. Exit"<<endl;
        cout<<"Enter your choice ::";
        cin >> a;

        switch(a){
            case 1 : obj.login(); break;
            case 2 : obj.signup(); break;
            case 3 : obj.forget(); break;
            case 4 : exit(0); break;
            default : cout<<"Invalid choice"<<endl; break;
        }
    }
}

void temp :: signup(){
    cin.ignore();
    cout<< "Enter your username ::";
    getline(cin ,username);

    cout << "Enter your email ::" ;
    getline(cin , Email);

    cout << "Enter your password ::";
    getline(cin , password);

    file.open("login.txt", ios::out | ios :: app);
    file << username << "*" << Email << "*" << password << endl;

    file.close();

}

void temp :: login(){
    
    cin.ignore();
    cout << "Enter your username ::" << endl;
    getline(cin , searchName);


    cout << "Enter your password ::" << endl;
    getline(cin, searchPass);

    file.open("Login.txt", ios :: in );

    // get the first stored credentials 
    getline(file , username , '*');
    getline(file , Email , '*');
    getline(file , password , '\n');

    while (!(file.eof())){
        if (username == searchName){ 
            if (password== searchPass){
                cout<< "Login Sucessfull for "<< username << endl;
                break;
                }
            else {
                cout<< "Incorrect Password" << endl;
                break;
            }}
        else {
            cout<< "Incorrect Username" << endl;
            break;
        
        }
        getline(file , username , '*');
        getline(file , Email , '*');
        getline(file , password , '\n');

    }

}

void temp:: forget(){
    cin.ignore();
    cout << "Enter your username ::";
    getline(cin , searchName);

    cout << "Enter your email ::";
    getline(cin , searchPass);

    file.open("login.txt",ios::in);

    getline(file,username,'*');
    getline(file,Email,'*');
    getline(file,password,'\n');

    while (!(file.eof())){
        if (username== searchName){
            if (Email== searchPass){
                cout << "your password is :: " << password << endl;
                break;
            }
            else {
                cout << "Incorrect Email" << endl;
                break;
            }
        }
        else {
            cout << "incorrect username" << endl;
            break;
        }
    getline(file,username,'*');
    getline(file,Email,'*');
    getline(file,password,'\n');
    }
}
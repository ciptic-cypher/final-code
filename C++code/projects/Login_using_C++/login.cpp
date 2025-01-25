#include <bits/stdc++.h>
using namespace std;

class temp{
    string username,password,email ;
    string searchpass , pass;
    fstream file ;

    public :
    void login();
    void signup();
    void forget();

}obj;

int main(){

    while(1){
        int a ;
         cout << "1. Login"<<endl;
         cout << "2. Signup"<<endl;
         cout << "3. Forget"<<endl;
         cout << "4. Exit"<<endl;
         cout << "Enter your choice :: ";
         cin >> a ;

         switch(a){
            case 1: obj.login(); break;
            case 2: obj.signup();break;
            case 3: obj.forget();break;
            case 4: exit(0); break;
            default: cout << "Invalid choice" << endl; 
         }
    }return 0;
}
void temp :: signup(){
    cin.ignore();
    cout << "ENter your username ::";
    getline(cin, username);

    cout << "Enter your password ::";
    getline(cin ,password);

    cout<< "Enter your Email ::";
    getline(cin , email);

    file.open("login.txt",ios::out | ios::app);
    file << username << "*" << password << "*" << email << endl;

    file.close();

}

void temp :: login(){
    cin.ignore();

    cout << "Enter your username ";
    getline(cin , searchpass);

    cout << "Enter your password";
    getline(cin , pass);

    file.open("login.txt",ios :: in);
    
    
    getline(file, username,'*');
    getline(file, password,'*');
    getline(file, email,'\n');

    while(!file.eof()){
        if (username==searchpass){
            if (password==pass){
                cout<< "Login Successfull for "<< username << endl;
                break;
            }
            else{
                cout << "Incorrect Password !"<< endl;
                break;
            }
        }
        else{
            cout << "Incorrect username !"<< endl;
            break;
        }
       
    }
    file.close();
}

void temp :: forget(){
    cin.ignore();

    cout << "Enter your username ";
    getline(cin , searchpass);

    cout << "Enter your email";
    getline(cin , pass);

    file.open("login.txt",ios :: in);
    
    
    getline(file, username,'*');
    getline(file, password,'*');
    getline(file, email,'\n');

    while(!file.eof()){
        if (username==searchpass){
            if (email==pass){
                cout<< "password for this is "<< password << endl;
                break;
            }
            else{
                cout << "Incorrect email !"<< endl;
                break;
            }
        }
        else{
            cout << "Incorrect username !"<< endl;
            break;
        }
    }
    file.close();
}
#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student {
    public:
        void set_age(int age) {
            this->age_ = age;
        }
        
        int get_age() {
            return this->age_;
        }
        
        void set_first_name(string first_name) {
            this->first_name_ = first_name;
        }
        
        string get_first_name() {
            return this->first_name_;
        }
        
        void set_last_name(string last_name) {
            this->last_name_ = last_name;
        }
        
        string get_last_name() {
            return this->last_name_;
        }
        
        void set_standard(int standard) {
            this->standard_ = standard;
        }
        
        int get_standard() {
            return this->standard_;
        }
        
        string to_string() {
            stringstream ss;
            
            ss << this->age_ << "," << this->first_name_ << "," << this->last_name_ << "," << this->standard_;
            
            return ss.str();
        }
    
    private:
        int age_;
        int standard_;
        string first_name_;
        string last_name_;
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}

#include <iostream>
#include <string>
using namespace std;

int main(){
	int cnt = 0;

	while (cnt < 100){
		string a;
		getline(cin, a, '\n');
		cnt++;
		cout << a<<endl;
	}
}
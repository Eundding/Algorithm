#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	string str;
	int arr[4] = {}; //소문자, 대문자, 숫자, 공백
	
	while (cin.eof() == false) {
		getline(cin, str, '\n');
		for (int i = 0; i < str.length(); i++) {
			if (str[i] >= 97 && str[i] <= 122) { //소문자
				arr[0]++;
			}
			else if (str[i] >= 65 && str[i] <= 90) { //대문자
				arr[1]++;
			}
			else if (str[i] >= 48 && str[i] <= 57) {
				arr[2]++;
			}
			else if (str[i] == ' ') {
				arr[3]++;
			}
		}
		if (cin.eof() == false) {
			cout << arr[0] << " " << arr[1] << " " <<
				arr[2] << " " << arr[3] << '\n';
			arr[0] = 0, arr[1] = 0, arr[2] = 0, arr[3] = 0;
		}
	}
}
#include <iostream>

using namespace std;

void reverse (string& s)
{
	string temp = "";
	int length = s.size();
	for (int i=length-1; i>=0; i--)
	{
		temp += s[i];
	}
	s = temp;
}

int atoi(const char ch)
{
	return (ch - '0');
}
int main()
{
	string k = "11";
	cout << atoi(k[0]);
}
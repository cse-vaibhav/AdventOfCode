#include <iostream>
#include <fstream>
#include <sstream>



using namespace std;

int count_lines()
{
	ifstream input;
	input.open("input.txt");
	int line_count = 0;
	string word;
	while(getline(input, word))
	{
		line_count++;
	}
	return line_count;
}

stringstream getInput()
{
	ifstream input;
	input.open("input.txt");
	stringstream inp;
	string line;
	for (int i=0;i<count_lines();i++)
	{
		getline(input,line);
		inp << line << '\n';
	}
	for (int i=0;i<count_lines();i++)
	{
		getline(inp, line);
		cout << line << endl;
	}
	return inp;
}
int main()
{

	int line_count = count_lines();	

	stringstream stream = getInput();
	// ifstream input;
	// input.open("input.txt");
	// int pos[2] = {0,0};
	// for (int i=0; i<line_count; i++)
	// {
	// 	string cmd;
	// 	int steps;
			
	// 	input >> cmd >> steps;

	// 	if (cmd == "forward")
	// 	{
	// 		pos[0] += steps;
	// 	}
	// 	else if (cmd == "up")
	// 	{
	// 		pos[1] -= steps;
	// 	}
	// 	else if (cmd == "down")
	// 	{
	// 		pos[1] += steps;
	// 	}
	// }
	// int res = 1;
	// for (int elem : pos)
	// {
	// 	res *= elem;
	// }
	// cout << res;
}
#include <iostream>
#include <fstream>

using namespace std;

int part1(int*, int);
int part2(int*, int);

int main()
{
	ifstream input;
	input.open(".\\input.in");

	ofstream output;
	output.open(".\\output.out");

	int size = 2000;
	int arr[size];
	for (int i=0;i<size;i++)
	{
		input >> arr[i];
	}
	output << part1(arr, size) << endl;
	output << part2(arr, size);
}

int part1(int arr[], int size)
{
	int num = arr[0];
	int count = 0;

	for (int i=1; i < size; i++)
	{
		if (arr[i] > num)
		{
			count += 1;
		}
		num = arr[i];
	}
	return count;
}

int part2(int arr[], int size)
{
	int count = 0;
	int curr_sum = arr[0] + arr[1] + arr[2];
	for (int i=1;i<size-2; i++)
	{
		 int s = arr[i] + arr[i+1] + arr[i+2];
		 if (s > curr_sum)
		 	count++;
		 curr_sum = s;
	}
	cout << "h";
	return count;
}
#include <iostream>
#include <cmath>

int main(int argc, char* argv[]) {
	double x = 1.0 * std::stod(argv[1]); 
	int y = std::atoi(argv[2]);
	double result = (x - 2) * (x - 2) - y;
	std::printf("%.16f \n", result);
	return 0;
}

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int d1, d2;
    cin >> d1 >> d2;

    const double pi = 3.141592;
    double circumference = 2 * (d1 + pi * d2);

    cout << fixed << setprecision(6) << circumference << endl;
    return 0;
}

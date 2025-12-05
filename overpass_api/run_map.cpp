#include <iostream>

int main() {
    // windows
    int result = std::system("python map_from_overpass.py 40.712 -74.0060 >nul 2>&1"); // call python script with arguments latitude, longitude

    // linux and mac
    //int result = std::system("python map_from_overpass.py 40.712 -74.0060 >/dev/null 2>&1");

    return 0;
}
#include <iostream>

int main() {
    // windows
    int result = std::system("map_from_overpass.exe 40.712 -74.0060"); // call python script with arguments latitude, longitude

    // linux and mac
    //int result = std::system("map_from_overpass.exe 40.712 -74.0060");

    std::cout << result << std::endl;

    return 0;
}
// lou

double CENTER_LAT = 38.2469;
double CENTER_LON = -85.7664;

// lex
/*
double CENTER_LAT = 38.0389;
double CENTER_LON = -84.5153;
*/

constexpr int ZOOM = 13; // 0–19
constexpr int IMAGE_SIZE = 600;
constexpr int TILE_SIZE = 256;
constexpr double PI = 3.14159265358979323846;
constexpr const char* TILE_DIR = "tiles";

#include <cmath>
#include <string>
#include <vector>
#include <fstream>
#include <filesystem>
#include <iostream>
#include <algorithm>
#include <cstring>

#define CURL_STATICLIB
#include "curl/curl.h"

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

namespace fs = std::filesystem;

struct Image {
    int w, h;
    std::vector<unsigned char> px; // RGBA
};

size_t write_file(void* ptr, size_t size, size_t nmemb, void* stream) {
    std::ofstream* f = (std::ofstream*)stream;
    f->write((char*)ptr, size * nmemb);
    return size * nmemb;
}

int lon_to_tile_x(double lon, int z) {
    return int((lon + 180.0) / 360.0 * (1 << z));
}

int lat_to_tile_y(double lat, int z) {
    double lat_rad = lat * PI / 180.0;
    return int(
        (1.0 - std::log(std::tan(lat_rad) + 1.0 / std::cos(lat_rad)) / PI)
        / 2.0 * (1 << z)
    );
}

bool download_tile(int z, int x, int y, const fs::path& path) {
    fs::create_directories(path.parent_path());

    CURL* curl = curl_easy_init();
    if (!curl) return false;

    std::string url =
        "https://tile.openstreetmap.org/" +
        std::to_string(z) + "/" +
        std::to_string(x) + "/" +
        std::to_string(y) + ".png";

    std::ofstream file(path, std::ios::binary);

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_file);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &file);
    curl_easy_setopt(curl, CURLOPT_USERAGENT, "TileStitcher/1.0");

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    file.close();

    return res == CURLE_OK;
}

Image load_tile(const fs::path& path) {
    int w, h, c;
    unsigned char* data = stbi_load(path.string().c_str(), &w, &h, &c, 4);
    if (!data) throw std::runtime_error("Failed to load tile");

    Image img{w, h};
    img.px.assign(data, data + w * h * 4);
    stbi_image_free(data);
    return img;
}

int make_map() try {
    int center_x = lon_to_tile_x(CENTER_LON, ZOOM);
    int center_y = lat_to_tile_y(CENTER_LAT, ZOOM);

    int tiles_needed = int(std::ceil(double(IMAGE_SIZE) / TILE_SIZE));
    int half = tiles_needed / 2;

    Image out;
    out.w = tiles_needed * TILE_SIZE;
    out.h = tiles_needed * TILE_SIZE;
    out.px.resize(out.w * out.h * 4, 255);

    for (int dy = -half; dy <= half; ++dy) {
        for (int dx = -half; dx <= half; ++dx) {
            int tx = center_x + dx;
            int ty = center_y + dy;

            fs::path tile_path =
                fs::path(TILE_DIR) /
                std::to_string(ZOOM) /
                std::to_string(tx) /
                (std::to_string(ty) + ".png");

            if (!fs::exists(tile_path)) {
                std::cout << "Downloading tile "
                          << ZOOM << "/" << tx << "/" << ty << "\n";
                download_tile(ZOOM, tx, ty, tile_path);
            }

            Image tile = load_tile(tile_path);

            int ox = (dx + half) * TILE_SIZE;
            int oy = (dy + half) * TILE_SIZE;

            for (int y = 0; y < TILE_SIZE; ++y) {
                for (int x = 0; x < TILE_SIZE; ++x) {
                    int dst = ((oy + y) * out.w + (ox + x)) * 4;
                    int src = (y * TILE_SIZE + x) * 4;
                    std::copy_n(&tile.px[src], 4, &out.px[dst]);
                }
            }
        }
    }

    // Crop to requested IMAGE_SIZE
    Image final_img{IMAGE_SIZE, IMAGE_SIZE};
    final_img.px.resize(IMAGE_SIZE * IMAGE_SIZE * 4);

    int start = (out.w - IMAGE_SIZE) / 2;

    for (int y = 0; y < IMAGE_SIZE; ++y) {
        std::memcpy(
            &final_img.px[y * IMAGE_SIZE * 4],
            &out.px[((y + start) * out.w + start) * 4],
            IMAGE_SIZE * 4
        );
    }

    stbi_write_png(
        "map.png",
        final_img.w,
        final_img.h,
        4,
        final_img.px.data(),
        final_img.w * 4
    );

    std::cout << "Saved map.png\n";
    return 0;
}
catch (const std::exception& e) {
    std::cerr << e.what() << "\n";
    return 1;
}

int main() {
    std::cout << "Creating map...\n";
    make_map();

    std::filesystem::remove_all(TILE_DIR);
    return 0;
}
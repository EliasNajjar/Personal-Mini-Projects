#include <iostream>
#include <string>
#include "C:\Users\elias\anaconda3\envs\geospatial\Library\include\curl\curl.h"

constexpr double CENTER_LAT = 38.0389;   // <-- change me
constexpr double CENTER_LON = -84.5153;   // <-- change me
constexpr int    RADIUS_METERS = 600;
constexpr int    IMAGE_SIZE = 600;

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

// ---------- nlohmann/json (single-header) ----------
#include "json.hpp"
using json = nlohmann::json;

// ---------- stb_image_write ----------
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

// ==================================================
// HTTP
// ==================================================

size_t write_cb(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

std::string run_overpass_query(double lat, double lon) {
    CURL* curl = curl_easy_init();
    if (!curl) throw std::runtime_error("curl init failed");

    std::string response;

    std::string query =
        "[out:json][timeout:25];"
        "node(around:" + std::to_string(RADIUS_METERS) + "," +
        std::to_string(lat) + "," + std::to_string(lon) + ");"
        "out geom;";

    std::string post = "data=" + query;

    curl_easy_setopt(curl, CURLOPT_URL, "https://overpass-api.de/api/interpreter");
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, post.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);

    if (res != CURLE_OK)
        throw std::runtime_error("curl request failed");

    return response;
}

// ==================================================
// Image drawing
// ==================================================

struct Image {
    int w, h;
    std::vector<unsigned char> px; // RGBA
};

Image make_image(int w, int h) {
    Image img{w, h};
    img.px.resize(w * h * 4, 255); // white
    return img;
}

void draw_circle(Image& img, int cx, int cy, int r) {
    for (int y = -r; y <= r; y++) {
        for (int x = -r; x <= r; x++) {
            if (x*x + y*y > r*r) continue;
            int px = cx + x;
            int py = cy + y;
            if (px < 0 || py < 0 || px >= img.w || py >= img.h) continue;
            int i = (py * img.w + px) * 4;
            img.px[i+0] = 0;
            img.px[i+1] = 0;
            img.px[i+2] = 0;
            img.px[i+3] = 255;
        }
    }
}

struct Bounds {
    double minLat, maxLat, minLon, maxLon;
};

Bounds compute_bounds(const json& j) {
    Bounds b{1e9, -1e9, 1e9, -1e9};

    for (auto& e : j["elements"]) {
        if (!e.contains("lat")) continue;
        double lat = e["lat"];
        double lon = e["lon"];
        b.minLat = std::min(b.minLat, lat);
        b.maxLat = std::max(b.maxLat, lat);
        b.minLon = std::min(b.minLon, lon);
        b.maxLon = std::max(b.maxLon, lon);
    }
    return b;
}

void latlon_to_pixel(
    double lat, double lon,
    const Bounds& b,
    int w, int h,
    int& x, int& y
) {
    x = int((lon - b.minLon) / (b.maxLon - b.minLon) * w);
    y = int((b.maxLat - lat) / (b.maxLat - b.minLat) * h);
}

// ==================================================
// MAIN
// ==================================================

int main() try {
    std::cout << "Querying Overpass...\n";
    std::string json_text = run_overpass_query(CENTER_LAT, CENTER_LON);

    json j = json::parse(json_text);

    Image img = make_image(IMAGE_SIZE, IMAGE_SIZE);
    Bounds bounds = compute_bounds(j);

    for (auto& e : j["elements"]) {
        if (!e.contains("lat")) continue;

        int x, y;
        latlon_to_pixel(
            e["lat"], e["lon"],
            bounds,
            img.w, img.h,
            x, y
        );

        draw_circle(img, x, y, 3);
    }

    // draw center point
    int cx, cy;
    latlon_to_pixel(
        CENTER_LAT, CENTER_LON,
        bounds,
        img.w, img.h,
        cx, cy
    );
    draw_circle(img, cx, cy, 6);

    stbi_write_png(
        "map.png",
        img.w,
        img.h,
        4,
        img.px.data(),
        img.w * 4
    );

    std::cout << "Saved map.png\n";
    return 0;
}
catch (const std::exception& e) {
    std::cerr << e.what() << "\n";
    return 1;
}

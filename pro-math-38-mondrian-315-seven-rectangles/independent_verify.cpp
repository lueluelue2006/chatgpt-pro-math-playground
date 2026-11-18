#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int side = 315, pieces = 7, total = side * side, mean = total/pieces;
struct Strip { int height, width; };
struct Skyline {
    std::array<Strip, pieces + 1> strips{};
    int count = 0;
    void append(int height, int width) {
        if (!width) return;
        if (count && strips[count-1].height == height) strips[count-1].width += width;
        else strips[count++] = {height, width};
    }
};
struct Tile { int w, h, area, shape; };

struct Search {
    int deficit, area_min, area_max;
    std::vector<Tile> tiles;
    std::array<bool,(side+1)*(side+1)> used{};
    std::array<std::uint64_t,pieces+1> visits{};
    std::uint64_t solutions = 0;
    explicit Search(int d) : deficit(d), area_min(mean-6*d/7), area_max(mean+6*d/7) {
        for (int w=1; w<=side; w++) {
            for (int h=(area_min+w-1)/w; h<=std::min(side,area_max/w); h++) {
                tiles.push_back({w,h,w*h,std::min(w,h)*(side+1)+std::max(w,h)});
            }
        }
    }

    void run(const Skyline& skyline, int depth, int filled, int smallest, int largest) {
        ++visits[depth];
        if (depth == pieces) { solutions += filled == total; return; }
        const int left = pieces-depth;
        const int lo = std::max(area_min, largest-deficit);
        const int hi = std::min(area_max, smallest+deficit);
        if (total-filled < left*lo || total-filled > left*hi) return;
        int first = 0;
        int component_area=0, min_pieces=0, max_pieces=0;
        for (int i=0; i<=skyline.count; i++) {
            if (i<skyline.count && skyline.strips[i].height < side) {
                const auto strip=skyline.strips[i];
                if (strip.height < skyline.strips[first].height) first=i;
                component_area += (side-strip.height)*strip.width;
            } else if (component_area) {
                const int need = (component_area+hi-1)/hi;
                const int fit = component_area/lo;
                if (need>fit) return;
                min_pieces += need;
                max_pieces += fit;
                component_area=0;
            }
        }
        if (left<min_pieces || left>max_pieces) return;
        int needed_bases=0;
        for (int i=0; i<skyline.count; i++) {
            const int h = skyline.strips[i].height;
            if (h==side) continue;
            int width=skyline.strips[i].width;
            bool prior_same_base=false;
            for (int j=i-1; j>=0 && skyline.strips[j].height<=h; j--) {
                width+=skyline.strips[j].width;
                prior_same_base |= skyline.strips[j].height==h;
            }
            if (prior_same_base) continue;
            for (int j=i+1; j<skyline.count && skyline.strips[j].height<=h; j++) {
                width+=skyline.strips[j].width;
            }
            if (width*(side-h)<lo || ++needed_bases>left) return;
        }
        const auto gap = skyline.strips[first];
        for (const auto tile : tiles) {
            if (tile.w > gap.width) break;
            if (tile.h > side-gap.height || tile.area<lo || tile.area>hi || used[tile.shape]) continue;
            Skyline next;
            for (int i=0; i<first; i++) next.append(skyline.strips[i].height,skyline.strips[i].width);
            next.append(gap.height+tile.h,tile.w);
            next.append(gap.height,gap.width-tile.w);
            for (int i=first+1; i<skyline.count; i++) next.append(skyline.strips[i].height,skyline.strips[i].width);
            used[tile.shape]=true;
            run(next,depth+1,filled+tile.area,std::min(smallest,tile.area),std::max(largest,tile.area));
            used[tile.shape]=false;
        }
    }
};

int main() {
    for (int d : {149,150}) {
        Search check(d);
        Skyline empty;
        empty.append(0,side);
        check.run(empty,0,0,total,0);
        std::cout << "D=" << d << " orientations=" << check.tiles.size() << " solutions=" << check.solutions << " nodes=";
        for (auto v : check.visits) std::cout << " " << v;
        std::cout << std::endl;
    }
}


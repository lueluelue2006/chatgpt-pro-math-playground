// Build: g++ -O3 -std=c++17 verify_315.cpp -o verify_315
// Run:   ./verify_315 149       (lower bound; default)
//        ./verify_315 150       (positive control)
// All computations are exact integers; no external libraries are needed.
#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <utility>
using namespace std;

constexpr int N=315, K=7, TOTAL=N*N, MEAN=TOTAL/K;
int D, lowerArea, upperArea, W[K], H[K];
using Profile = array<pair<int,int>, K+2>; // (height, width), left to right
unsigned long long nodes[K+1]{};

unsigned long long search(const Profile& p, int n, int k,
                          int minArea, int maxArea, int remainingArea) {
    ++nodes[k];
    if (k==K) return remainingArea==0;

    // Select the leftmost run at the lowest height.
    int y=N, j=0, levels=0;
    for (int i=0; i<n; ++i) {
        int yi=p[i].first;
        if (yi<y) { y=yi; j=i; }
        bool first=true;
        for (int t=0; t<i; ++t)
            if (p[t].first==yi) first=false;
        if (yi<N && first) ++levels;
    }
    // Each distinct unfinished height needs a different future rectangle.
    if (levels>K-k || y==N) return 0;

    // Every future area lies in [a,b]. With r OTHER future rectangles,
    // the next area also lies in [remainingArea-r*b, remainingArea-r*a].
    int a=max(lowerArea,maxArea-D), b=min(upperArea,minArea+D);
    int r=K-k-1;
    int l=max(a,remainingArea-r*b), u=min(b,remainingArea-r*a);
    if (l>u) return 0;

    unsigned long long count=0;
    for (int w=1; w<=p[j].second; ++w) {
        for (int h=(l+w-1)/w; h<=min(u/w,N-y); ++h) {
            // Transposing the entire square allows this symmetry choice.
            if (k==0 && w>h) continue;
            bool repeated=false;
            for (int i=0; i<k; ++i)
                if ((W[i]==w && H[i]==h) || (W[i]==h && H[i]==w))
                    repeated=true;
            if (repeated) continue;
            W[k]=w; H[k]=h;

            // Raise the first w columns of the selected run by h.
            // Merge adjacent runs having the same height.
            Profile next;
            int m=0;
            auto append=[&](int height,int width) {
                if (!width) return;
                if (m && next[m-1].first==height)
                    next[m-1].second+=width;
                else next[m++]={height,width};
            };
            for (int i=0; i<n; ++i) {
                if (i!=j) append(p[i].first,p[i].second);
                else { append(y+h,w); append(y,p[i].second-w); }
            }
            int area=w*h;
            count+=search(next,m,k+1,min(minArea,area),
                          max(maxArea,area),remainingArea-area);
        }
    }
    return count;
}

struct Rectangle { int x,y,w,h; };
bool verify_witness() {
    const array<Rectangle,K> t{{
        {0,0,90,157}, {0,157,90,158}, {90,0,112,126},
        {202,0,113,126}, {90,126,75,189},
        {165,126,150,94}, {165,220,150,95}
    }};
    int sum=0, lo=TOTAL, hi=0;
    for (int i=0; i<K; ++i) {
        auto q=t[i];
        if (q.x<0 || q.y<0 || q.w<=0 || q.h<=0 ||
            q.x+q.w>N || q.y+q.h>N) return false;
        int area=q.w*q.h;
        sum+=area; lo=min(lo,area); hi=max(hi,area);
        for (int j=0; j<i; ++j) {
            auto s=t[j];
            if (minmax(q.w,q.h)==minmax(s.w,s.h)) return false;
            if (max(q.x,s.x)<min(q.x+q.w,s.x+s.w) &&
                max(q.y,s.y)<min(q.y+q.h,s.y+s.h)) return false;
        }
    }
    return sum==TOTAL && hi-lo==150;
}

int main(int argc,char** argv) {
    D=argc>1 ? atoi(argv[1]) : 149;
    if (D<0 || D>150) {
        cerr << "Use an integer bound between 0 and 150.\n";
        return 2;
    }
    if (!verify_witness()) { cerr << "Witness failed\n"; return 1; }
    cout << "witness: valid, difference = 150\n";
    lowerArea=MEAN-(K-1)*D/K;
    upperArea=MEAN+(K-1)*D/K;
    cout << "D = " << D << ", area interval = ["
         << lowerArea << ", " << upperArea << "]\n";
    Profile p;
    p[0]={0,N};
    auto count=search(p,1,0,TOTAL,0,TOTAL);
    cout << "solutions (first width <= height): " << count << '\n';
    cout << "nodes by number of placed rectangles:\n";
    for (int k=0; k<=K; ++k) cout << k << ' ' << nodes[k] << '\n';
}

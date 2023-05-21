#include <bits/stdc++.h>
using lli = long long int;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t; std::cin >> t;
    for (int _{}; _ < t; ++_) {
        int n; std::cin >> n;
        int d; std::cin >> d;
        std::vector<int> a(n);
        for (int& x : a) {
            std::cin >> x;
        }

        for (int i{}; i < n; ++i) {
            a[i] += a[i - 1];
        }
        
        for (int i{}; i < d; ++i) {
            int l; std::cin >> l;
            int r; std::cin >> r;
            lli x{(r-- - l-- + 1) * lli(i)};
            int y{a[r]};
            if (l) {
                y -= a[l - 1];
            }

            std::cout << x + y << ' ';
        }

        std::cout << '\n';
    }
}
#include <bits/stdc++.h>
using lli = long long int;

auto solve(lli& n) -> lli {
    return lli(std::sqrt(n / 2)) * 4;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t; std::cin >> t;
    for (int _{}; _ < t; ++_) {
        lli n; std::cin >> n;

        std::cout << solve(n) << '\n';
    }
}
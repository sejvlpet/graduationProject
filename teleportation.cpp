#include <bits/stdc++.h>

using namespace std;

int T, n, m, v, z_vychod, z_jih, pocet;
vector<vector<int>> a;    // tabulka pro zapis stavu policka
vector<pair<int, int>> z; // seznam dostupnych zaklinadel

bool f(const int _i, const int _j)
{
  if (_i >= m || _j >= n) // kontrola hranic mrizky - vsechna pole mimo mrizku jsou vyherni
    return 0;
  if (a[_i][_j] == -1) { // pokud hodnota neni vypocitana tak se spocita a zapise
    int _res = 1; // nejdrive predpokladame prohru
    for (auto _z : z) { // vsechna zaklinadla
      if (f(_i + _z.first, _j + _z.second)) { // pouze pokud se najde jedna moznost, kdy vyhrajeme, pak vysledek je vyhra a uz nemusime zkoumat dalsi zaklinadla
        _res = 0;
        break;
      }
    }
    // doplneni zjistene hodnoty do tabulky
    a[_i][_j] = _res;
  }
  return a[_i][_j];
}

int main()
{
  // nacteni rozmeru mrizky a poctu zaklinadel
  cin >> pocet;
  for(int i = 0; i < pocet; i++){
    cin >> m >> n >> v;

    a.clear();
    // zvetseni tabulky na pozadovanou velikost (m x n) a vyplneni -1 (jako NEVYPLNENO)
    a.resize(m, vector<int>(n, -1));

    z.clear();
    // priprava prostoru pro nacteni zaklinadel
    z.reserve(v);

    for (int line = 0; line < v; ++line) {
      cin >> z_jih >> z_vychod;
      z.push_back({ z_jih, z_vychod });
    }

    // zaciname v rohu (0,0) a to je jedine pro co ve vysledku potrebujeme vedet
    // jak hra dopadne
    cout << !f(0, 0) << endl;
  }
  return 0;
}

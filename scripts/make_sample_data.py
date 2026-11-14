"""ORNEK veri uretir: frontend/data/atlas.json

Bu dosya GERCEK FIRMS verisi DEGILDIR. Arayuz gercek veri baglanana kadar
calissin diye, mevsimsel bir profilden deterministik sahte sayilar uretir.
Gercek veri geldiginde ayni sekilde (asagidaki "Sekil") bir atlas.json yazip
meta.sample alanini false yapmak yeterli; arayuzde degisiklik gerekmez.

Sekil:
{
  "meta": {"sample": true, "generated": "...", "note": "...",
           "sensors": {"modis": {"label": "MODIS", "from": 2001, "to": 2025}, ...}},
  "provinces": {
    "Antalya": {"modis": {"2001": [oca, sub, ..., ara]}, "viirs": {...}}
  }
}
Il adlari frontend/data/tr-provinces.json icindeki "name" ile ayni olmali.

Calistir:  python scripts/make_sample_data.py
"""
import json
import math
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "frontend" / "data" / "atlas.json"

# il: (olcek, orman payi 0-1) -- orman payi yaz zirvesini, kalani hasat sonrasi anizi temsil eder
PROVINCES = {
    "İzmir": (95, 0.55), "Manisa": (120, 0.35), "Muğla": (80, 0.8),
    "Aydın": (85, 0.45), "Denizli": (60, 0.45), "Uşak": (30, 0.3),
    "Afyon": (55, 0.2), "Antalya": (110, 0.7), "Burdur": (25, 0.4),
    "Isparta": (28, 0.5), "Konya": (150, 0.1), "Karaman": (35, 0.2),
    "Mersin": (90, 0.55),
}
SENSORS = {
    "modis": {"label": "MODIS", "from": 2001, "to": 2025, "gain": 1.0},
    "viirs": {"label": "VIIRS", "from": 2012, "to": 2025, "gain": 3.6},
}
FOREST = [0.02, 0.03, 0.05, 0.08, 0.15, 0.45, 0.9, 1.0, 0.7, 0.3, 0.08, 0.03]
STUBBLE = [0.03, 0.04, 0.06, 0.08, 0.2, 0.75, 0.55, 0.3, 0.5, 1.0, 0.6, 0.1]


def main():
    rng = random.Random(2026)
    provinces = {}
    for name, (scale, forest) in PROVINCES.items():
        entry = {}
        year_factor = {y: math.exp(rng.gauss(0, 0.35)) for y in range(2001, 2026)}
        for key, s in SENSORS.items():
            years = {}
            for y in range(s["from"], s["to"] + 1):
                row = []
                for m in range(12):
                    base = forest * FOREST[m] + (1 - forest) * STUBBLE[m]
                    lam = scale * s["gain"] * base * year_factor[y] * math.exp(rng.gauss(0, 0.3))
                    row.append(max(0, round(lam)))
                years[str(y)] = row
            entry[key] = years
        provinces[name] = entry

    data = {
        "meta": {
            "sample": True,
            "generated": "scripts/make_sample_data.py",
            "note": "Örnek veri: gerçek FIRMS sayıları değildir.",
            "sensors": {k: {"label": v["label"], "from": v["from"], "to": v["to"]}
                        for k, v in SENSORS.items()},
        },
        "provinces": provinces,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"yazildi: {OUT} ({OUT.stat().st_size} bayt, {len(provinces)} il)")


if __name__ == "__main__":
    main()

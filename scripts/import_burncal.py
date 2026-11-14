"""burncal reposundaki gercek il serilerini (frontend/atlas-data.js) bu arayuzun
frontend/data/atlas.json bicimine cevirir.

Calistir:  python scripts/import_burncal.py <burncal klasoru>/frontend/atlas-data.js
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "frontend" / "data" / "atlas.json"
GEO = ROOT / "frontend" / "data" / "tr-provinces.json"
ALIAS = {"Afyonkarahisar": "Afyon", "Hakkâri": "Hakkari"}
KEYS = {"MODIS": "modis", "VIIRS": "viirs", "Birleşmiş": "merged"}


def main(src):
    text = Path(src).read_text(encoding="utf-8")
    atlas = json.loads(text[text.index("{"):text.rindex("}") + 1])
    names = {f["properties"]["name"] for f in json.loads(GEO.read_text(encoding="utf-8"))["features"]}
    provinces, sensors, unknown = {}, {}, set()
    for label, by_prov in atlas["series"].items():
        key = KEYS.get(label)
        if not key:
            continue
        years = set()
        for name, series in by_prov.items():
            name = ALIAS.get(name, name)
            if name not in names:
                unknown.add(name)
                continue
            if series:
                provinces.setdefault(name, {})[key] = series
                years.update(int(y) for y in series)
        if years:
            sensors[key] = {"label": label, "from": min(years), "to": max(years)}
    if unknown:
        sys.exit(f"Haritada karsiligi olmayan il adlari: {sorted(unknown)} (ALIAS'a ekleyin)")
    data = {"meta": {"sample": False, "generated": "scripts/import_burncal.py",
                     "note": "Kaynak: NASA FIRMS (MODIS, VIIRS S-NPP), type = 0 tespitleri.",
                     "sensors": sensors},
            "provinces": provinces}
    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"yazildi: {OUT} ({OUT.stat().st_size} bayt, {len(provinces)} il, {sensors})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])

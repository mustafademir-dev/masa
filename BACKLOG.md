# BACKLOG

## Next step
Asıl proje `onerrbaris/burncal`. Bu arayüz oraya taşındı ama push edilemedi (Claude GitHub uygulaması o hesapta kurulu değil); buradaki `frontend/` aynı kodun yedeğidir. Uygulama kurulunca `burncal`'da `yeni-harita-tasarimi` dalı açılacak.

## In progress
<!-- task – who (if two people work at once) -->

## Open
- Birleşmiş seri: `atlas.json` içinde her ile `merged` anahtarı eklenince sekme kendiliğinden dolar (arayüz hazır).
- MODIS `type == 0` filtresi 2018 kırılması: veri betiğinde konum maskesine geçilecek mi, karar bekliyor.
- Adana, Hatay ve Güneydoğu verisi (harita 81 ili gösteriyor; verisi olmayan il "veri yok" durumunda açılıyor).
- Güncel ateş noktası katmanı (NASA GIBS termal anomali karoları denendi, 400 döndü; FIRMS anahtarı gerekebilir).

## Done
- Yeni atlas arayüzü `frontend/` (dal: `yeni-harita-tasarimi`): MapLibre küre + uydu + 3B arazi, yakınlaştıkça yol/yerleşim/bina detayı, il tıklayınca sinematik uçuş ve panel (Aylar / Takvim / Kıyas, CSV), MODIS / VIIRS / Birleşmiş sekmeleri, yıl oynatma, WASD-QE-RF klavye.

## Decisions
- 2026-11-14 – Gerçek veri bağlandı: `scripts/build_atlas_json.py` (burncal içinde çalışır; `atlas-data.js` + `harmonized-data.js` okur, Birleşmiş seri ve doğrulama güveni dahil) → 81 il, MODIS 2000–2025, VIIRS 2012–2025 (`type == 0` filtreli, burncal `scripts/build_izmir_atlas.py` çıktısı). burncal verisi değişince betik yeniden çalıştırılır.
- 2026-11-14 – Birim il (bölge değil). Fable mimarisinden çok yıllı takvim, medyan kıyası, güven göstergesi ve CSV alındı; bölge vurgusu alınmadı.
- 2026-11-14 – Düz HTML + JS korunur, derleme adımı yok. Harita için MapLibre GL 5.6.0 `frontend/vendor/` içine kopyalandı.
- 2026-11-14 – Karolar anahtarsız: Esri World Imagery (uydu), OpenFreeMap (vektör detay ve yazı tipleri), AWS Terrain Tiles (yükseklik). Değiştirmek için `frontend/js/mapstyle.js` içindeki `sources`.
- 2026-11-14 – İl sınırları: cihadturhan/tr-geojson (OSM, ODbL) → `frontend/data/tr-provinces.json`.

## Çalıştırma
`cd frontend` → `python -m http.server 8000` → http://localhost:8000 (açılış animasyonunu atlamak için `?hizli`).

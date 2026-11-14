# BACKLOG

## Next step
Barış'ın mevcut atlası (13 illik gerçek veri) repoda yok: onu push et, sonra gerçek sayıları `frontend/data/atlas.json` şekline çevirip `meta.sample` alanını `false` yap (şekil: `scripts/make_sample_data.py` başındaki açıklama).

## In progress
<!-- task – who (if two people work at once) -->

## Open
- Gerçek FIRMS verisini `atlas.json` şekline çeviren Python betiği (şu an ÖRNEK veri gösteriliyor, arayüzde "Örnek veri" rozeti var).
- Birleşmiş seri: `atlas.json` içinde her ile `merged` anahtarı eklenince sekme kendiliğinden dolar (arayüz hazır).
- MODIS `type == 0` filtresi 2018 kırılması: veri betiğinde konum maskesine geçilecek mi, karar bekliyor.
- Adana, Hatay ve Güneydoğu verisi (harita 81 ili gösteriyor; verisi olmayan il "veri yok" durumunda açılıyor).
- Güncel ateş noktası katmanı (NASA GIBS termal anomali karoları denendi, 400 döndü; FIRMS anahtarı gerekebilir).

## Done
- Yeni atlas arayüzü `frontend/` (dal: `yeni-harita-tasarimi`): MapLibre küre + uydu + 3B arazi, yakınlaştıkça yol/yerleşim/bina detayı, il tıklayınca sinematik uçuş ve panel (Aylar / Takvim / Kıyas, CSV), MODIS / VIIRS / Birleşmiş sekmeleri, yıl oynatma, WASD-QE-RF klavye.

## Decisions
- 2026-11-14 – Birim il (bölge değil). Fable mimarisinden çok yıllı takvim, medyan kıyası, güven göstergesi ve CSV alındı; bölge vurgusu alınmadı.
- 2026-11-14 – Düz HTML + JS korunur, derleme adımı yok. Harita için MapLibre GL 5.6.0 `frontend/vendor/` içine kopyalandı.
- 2026-11-14 – Karolar anahtarsız: Esri World Imagery (uydu), OpenFreeMap (vektör detay ve yazı tipleri), AWS Terrain Tiles (yükseklik). Değiştirmek için `frontend/js/mapstyle.js` içindeki `sources`.
- 2026-11-14 – İl sınırları: cihadturhan/tr-geojson (OSM, ODbL) → `frontend/data/tr-provinces.json`.

## Çalıştırma
`cd frontend` → `python -m http.server 8000` → http://localhost:8000 (açılış animasyonunu atlamak için `?hizli`).

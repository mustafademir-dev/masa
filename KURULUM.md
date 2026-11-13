# Kurulum

## İkimiz de (hackathon'dan önce)
1. `claude --version` → **2.1.321 veya üstü** (Fable 5.2 için). Değilse `claude update`.
2. claude.ai → Ayarlar → **usage credits kapalı**.
3. Fable reset'ini harcama, hackathon'a sakla.
4. Repoyu klonla. Skill repoyla geliyor, ayrıca bir şey kurmaya gerek yok. Klasörde `claude` → `/orchestration` yazınca görünüyorsa hazır.

## Hackathon günü
- Başlangıç: `/model fable` → `/orchestration mimari`
- Sonra: `/orchestration insa`
- Fable çok yerse: `/model opus` (Sonnet'e asla geçme)
- Son ~4 saat: `/orchestration final`

## Hesap değiştirme (biri limite takılınca)
1. Limiti biten hesapta: "BACKLOG.md'yi güncelle, commit ve push et" de.
2. Diğer hesapta: `git pull` → `claude` → `/model fable` → `/orchestration insa` → "BACKLOG.md'yi oku, Next step'ten devam et".

## Aynı anda ikimiz çalışırsak
Herkes BACKLOG.md'de aldığı işin yanına adını yazar, sadece o işin dosyalarına dokunur. Sık `git pull`, küçük commit.

# Kurulum

## Mustafa (bir kere, repoyu GitHub'a atmadan önce)
WSL'de repo klasöründe:
```
python3 setup_skill.py --global
```
Skill'i hem repodaki `.claude/skills/` klasörüne hem global'e kurar. Sonra `.claude/` dahil her şeyi commit edip push et. Arkadaşın klonlayınca skill hazır gelir.

## İkimiz de (Cuma, hackathon'dan önce)
1. `claude --version` → **2.1.321 veya üstü** olmalı (Fable 5.2 için). Değilse `claude update`.
2. claude.ai → Ayarlar → **usage credits kapalı** olsun (Fable %50 sınırını aşınca para yemesin).
3. Fable reset'ini harcama, hackathon'a sakla.

## Arkadaşım (Windows, WSL yok)
1. Git for Windows kurulu olsun (`git --version`).
2. Repoyu klonla, klasöre gir, `claude` yaz.
3. `/orchestration` yazınca skill listede çıkıyorsa hazırsın. Ekstra bir şey kurmana gerek yok, skill repodan geliyor.

## Hackathon günü
- Mustafa: `/model fable` → `/orchestration mimari`
- Mimari bitince ikimiz de: `/model fable` → `/orchestration insa`
- Fable çok yerse: `/model opus` (Sonnet'e asla geçme)
- Son ~4 saat: `/orchestration final`
- Oturum koparsa: aynı komut + "kendi BACKLOG dosyanı oku, kaldığın yerden devam et"

## Kurallar (kısa)
- Mustafa → `backend/` + `BACKLOG_BACKEND.md`, arkadaşım → `frontend/` + `BACKLOG_FRONTEND.md`
- `shared/` ve `ARCHITECTURE.md` sadece ikimiz anlaşınca değişir
- Sık `git pull`, küçük commit
- Reset'leri aynı anda harcamayalım

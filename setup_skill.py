"""Copies skill-src/orchestration into this repo's .claude/skills (and with --global, into ~/.claude/skills).
Works on Windows and WSL/Linux. Run from anywhere: python setup_skill.py [--global]"""
import shutil, sys, time
from pathlib import Path

root = Path(__file__).resolve().parent
src = root / "skill-src" / "orchestration"
targets = [root / ".claude" / "skills" / "orchestration"]
if "--global" in sys.argv:
    targets.append(Path.home() / ".claude" / "skills" / "orchestration")

for dest in targets:
    if dest.exists():
        # back up OUTSIDE skills/ so Claude Code doesn't load the backup as a second skill
        backup = dest.parent.parent / "skill-backups" / f"orchestration.{int(time.time())}"
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(dest), str(backup))
        print(f"backup: {backup}")
    shutil.copytree(src, dest)
    print(f"installed: {dest}")
    for f in sorted(dest.rglob("*")):
        if f.is_file():
            print("  ", f.relative_to(dest))

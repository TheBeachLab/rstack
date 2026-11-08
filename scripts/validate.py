#!/usr/bin/env python3
"""Validate the portable bundle against Rakazo's text-plugin constraints."""
import json
import re
from pathlib import Path


def validate(root):
    manifest = json.loads((root / "plugin.json").read_text())
    assert manifest["name"] == "rstack"
    upstream = json.loads((root / "upstream.json").read_text())
    catalog = json.loads((root / "skills/rstack/references/catalogue.json").read_text())
    entries = {s["name"]: s for s in catalog["skills"]}
    expected = {s["installed_name"] for s in upstream["skills"].values()}
    expected |= set(upstream["helper_roles"].values())
    expected |= set(upstream["optional_recipes"]) | {"rstack"}
    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    assert actual == expected == set(entries), "Incomplete or unexpected skill inventory"
    assert len(actual) == 64 and "interrogate" not in actual and "pstack" not in actual
    fetched = [root / "plugin.json"]
    calls = 0
    for name in sorted(actual):
        folder = root / "skills" / name
        skill = folder / "SKILL.md"
        text = skill.read_text()
        header = text.split("---", 2)[1]
        assert re.search(r"^name: " + re.escape(name) + "$", header, re.M), name
        description = json.loads(re.search(r"^description: (.+)$", header, re.M)[1])
        assert description == entries[name]["description"] and description.strip(), name
        assert '"file":"references/rakazo.md"' in text, name
        companions = [p for p in folder.rglob("*") if p.is_file() and p != skill]
        assert sorted(str(p.relative_to(folder)) for p in companions) == entries[name]["files"], name
        assert len(companions) <= 40 and sum(p.stat().st_size for p in companions) <= 400_000, name
        for file in [skill, *companions]:
            assert not file.is_symlink() and file.stat().st_size <= 100_000, file
            assert file.suffix in {".md", ".mdx", ".txt", ".json", ".yaml", ".yml", ".csv"}, file
            body = file.read_text()
            if file.suffix == ".md":
                assert not re.search(r"\.cursor/|pstack-models|grok-4|claude-opus|`Task`|generalPurpose|readonly:|run_in_background:|update_state|SendToUser|AskQuestion", body), file
                assert not re.search(r"/Users/|/home/[a-z][a-z0-9_-]*/|BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY", body), file
                for literal in re.findall(r"skill_read\((\{[^\n}]*\})\)", body):
                    args = json.loads(literal)
                    if "<" in args.get("file", ""):
                        continue
                    target = root / "skills" / args["name"] / args.get("file", "SKILL.md")
                    assert target.is_file(), (file, args)
                    calls += 1
                for target in re.findall(r"\]\(([^)]+)\)", body):
                    if "://" not in target and target not in {"url", "<url>"} and not target.startswith(("#", "mailto:")):
                        assert (file.parent / target.split("#")[0]).exists(), (file, target)
        fetched.extend([skill, *companions])
    assert len(fetched) <= 200 and sum(p.stat().st_size for p in fetched) <= 4_000_000
    print(json.dumps({"skills": len(actual), "fetched_files": len(fetched), "resource_calls_checked": calls, "status": "valid"}))


if __name__ == "__main__":
    validate(Path(__file__).resolve().parents[1])

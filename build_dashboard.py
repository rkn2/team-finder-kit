"""Embed the sample roster and sample result into dashboard.html (run after editing either)."""
import json, pathlib
d = pathlib.Path(__file__).parent
src = (d / "dashboard.src.html").read_text()
src = src.replace('/*SAMPLE_CSV*/""', json.dumps((d / "sample-roster.csv").read_text()))
src = src.replace("/*SAMPLE_RESULT*/null", json.dumps(json.loads((d / "sample-result.json").read_text())))
(d / "dashboard.html").write_text(src)
print("wrote dashboard.html")

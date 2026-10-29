# Builds the two Slides batchUpdate request files for the other-biases deck.
# Run link_lines.py with DECK_DIR=deck_other ... > /tmp/claude-0/o_lnk.json first.
import json
src = open("scripts/build_deck.py").read()
src = src[:src.index('if __name__ == "__main__" and sys.argv[1] == "templates"')]
ns = {"__file__": "scripts/build_deck.py", "__name__": "bd"}
exec(src, ns)
ns["ELEMS"]["fig"] = ns["ELEMS"]["fig"] + ["_lnk"]
d = json.load(open("deck_other/slides.json"))["slides"]
lnk = json.load(open("/tmp/claude-0/o_lnk.json"))
text = {r["insertText"]["objectId"]: r["insertText"]["text"] for r in lnk if "insertText" in r}
spans = [r for r in lnk if "updateTextStyle" in r and r["updateTextStyle"]["textRange"]["type"] == "FIXED_RANGE"
         and r["updateTextStyle"]["objectId"].endswith("_lnk")]
missing = []
for half, (sl, idx) in enumerate(((d[:21], 1), (d[21:], 22))):
    reqs = []
    for i, s in enumerate(sl):
        r = ns["compact"](s, idx + i)
        if s["kind"] == "section":
            r = [x for x in r if not ("replaceAllText" in x and x["replaceAllText"]["containsText"]["text"] in ("{{body}}", "{{source}}"))]
        if s["kind"] == "fig":
            t = text.get(s["id"] + "_lnk")
            if t is None: missing.append(s["id"]); t = ""
            r.append({"replaceAllText": {"containsText": {"text": "{{lnk}}", "matchCase": True}, "replaceText": t, "pageObjectIds": [s["id"]]}})
            r += [x for x in spans if x["updateTextStyle"]["objectId"] == s["id"] + "_lnk"]
        reqs += r
    json.dump(reqs, open(f"/tmp/claude-0/o_batch{half}.json", "w"), separators=(",", ":"), ensure_ascii=False)
    print(half, len(reqs), len(json.dumps(reqs, ensure_ascii=False)))
print("missing", missing)

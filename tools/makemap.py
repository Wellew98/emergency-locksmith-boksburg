import math

P = {
 "Atlasville":(-26.1556425,28.2848199),"Beyers Park":(-26.1876655,28.2614332),
 "Boksburg Central":(-26.2230665,28.2490915),"Boksburg East":(-26.2267793,28.2888392),
 "Boksburg North":(-26.205137,28.255586),"Boksburg South":(-26.2288576,28.2775119),
 "Boksburg West":(-26.196389,28.2395052),"Cason":(-26.2107548,28.2577787),
 "Dawn Park":(-26.3049755,28.243891),"Parkrand":(-26.2459107,28.2672801),
 "Sunward Park":(-26.2592913,28.255564),"Vosloorus":(-26.3631503,28.2076069),
}

W = 400
S = 16.0                       # px per km, identical on both axes
LAT_KM = 110.574
LNG_KM = 111.320 * math.cos(math.radians(26.25))

lat0 = max(v[0] for v in P.values())   # northernmost
lng0 = min(v[1] for v in P.values())   # westernmost

def xy(lat, lng):
    return ((lng - lng0) * LNG_KM * S, (lat0 - lat) * LAT_KM * S)

raw = {k: xy(*v) for k, v in P.items()}
mapw = max(x for x, y in raw.values())
maph = max(y for x, y in raw.values())
TOP = 26
OFFX = 112.0
pts = {k: (x + OFFX, y + TOP) for k, (x, y) in raw.items()}
H = int(maph + TOP + 62)

# label placement: left or right gutter, de-collided vertically
LH = 15.0
def place(side_names, x_anchor, anchor):
    out = {}
    order = sorted(side_names, key=lambda n: pts[n][1])
    ys = []
    for n in order:
        y = pts[n][1] + 3.5
        if ys and y - ys[-1] < LH:
            y = ys[-1] + LH
        ys.append(y)
    span = ys[-1] - ys[0]
    lift = min(0, (TOP + maph) - ys[-1])
    for n, y in zip(order, ys):
        out[n] = (x_anchor, y + lift, anchor)
    return out

_by_x = sorted(P, key=lambda n: pts[n][0])
left, right = _by_x[:6], _by_x[6:]
lab = {}
lab.update(place(left, OFFX - 12, "end"))
lab.update(place(right, OFFX + mapw + 12, "start"))


def esc(s):
    return s.replace("&", "&amp;")


def build(active=None):
    a = []
    a.append('<svg viewBox="0 0 %d %d" role="img" aria-labelledby="mapT mapD" focusable="false">' % (W, H))
    title = "Boksburg suburbs we cover" if not active else "Where %s sits in our Boksburg coverage" % active
    desc = ("Twelve suburb centres plotted to scale across roughly 8 km east to west and 23 km "
            "north to south, from Atlasville in the north to Vosloorus in the south."
            + ("" if not active else " %s is highlighted." % active))
    a.append('<title id="mapT">%s</title><desc id="mapD">%s</desc>' % (esc(title), esc(desc)))

    panel_top, panel_bot = TOP - 18, H - 44
    a.append('<rect x="0" y="%.1f" width="%d" height="%.1f" fill="#F1EEE8"/>' % (panel_top, W, panel_bot - panel_top))

    # north-south ruler, 5 km ticks, same scale as the plot
    rx = 13
    a.append('<g stroke="#101418" stroke-opacity=".45" stroke-width="1.5">')
    a.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (rx, TOP, rx, TOP + maph))
    km = 0
    while km * S <= maph + 0.5:
        a.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (rx, TOP + km * S, rx + 5, TOP + km * S))
        km += 5
    a.append('</g>')
    a.append('<g font-family="\'Public Sans\', Arial, sans-serif" font-size="9.5" fill="#5C666F">')
    km = 0
    while km * S <= maph + 0.5:
        a.append('<text x="%.1f" y="%.1f" text-anchor="middle">%d</text>' % (rx, TOP + km * S - 6, km))
        km += 5
    a.append('<text x="%.1f" y="%.1f" text-anchor="middle">km</text>' % (rx, TOP + maph + 14))
    a.append('<text x="%d" y="%.1f" text-anchor="end">N &#8593;</text>' % (W - 10, TOP - 4))
    a.append('</g>')

    # leader lines
    a.append('<g stroke="#101418" stroke-opacity=".3" stroke-width="1">')
    for n in P:
        px, py = pts[n]
        lx, ly, an = lab[n]
        ex = lx - 3 if an == "end" else lx + 3
        a.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f" fill="none"/>'
                 % (px, py, (px + ex) / 2, ly, ex, ly))
    a.append('</g>')

    for n in P:
        px, py = pts[n]
        if n == active:
            a.append('<circle cx="%.1f" cy="%.1f" r="9.5" fill="#F0C419" stroke="#101418" stroke-width="2.5"/>' % (px, py))
            a.append('<circle cx="%.1f" cy="%.1f" r="3" fill="#101418"/>' % (px, py))
        else:
            a.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#ffffff" stroke="#101418" stroke-width="2"/>' % (px, py))

    a.append('<g font-family="\'Public Sans\', Arial, sans-serif" font-size="11">')
    for n in P:
        lx, ly, an = lab[n]
        if n == active:
            a.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-weight="800" fill="#101418">%s</text>'
                     % (lx, ly, an, esc(n.upper())))
        else:
            a.append('<text x="%.1f" y="%.1f" text-anchor="%s" fill="#3E464D">%s</text>'
                     % (lx, ly, an, esc(n)))
    a.append('</g>')

    by = H - 22
    bx = 13
    a.append('<g stroke="#101418" stroke-width="2">'
             '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/></g>'
             % (bx, by, bx + 5 * S, by, bx, by - 4, bx, by + 4, bx + 5 * S, by - 4, bx + 5 * S, by + 4))
    a.append('<g font-family="\'Public Sans\', Arial, sans-serif" font-size="11" fill="#5C666F">')
    a.append('<text x="%.1f" y="%.1f">5 km</text>' % (bx + 5 * S + 9, by + 4))
    a.append('</g>')
    a.append('</svg>')
    return "\n".join(a)


CAP = ("Suburb centres plotted to scale from verified coordinates. Positions are centre points, "
       "not service boundaries. Atlasville to Vosloorus is about 24 km, so tell us the suburb "
       "and the nearest main road when you call.")

def figure(active=None):
    return ('<figure class="fig fig--map">\n' + build(active) +
            '\n<figcaption>' + CAP + '</figcaption>\n</figure>')

if __name__ == "__main__":
    print("viewBox 400 x", H)
    open("/tmp/_map_preview.html", "w").write(
        '<link rel="stylesheet" href="/assets/style.css"><div class="wrap" style="padding:20px">'
        + figure("Sunward Park") + '</div>')

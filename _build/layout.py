import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFFICIAL = "https://chapellawsolicitors.co.uk/"
FIRM = "Chapel Law Solicitors Limited"
EMAIL = "info@chapellawsolicitors.co.uk"
TEL = "+44 (0)20 3161 7187"
TEL_HREF = "tel:+442031617187"
WA = "https://wa.me/447899771229"
WA_TEL = "+44 (0)7899 771229"
WECHAT = "ChapelLawSolicitors"
ADDRESS = "Office 207, Atlas Business Centre, London NW2 7HJ"
ADDRESS_SHORT = "Atlas Business Centre, London NW2 7HJ"
MAPS = "https://www.google.com/maps/search/?api=1&query=Atlas+Business+Centre+London+NW2+7HJ"
SRA_BADGE = "https://cdn.yoshki.com/iframe/55845r.html"

LANGS = {
    "en": {"prefix": "", "html": "en-GB", "label": "EN", "name": "English"},
    "zh": {"prefix": "zh/", "html": "zh-Hans", "label": "中文", "name": "简体中文"},
}

_cur = ["en"]


def cur():
    return _cur[0]


def set_lang(lang):
    _cur[0] = lang


def L(en, zh):
    """Pick the text for the language being built."""
    return en if cur() == "en" else zh


def root():
    """Relative path from a page back to the site root."""
    return "../" if LANGS[cur()]["prefix"] else ""


ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "chat": '<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/>',
    "wechat": '<path d="M9.5 4C5.4 4 2 6.8 2 10.2c0 2 1.1 3.7 2.8 4.8L4 17.5l2.9-1.5c.8.2 1.7.4 2.6.4"/><path d="M15.5 9.5c-3.6 0-6.5 2.4-6.5 5.3s2.9 5.3 6.5 5.3c.7 0 1.4-.1 2-.3l2.5 1.2-.6-2.1c1.6-1 2.6-2.5 2.6-4.1 0-2.9-2.9-5.3-6.5-5.3z"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "ext": '<path d="M7 17 17 7M9 7h8v8"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "copy": '<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    # practice areas
    "passport": '<rect x="5" y="2" width="14" height="20" rx="2"/><circle cx="12" cy="10" r="3.2"/><path d="M8.8 10h6.4M12 6.8c-1 1-1.4 2-1.4 3.2s.4 2.2 1.4 3.2c1-1 1.4-2 1.4-3.2S13 7.8 12 6.8zM9 17h6"/>',
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
    "building": '<path d="M4 21V5l8-3v19M12 8l8 3v10"/><path d="M2 21h20M7.5 8h1M7.5 12h1M7.5 16h1M15.5 13h1M15.5 17h1"/>',
    "family": '<circle cx="8" cy="6" r="2.5"/><circle cx="16.5" cy="8" r="2"/><path d="M3.5 21v-5.5A4.5 4.5 0 0 1 8 11a4.5 4.5 0 0 1 4.5 4.5V21"/><path d="M13.5 21v-4a3 3 0 0 1 6 0v4"/>',
    "briefcase": '<rect x="2.5" y="7" width="19" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M2.5 12.5h19"/>',
    "shield": '<path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10z"/><path d="M12 8v4M12 15.5v.5"/>',
    "scales": '<path d="M12 3v18M7 21h10M5 7h14"/><path d="M5 7 2 14a3.5 3.5 0 0 0 6 0L5 7zM19 7l-3 7a3.5 3.5 0 0 0 6 0l-3-7z"/>',
}


def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


MARK = ('<svg class="brand-mark" viewBox="0 0 48 48" fill="none" stroke="currentColor" aria-hidden="true">'
        '<path d="M11 5H5v38h6M37 5h6v38h-6" stroke-width="2.6"/>'
        '<path d="M14 10h20" stroke-width="2.6"/>'
        '<path d="M15.5 15h17" stroke-width="2"/>'
        '<path d="M18 15c-3.4 0-3.4 5 0 5 1.6 0 1.6-2.4 0-2.4M30 15c3.4 0 3.4 5 0 5-1.6 0-1.6-2.4 0-2.4" stroke-width="1.6"/>'
        '<path d="M20 21v16M28 21v16" stroke-width="3"/>'
        '<path d="M23 22v15M25 22v15" stroke-width="1"/>'
        '<path d="M16 39h16" stroke-width="2.6"/>'
        '</svg>')


def brand(href):
    return f'''<a class="brand" href="{href}" aria-label="Chapel Law Solicitors 盛倫律師事務所 — {L("home", "首页")}">
      {MARK}
      <span class="brand-text"><span class="brand-name">Chapel Law</span><span class="brand-sub">Solicitors</span></span>
      <span class="brand-cn" lang="zh-Hant"><span>盛</span><span>倫</span></span>
    </a>'''


def nav_items():
    return [
        ("services", "services.html", L("Practice areas", "业务范围")),
        ("fees", "fees.html", L("Fixed fees", "收费标准")),
        ("about", "about.html", L("About us", "关于我们")),
        ("contact", "contact.html", L("Contact", "联系我们")),
    ]


def page(rel, *, key, title, description, body):
    """Write one page for the current language. `rel` is the path inside a language root."""
    lang = cur()
    out_path = os.path.join(OUT, LANGS[lang]["prefix"] + rel)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    r = root()
    nav = "\n".join(
        f'<a href="{href}"{" aria-current=\"page\"" if k == key else ""}>{label}</a>'
        for k, href, label in nav_items()
    )
    switch = "".join(
        f'<a href="{r}{v["prefix"]}{rel}" lang="{v["html"]}" hreflang="{v["html"]}"'
        f'{" aria-current=\"true\"" if k == lang else ""}>{v["label"]}</a>'
        for k, v in LANGS.items()
    )
    fonts = ("family=Noto+Serif+TC:wght@600&text=%E7%9B%9B%E5%80%AB%E7%B2%B5%E8%AA%9E&family=Inter:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400"
             + ("&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@500;600" if lang == "zh" else ""))

    html = f"""<!doctype html>
<html lang="{LANGS[lang]["html"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#16181d">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="{r}assets/css/style.css">
</head>
<body class="lang-{lang}">
<a class="skip" href="#main">{L("Skip to content", "跳至主要内容")}</a>
<div class="concept-bar" role="note">
  <div class="container concept-inner">
    <p><span class="concept-tag">{L("Concept", "概念设计")}</span><span class="concept-long">{L(f'Concept redesign. Not the <a href="{OFFICIAL}" target="_blank" rel="noopener">official Chapel Law Solicitors website</a>.', f'概念设计展示，并非 <a href="{OFFICIAL}" target="_blank" rel="noopener">盛伦律师事务所官方网站</a>。')}</span></p>
    <a href="https://ux-circles.com/web" target="_blank" rel="noopener"><span class="concept-by">{L("Designed by ", "设计：")}</span><strong>UX CIRCLES</strong> {icon("ext", "")}</a>
  </div>
</div>
<header class="site-header">
  <div class="container header-inner">
    {brand("index.html")}
    <nav class="nav" id="site-nav" aria-label="{L("Main", "主导航")}">
      {nav}
      <div class="nav-extra">
        <a class="nav-phone" href="{TEL_HREF}">{icon("phone")}<span>020 3161 7187</span></a>
        <a class="btn btn-primary" href="contact.html#enquiry">{L("Free consultation", "免费咨询")}</a>
      </div>
    </nav>
    <div class="header-tools">
      <div class="lang-switch" aria-label="{L("Language", "语言")}">{switch}</div>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{L("Menu", "菜单")}">{icon("menu", "ic-open")}{icon("close", "ic-close")}</button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        {brand("index.html")}
        <p>{L("Bilingual solicitors in London. English, Mandarin and Cantonese.", "伦敦双语律师事务所，提供普通话、粤语及英语服务。")}</p>
        <div class="sra-badge">
          <div class="sra-badge-inner"><iframe title="{L("SRA digital badge", "SRA 律师监管局认证徽章")}" loading="lazy" src="{SRA_BADGE}"></iframe></div>
        </div>
      </div>
      <div>
        <h2 class="footer-h">{L("Practice areas", "业务范围")}</h2>
        <ul class="footer-links">
          <li><a href="services.html#immigration">{L("UK immigration", "英国移民")}</a></li>
          <li><a href="services.html#residential">{L("Residential property", "住宅物业")}</a></li>
          <li><a href="services.html#commercial">{L("Commercial property", "商业物业")}</a></li>
          <li><a href="services.html#family">{L("Family law", "家事法")}</a></li>
          <li><a href="services.html#business">{L("Business law", "商业法")}</a></li>
          <li><a href="services.html#injury">{L("Personal injury", "人身伤害")}</a></li>
          <li><a href="services.html#criminal">{L("Criminal law", "刑事法")}</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-h">{L("The firm", "律所")}</h2>
        <ul class="footer-links">
          <li><a href="about.html">{L("About us", "关于我们")}</a></li>
          <li><a href="fees.html">{L("Fixed fees", "收费标准")}</a></li>
          <li><a href="careers.html">{L("Careers", "招聘")}</a></li>
          <li><a href="complaints.html">{L("Complaints", "投诉程序")}</a></li>
          <li><a href="contact.html">{L("Contact", "联系我们")}</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-h">{L("Get in touch", "联系方式")}</h2>
        <ul class="footer-contact">
          <li>{icon("phone")}<a href="{TEL_HREF}">{TEL}</a></li>
          <li>{icon("chat")}<a href="{WA}" target="_blank" rel="noopener">WhatsApp {WA_TEL}</a></li>
          <li>{icon("wechat")}<span>{L("WeChat", "微信")}: {WECHAT}</span></li>
          <li>{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{icon("pin")}<span>{ADDRESS}</span></li>
          <li>{icon("clock")}<span>{L("Mon–Fri, 9:30am–6:30pm", "周一至周五 9:30–18:30")}</span></li>
        </ul>
      </div>
    </div>
    <div class="regulatory">
      <p>{L(f"{FIRM} is a firm of solicitors authorised and regulated by the Solicitors Regulation Authority. The information on this website is general information only and is not legal advice.",
             f"{FIRM}（盛伦律师事务所）为英国律师监管局（SRA）授权及监管的律师事务所。本网站内容仅供一般参考，不构成法律意见。")}</p>
      <p>© <span id="year">2026</span> {FIRM} · <a href="complaints.html">{L("Complaints procedure", "投诉程序")}</a><br><span class="concept-note">{L("Unofficial redesign concept by", "非官方概念设计，由")} <a href="https://ux-circles.com/web" target="_blank" rel="noopener">UX CIRCLES</a>{L("", " 设计")}</span></p>
    </div>
  </div>
</footer>
<div class="mobile-cta">
  <a href="{TEL_HREF}">{icon("phone")}<span>{L("Call", "致电")}</span></a>
  <a href="{WA}" target="_blank" rel="noopener">{icon("chat")}<span>WhatsApp</span></a>
  <a class="primary" href="contact.html#enquiry">{icon("mail")}<span>{L("Free consultation", "免费咨询")}</span></a>
</div>
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

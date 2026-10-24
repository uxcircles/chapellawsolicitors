"""Build every page in English (/) and Simplified Chinese (/zh/).

    python3 _build/pages.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import layout  # noqa: E402
from layout import (ADDRESS, EMAIL, LANGS, MAPS, TEL, TEL_HREF, WA, WA_TEL, WECHAT, L, icon, page,  # noqa: E402
                    set_lang)
from fees import GROUPS  # noqa: E402


# ===================================================================== Shared data

def areas():
    return [
        {
            "id": "immigration", "icon": "passport",
            "name": L("UK immigration", "英国移民"),
            "short": L("Visas, settlement, citizenship, appeals and sponsor licences.",
                       "签证、永居、入籍、上诉及雇主担保执照。"),
            "intro": L("Most of our work is immigration. We prepare and submit applications, explain what the Home Office will look for, and take on refusals, appeals and reviews. You get a fixed fee before we start.",
                       "移民是我们的主要业务。我们负责准备及递交申请，向您解释移民局的审核重点，也处理拒签、上诉及复审个案。开始工作前，您会先收到固定收费报价。"),
            "items": [
                L("Spouse, partner, child and family visas", "配偶、伴侣、子女及家庭签证"),
                L("Skilled Worker visas and sponsor licences for employers", "技术工人签证及雇主担保执照"),
                L("Student, Child Student and visitor visas", "学生、儿童学生及访问签证"),
                L("Global Talent and business routes", "全球人才及商业类签证"),
                L("Indefinite leave to remain and British citizenship", "永久居留（ILR）及英国入籍"),
                L("Long residence, 7-year child and human rights applications", "长期居留、儿童七年规则及人权申请"),
                L("Appeals, administrative review and judicial review", "上诉、行政复审及司法复核"),
                L("Immigration bail and civil penalties for illegal working", "移民保释及非法用工罚款"),
            ],
            "fees": "fees.html#family",
        },
        {
            "id": "residential", "icon": "home",
            "name": L("Residential property", "住宅物业"),
            "short": L("Buying and selling homes, freehold or leasehold.",
                       "住宅买卖，永久产权或租赁产权。"),
            "intro": L("We handle the conveyancing when you buy or sell a home in England and Wales, from searches and contracts to completion and registration. We explain each document in Chinese if you prefer.",
                       "在英格兰及威尔士买卖住宅时，我们处理整个产权转让流程：查册、合同、交割到产权登记。如有需要，每份文件都可以用中文向您解释。"),
            "items": [
                L("Buying and selling freehold and leasehold property", "买卖永久产权及租赁产权物业"),
                L("Searches, title checks and contract review", "查册、业权审查及合同审阅"),
                L("Working with your mortgage lender", "与按揭银行对接"),
                L("Completion and Land Registry registration", "交割及土地注册处登记"),
            ],
            "fees": "fees.html#residential",
        },
        {
            "id": "commercial", "icon": "building",
            "name": L("Commercial property", "商业物业"),
            "short": L("Leases, assignments, renewals and freehold purchases for businesses.",
                       "商业租约、转让、续期及永久产权买卖。"),
            "intro": L("For shops, restaurants, offices and other business premises, we act for tenants, landlords and buyers on leases and purchases.",
                       "适用于商铺、餐厅、办公室等商业物业，我们代表租客、业主及买家处理租约及物业买卖。"),
            "items": [
                L("New leases, assignments and sublets", "新租约、租约转让及转租"),
                L("Lease renewals", "租约续期"),
                L("Freehold purchases and long leases", "永久产权及长期租约买卖"),
            ],
            "fees": "fees.html#commercial",
        },
        {
            "id": "family", "icon": "family",
            "name": L("Family law", "家事法"),
            "short": L("Divorce, arrangements for children and dividing property.",
                       "离婚、子女安排及财产分割。"),
            "intro": L("When a relationship ends, we help you understand your options and reach an arrangement that protects you and your children.",
                       "婚姻或关系结束时，我们帮助您了解可行方案，争取保障您和子女的安排。"),
            "items": [
                L("Divorce and dissolution of civil partnership", "离婚及解除民事伴侣关系"),
                L("Child arrangements and custody disputes", "子女抚养及探视安排纠纷"),
                L("Dividing property and finances", "财产及财务分割"),
            ],
            "fees": None,
        },
        {
            "id": "business", "icon": "briefcase",
            "name": L("Business law", "商业法"),
            "short": L("Setting up companies, business deals, employment and tax issues.",
                       "成立公司、商业交易、雇佣及税务事宜。"),
            "intro": L("We help owners start and run businesses in the UK: setting up the company, buying or selling a business, and dealing with staff and HMRC issues.",
                       "我们协助企业主在英国创业及经营：成立公司、买卖生意，以及处理员工和税务（HMRC）事宜。"),
            "items": [
                L("Setting up a company", "成立公司"),
                L("Buying and selling a business", "生意买卖"),
                L("Employment disputes and work visa compliance", "劳资纠纷及工作签证合规"),
                L("Tax issues", "税务问题"),
            ],
            "fees": None,
        },
        {
            "id": "injury", "icon": "shield",
            "name": L("Personal injury", "人身伤害"),
            "short": L("Compensation claims after an accident or injury.",
                       "意外或受伤后的赔偿申索。"),
            "intro": L("If you have been injured in an accident that was not your fault, we can tell you whether you have a claim and pursue the compensation you are owed.",
                       "如果您在非因自己过失的意外中受伤，我们可以评估您是否有权索偿，并为您争取应得的赔偿。"),
            "items": [
                L("Road traffic accidents", "交通意外"),
                L("Accidents at work", "工伤"),
                L("Slips, trips and other accidents in public places", "公共场所滑倒、绊倒等意外"),
            ],
            "fees": None,
        },
        {
            "id": "criminal", "icon": "scales",
            "name": L("Criminal law", "刑事法"),
            "short": L("Police investigations, criminal cases and appeals.",
                       "警方调查、刑事案件及上诉。"),
            "intro": L("If you are under investigation or have been charged, we can advise and represent you, and help with appeals.",
                       "如果您正被调查或已被起诉，我们可以为您提供法律意见及代理，并处理上诉。"),
            "items": [
                L("Police interviews and investigations", "警方问话及调查"),
                L("Criminal cases at court", "法庭刑事案件"),
                L("Appeals", "上诉"),
            ],
            "fees": None,
        },
    ]


def popular_fees():
    return [
        (L("Spouse or partner visa", "配偶或伴侣签证"), "£1,300"),
        (L("Skilled Worker visa", "技术工人签证"), "£1,250"),
        (L("Indefinite leave to remain", "永久居留（ILR）"), "£1,000"),
        (L("British citizenship", "英国入籍"), "£1,050"),
        (L("Buying or selling a freehold home", "买卖永久产权住宅"), "£1,400"),
    ]


def cta_band():
    return f'''
<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>{L("Not sure where to start?", "不知道从何开始？")}</h2>
      <p>{L("Tell us what is happening. Your first consultation is free, and we reply the same or next working day.",
             "告诉我们您的情况。首次咨询免费，我们会在当天或下一个工作日回复。")}</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-light" href="contact.html#enquiry">{L("Book a free consultation", "预约免费咨询")} {icon("arrow")}</a>
      <a class="btn btn-ghost-light" href="{TEL_HREF}">{icon("phone")} 020 3161 7187</a>
    </div>
  </div>
</section>'''


def page_head(eyebrow, title, lede, crumb):
    return f'''
<section class="page-head">
  <div class="container">
    <nav class="crumbs" aria-label="{L("Breadcrumb", "导航路径")}"><a href="index.html">{L("Home", "首页")}</a><span aria-hidden="true">/</span><span aria-current="page">{crumb}</span></nav>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>'''


def contact_card(compact=False):
    return f'''
<div class="contact-card{" compact" if compact else ""}">
  <p class="contact-card-title">{L("Speak to a solicitor", "与律师联系")}</p>
  <ul class="channels">
    <li><a href="{TEL_HREF}">{icon("phone")}<span><strong>{TEL}</strong><small>{L("Office", "办公室电话")}</small></span></a></li>
    <li><a href="{WA}" target="_blank" rel="noopener">{icon("chat")}<span><strong>{WA_TEL}</strong><small>WhatsApp</small></span></a></li>
    <li><button type="button" class="copy" data-copy="{WECHAT}" data-done="{L("Copied", "已复制")}">{icon("wechat")}<span><strong>{WECHAT}</strong><small>{L("WeChat ID · tap to copy", "微信号 · 点击复制")}</small></span>{icon("copy", "ic ic-end")}</button></li>
    <li><a href="mailto:{EMAIL}">{icon("mail")}<span><strong>{EMAIL}</strong><small>{L("Email", "电子邮件")}</small></span></a></li>
  </ul>
  <p class="hours">{icon("clock")}<span>{L("Mon–Fri, 9:30am–6:30pm", "周一至周五 9:30–18:30（伦敦时间）")} · <span class="open-status" data-open="{L("Open now", "现在营业")}" data-closed="{L("Closed now", "现在休息")}"></span></span></p>
</div>'''


# ===================================================================== Home

def home():
    cards = "\n".join(f'''
      <a class="area-card reveal" href="services.html#{a["id"]}">
        <span class="area-icon">{icon(a["icon"])}</span>
        <h3>{a["name"]}</h3>
        <p>{a["short"]}</p>
        <span class="more">{L("Learn more", "了解更多")} {icon("arrow")}</span>
      </a>''' for a in areas())
    fees = "\n".join(f'<li><span>{n}</span><strong>{p}</strong></li>' for n, p in popular_fees())

    body = f'''
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">{L("Solicitors in London · 伦敦华人律师", "伦敦律师事务所 · Solicitors in London")}</p>
      <h1>{L("UK legal advice in <em>your</em> language.", "用<em>您的语言</em>，<br>解答英国法律问题。")}</h1>
      <p class="lede">{L("Immigration, property, family and business law for individuals and families, explained clearly in Mandarin, Cantonese or English. Fixed fees agreed before we start.",
                         "移民、物业、家事及商业法律服务，以普通话、粤语或英语清楚解释。开始工作前先确定固定收费。")}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="contact.html#enquiry">{L("Book a free consultation", "预约免费咨询")} {icon("arrow")}</a>
        <a class="btn btn-outline" href="fees.html">{L("See our fixed fees", "查看收费标准")}</a>
      </div>
      <ul class="langs" aria-label="{L("Languages we speak", "服务语言")}">
        <li><span lang="zh-Hans">普通话</span><small>Mandarin</small></li>
        <li><span lang="zh-Hant">粵語</span><small>Cantonese</small></li>
        <li><span lang="en">English</span><small>{L("English", "英语")}</small></li>
      </ul>
    </div>
    {contact_card()}
  </div>
</section>

<section class="trust">
  <div class="container trust-grid">
    <div>{icon("shield")}<p><strong>{L("Regulated by the SRA", "受 SRA 监管")}</strong><span>{L("Authorised solicitors in England &amp; Wales", "英格兰及威尔士执业律师")}</span></p></div>
    <div>{icon("chat")}<p><strong>{L("Free first consultation", "首次咨询免费")}</strong><span>{L("Understand your options before you commit", "先了解方案，再决定是否委托")}</span></p></div>
    <div>{icon("check")}<p><strong>{L("Fixed fees", "固定收费")}</strong><span>{L("Agreed in writing before work begins", "开始工作前书面确认")}</span></p></div>
    <div>{icon("clock")}<p><strong>{L("Reply in one working day", "一个工作日内回复")}</strong><span>{L("Same or next working day", "当天或下一个工作日")}</span></p></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{L("Practice areas", "业务范围")}</p>
      <h2>{L("What do you need help with?", "您需要哪方面的帮助？")}</h2>
    </div>
    <div class="area-grid">{cards}
      <a class="area-card area-card-cta reveal" href="contact.html#enquiry">
        <h3>{L("Something else?", "其他问题？")}</h3>
        <p>{L("Wills, probate or a matter not listed here. Ask us and we will tell you honestly whether we can help.", "遗嘱、遗产或其他未列出的事务，欢迎询问，我们会坦诚告诉您能否协助。")}</p>
        <span class="more">{L("Ask us", "联系我们")} {icon("arrow")}</span>
      </a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{L("How it works", "服务流程")}</p>
      <h2>{L("Clear steps, and a price you know up front", "流程清晰，费用事先说明")}</h2>
      <ol class="steps">
        <li><span class="step-n">1</span><div><h3>{L("Free consultation", "免费咨询")}</h3><p>{L("Call, WhatsApp, WeChat or email us. A solicitor looks at your situation and explains your options in your language.", "通过电话、WhatsApp、微信或电邮联系我们。律师会了解您的情况，并以您熟悉的语言解释可行方案。")}</p></div></li>
        <li><span class="step-n">2</span><div><h3>{L("Fixed-fee quote", "固定收费报价")}</h3><p>{L("We confirm the fee and what it covers in writing. If your case is complex, we tell you before you instruct us, not after.", "我们以书面形式确认收费及服务范围。如案件较复杂，会在您委托前说明，而不是事后加价。")}</p></div></li>
        <li><span class="step-n">3</span><div><h3>{L("We handle it", "由我们跟进处理")}</h3><p>{L("We prepare the documents, deal with the Home Office, court or other side, and keep you updated until it is done.", "我们准备文件，与移民局、法院或对方沟通，并全程向您汇报进度，直到完成。")}</p></div></li>
      </ol>
    </div>
    <aside class="fee-teaser reveal">
      <p class="eyebrow">{L("Fixed fees", "固定收费")}</p>
      <h3>{L("Popular services", "常见服务收费")}</h3>
      <ul class="fee-list">{fees}</ul>
      <p class="fine">{L("Indicative legal fees. Home Office, Land Registry and other third-party fees are extra.", "以上为参考律师费，移民局、土地注册处等第三方费用另计。")}</p>
      <a class="btn btn-outline btn-block" href="fees.html">{L("See all fees", "查看全部收费")} {icon("arrow")}</a>
    </aside>
  </div>
</section>

<section class="section">
  <div class="container split split-even">
    <div class="reveal">
      <p class="eyebrow">{L("About the firm", "关于盛伦")}</p>
      <h2>{L("A London firm built for Chinese-speaking clients", "专为华人客户服务的伦敦律所")}</h2>
      <p>{L("Chapel Law Solicitors (盛倫) is a private law firm in London, authorised and regulated by the Solicitors Regulation Authority.",
             "盛伦律师事务所（Chapel Law Solicitors）是一家位于伦敦的私人律师事务所，受英国律师监管局（SRA）授权及监管。")}</p>
      <p>{L("Whether you are studying, working, running a business or settling in the UK, we explain British law in Chinese or English and give advice built around your situation.",
             "无论您在英国求学、工作、经商还是准备定居，我们都会用中文或英文为您解释英国法律，并根据您的实际情况提供建议。")}</p>
      <a class="text-link" href="about.html">{L("About us and our team", "了解我们的团队")} {icon("arrow")}</a>
    </div>
    <figure class="quote reveal">
      <svg class="quote-mark" viewBox="0 0 40 32" aria-hidden="true"><path fill="currentColor" d="M0 32V19C0 8.5 5.3 2.2 15.8 0l1.7 3.6C12 5.2 9.2 8.6 8.9 13.7H16V32H0zm23.4 0V19c0-10.5 5.3-16.8 15.9-19L41 3.6c-5.5 1.6-8.3 5-8.6 10.1h7.1V32H23.4z"/></svg>
      <blockquote><p>{L("I had superb service from the solicitors on the visa application for my cousin. I would like to say a huge thank you to Chapel Law Solicitors for the clear guidance and fast handling for the application.",
                          "律师在我表弟的签证申请上提供了一流的服务。非常感谢盛伦律师事务所清晰的指导和快速的处理。")}</p></blockquote>
      <figcaption>Garcia · {L("visa application client", "签证申请客户")}</figcaption>
    </figure>
  </div>
</section>
{cta_band()}
'''
    page("index.html", key="home",
         title=L("Chapel Law Solicitors | Bilingual solicitors in London", "盛伦律师事务所 | 伦敦华人律师 · 普通话 粤语"),
         description=L("London solicitors for immigration, property, family and business law, in Mandarin, Cantonese and English. Free first consultation and fixed fees.",
                       "伦敦华人律师事务所，提供移民、物业、家事及商业法律服务，普通话、粤语及英语。首次咨询免费，固定收费。"),
         body=body)


# ===================================================================== Practice areas

def services():
    all_areas = areas()
    toc = "".join(f'<a href="#{a["id"]}">{icon(a["icon"])}<span>{a["name"]}</span></a>' for a in all_areas)
    blocks = []
    for a in all_areas:
        items = "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in a["items"])
        fee_link = (f'<a class="text-link" href="{a["fees"]}">{L("See fixed fees", "查看收费")} {icon("arrow")}</a>'
                    if a["fees"] else
                    f'<p class="fine">{L("Fees depend on the case. We give you a written quote after your free consultation.", "收费视乎案件而定，免费咨询后我们会提供书面报价。")}</p>')
        blocks.append(f'''
    <article class="area-block reveal" id="{a["id"]}">
      <div class="area-block-head">
        <span class="area-icon">{icon(a["icon"])}</span>
        <h2>{a["name"]}</h2>
      </div>
      <div class="area-block-body">
        <p>{a["intro"]}</p>
        <h3 class="list-h">{L("We can help with", "服务内容")}</h3>
        <ul class="check-list">{items}</ul>
        <div class="area-block-foot">
          {fee_link}
          <a class="btn btn-primary btn-sm" href="contact.html?area={a["id"]}#enquiry">{L("Ask about this", "就此咨询")}</a>
        </div>
      </div>
    </article>''')

    body = page_head(L("Practice areas", "业务范围"),
                     L("How we can help", "我们可以如何协助您"),
                     L("Seven areas of law, each handled by solicitors who can explain it to you in Mandarin, Cantonese or English.",
                       "七大法律领域，均由能以普通话、粤语或英语与您沟通的律师处理。"),
                     L("Practice areas", "业务范围")) + f'''
<section class="section section-tight">
  <div class="container with-rail">
    <nav class="rail" aria-label="{L("Practice areas", "业务范围")}"><div class="rail-inner">{toc}</div></nav>
    <div class="area-blocks">{"".join(blocks)}
    </div>
  </div>
</section>
{cta_band()}
'''
    page("services.html", key="services",
         title=L("Practice areas | Chapel Law Solicitors", "业务范围 | 盛伦律师事务所"),
         description=L("UK immigration, residential and commercial property, family, business, personal injury and criminal law, in Mandarin, Cantonese and English.",
                       "英国移民、住宅及商业物业、家事、商业、人身伤害及刑事法律服务，提供普通话、粤语及英语。"),
         body=body)


# ===================================================================== Fees

def fees_page():
    chips = "".join(f'<a href="#{g["id"]}">{L(g["en"], g["zh"])}</a>' for g in GROUPS)
    tables = []
    for g in GROUPS:
        rows = "".join(
            f'<tr><th scope="row">{L(en, zh)}</th><td>{L(pen, pzh)}</td></tr>'
            for en, zh, pen, pzh in g["rows"])
        note = f'<p class="fine">{L(g["note_en"], g["note_zh"])}</p>' if g.get("note_en") else ""
        tables.append(f'''
      <section class="fee-group" id="{g["id"]}" data-fee-group>
        <h2>{L(g["en"], g["zh"])}</h2>
        {note}
        <table class="fee-table">
          <thead><tr><th scope="col">{L("Service", "服务")}</th><th scope="col">{L("Our fee", "律师费")}</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </section>''')

    body = page_head(L("Fixed fees", "收费标准"),
                     L("Our fixed fees", "固定收费标准"),
                     L("Your first consultation is free. After that, most work is done for a fixed fee, agreed in writing before we start.",
                       "首次咨询免费。之后大部分服务均采用固定收费，并在开始工作前以书面确认。"),
                     L("Fixed fees", "收费标准")) + f'''
<section class="section section-tight">
  <div class="container">
    <div class="fee-notes">
      <div>{icon("check")}<p><strong>{L("What is included", "收费包括")}</strong>{L("Our legal work on the application or transaction from start to finish.", "由开始到完成，与申请或交易相关的律师工作。")}</p></div>
      <div>{icon("search")}<p><strong>{L("What is not included", "收费不包括")}</strong>{L("Home Office application fees, the Immigration Health Surcharge, Land Registry fees and other third-party costs.", "移民局申请费、移民医疗附加费（IHS）、土地注册处费用及其他第三方费用。")}</p></div>
      <div>{icon("shield")}<p><strong>{L("Complex cases", "复杂个案")}</strong>{L("These are typical fees. If your case needs more work, we quote a higher fixed fee and tell you before you instruct us.", "以上为一般收费。如个案需要更多工作，我们会在您委托前提供较高的固定报价并事先说明。")}</p></div>
    </div>

    <div class="fee-tools">
      <label class="fee-search">{icon("search")}<span class="sr-only">{L("Search fees", "搜索收费项目")}</span>
        <input type="search" id="fee-search" placeholder="{L("Search, e.g. spouse, ILR, lease", "搜索，例如：配偶、永居、租约")}" autocomplete="off"></label>
      <nav class="chips" aria-label="{L("Fee categories", "收费类别")}">{chips}</nav>
    </div>
    <p class="fee-empty" id="fee-empty" hidden>{L("Nothing matches that search. Call us on 020 3161 7187 and we will give you a quote.", "找不到相关项目。请致电 020 3161 7187，我们会为您报价。")}</p>

    <div class="fee-groups">{"".join(tables)}
    </div>
  </div>
</section>
{cta_band()}
'''
    page("fees.html", key="fees",
         title=L("Fixed fees | Chapel Law Solicitors", "收费标准 | 盛伦律师事务所"),
         description=L("Fixed legal fees for UK visas, settlement, citizenship, appeals and conveyancing. Free first consultation.",
                       "英国签证、永居、入籍、上诉及物业买卖的固定律师费。首次咨询免费。"),
         body=body)


# ===================================================================== About

def about():
    team = [
        ("DL", "Danny Liang", L("Director", "董事")),
        ("D", "David", L("Senior Solicitor", "高级律师")),
        ("AH", "Andrew Hill", L("Barrister", "大律师")),
        ("DY", "Dylan Yeap", L("Senior Paralegal", "高级律师助理")),
    ]
    people = "".join(f'<li class="person reveal"><span class="avatar" aria-hidden="true">{i}</span><p><strong>{n}</strong><span>{r}</span></p></li>'
                     for i, n, r in team)
    body = page_head(L("About us", "关于我们"),
                     L("Bilingual solicitors in London", "伦敦双语律师事务所"),
                     L("We help Chinese-speaking clients who are studying, working, investing or settling in the UK to understand British law and act with confidence.",
                       "我们协助在英国求学、工作、投资或定居的华人客户了解英国法律，安心作出决定。"),
                     L("About us", "关于我们")) + f'''
<section class="section section-tight">
  <div class="container split split-even">
    <div class="prose reveal">
      <h2>{L("Who we are", "我们是谁")}</h2>
      <p>{L("Chapel Law Solicitors Limited (盛倫律師事務所) is a private law firm in London, licensed to practise law in England and Wales and regulated by the Solicitors Regulation Authority.",
             "盛伦律师事务所（Chapel Law Solicitors Limited）是一家位于伦敦的私人律师事务所，具备英格兰及威尔士执业资格，受英国律师监管局（SRA）监管。")}</p>
      <p>{L("We are one of a small number of London firms offering a full legal service in both Chinese and English. Our solicitors work in Mandarin, Cantonese and English, so nothing gets lost in translation.",
             "我们是伦敦少数能以中英文提供全面法律服务的律所之一。我们的律师能以普通话、粤语及英语工作，沟通不再有隔阂。")}</p>
      <h2>{L("How we work", "我们的工作方式")}</h2>
      <p>{L("We start from your situation, not a template. Every piece of advice is tailored to what you need, and we explain it plainly so you can make your own decisions.",
             "我们从您的实际情况出发，而不是套用模板。每项建议都按您的需要度身订造，并以浅白的方式解释，让您能自己作出决定。")}</p>
      <p>{L("We aim to reply the same or next working day, and we want long-term relationships: many clients come back to us as their life in the UK moves from a visa to a home, a business and citizenship.",
             "我们力求在当天或下一个工作日回复，并重视长期关系：不少客户从签证、置业、创业到入籍，一路都由我们协助。")}</p>
    </div>
    <aside class="facts reveal">
      <dl>
        <div><dt>{L("Languages", "服务语言")}</dt><dd>{L("Mandarin · Cantonese · English", "普通话 · 粤语 · 英语")}</dd></div>
        <div><dt>{L("Regulated by", "监管机构")}</dt><dd>{L("Solicitors Regulation Authority", "英国律师监管局（SRA）")}</dd></div>
        <div><dt>{L("Office", "办公地址")}</dt><dd>{ADDRESS}</dd></div>
        <div><dt>{L("Opening hours", "办公时间")}</dt><dd>{L("Mon–Fri, 9:30am–6:30pm", "周一至周五 9:30–18:30")}</dd></div>
        <div><dt>{L("First consultation", "首次咨询")}</dt><dd>{L("Free", "免费")}</dd></div>
      </dl>
    </aside>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{L("Our team", "我们的团队")}</p>
      <h2>{L("The people you will work with", "为您服务的团队")}</h2>
    </div>
    <ul class="people">{people}</ul>
    <p class="fine center">{L("Looking to join us? See <a href=\"careers.html\">careers</a>.", "有意加入我们？请查看<a href=\"careers.html\">招聘信息</a>。")}</p>
  </div>
</section>
{cta_band()}
'''
    page("about.html", key="about",
         title=L("About us | Chapel Law Solicitors", "关于我们 | 盛伦律师事务所"),
         description=L("Chapel Law Solicitors is an SRA-regulated London law firm working in Mandarin, Cantonese and English.",
                       "盛伦律师事务所是受 SRA 监管的伦敦律所，提供普通话、粤语及英语法律服务。"),
         body=body)


# ===================================================================== Contact

def contact():
    options = "".join(f'<option value="{a["id"]}">{a["name"]}</option>' for a in areas())
    body = page_head(L("Contact", "联系我们"),
                     L("Talk to us", "与我们联系"),
                     L("Your first consultation is free. Call, message or send the form below and we will reply the same or next working day.",
                       "首次咨询免费。欢迎致电、发消息或填写下方表格，我们会在当天或下一个工作日回复。"),
                     L("Contact", "联系我们")) + f'''
<section class="section section-tight">
  <div class="container contact-grid">
    <div class="enquiry reveal" id="enquiry">
      <h2>{L("Send an enquiry", "在线咨询")}</h2>
      <p class="fine">{L("Fill this in and your email app will open with the message ready to send. Please keep it brief; we will ask for documents later.", "填写后会打开您的电邮程序，信息已预先填好。请简述情况即可，文件稍后再提供。")}</p>
      <form class="form" id="enquiry-form" data-to="{EMAIL}" data-subject="{L("Enquiry from website", "网站咨询")}" novalidate>
        <div class="field-row">
          <label class="field"><span>{L("Name", "姓名")}</span><input name="name" autocomplete="name" required></label>
          <label class="field"><span>{L("Phone", "电话")}</span><input name="phone" type="tel" autocomplete="tel"></label>
        </div>
        <label class="field"><span>{L("Email", "电子邮件")}</span><input name="email" type="email" autocomplete="email" required></label>
        <div class="field-row">
          <label class="field"><span>{L("I need help with", "咨询事项")}</span>
            <select name="area"><option value="">{L("Choose one", "请选择")}</option>{options}<option value="other">{L("Something else", "其他")}</option></select></label>
          <fieldset class="field">
            <legend>{L("Preferred language", "希望使用的语言")}</legend>
            <div class="seg">
              <label><input type="radio" name="lang" value="普通话 Mandarin"{" checked" if L(0, 1) else ""}><span>普通话</span></label>
              <label><input type="radio" name="lang" value="粵語 Cantonese"><span>粵語</span></label>
              <label><input type="radio" name="lang" value="English"{" checked" if L(1, 0) else ""}><span>English</span></label>
            </div>
          </fieldset>
        </div>
        <label class="field"><span>{L("How can we help?", "请简述您的情况")}</span><textarea name="message" rows="5" required></textarea></label>
        <p class="form-error" hidden>{L("Please add your name, email and a short message.", "请填写姓名、电邮及简要说明。")}</p>
        <button class="btn btn-primary" type="submit">{L("Send enquiry", "发送咨询")} {icon("arrow")}</button>
        <p class="fine">{L("Please do not send confidential documents until we have confirmed we can act for you.", "在我们确认可以接受委托之前，请勿发送机密文件。")}</p>
      </form>
    </div>
    <div class="contact-side">
      {contact_card(compact=True)}
      <div class="visit reveal">
        <h2 class="h-sm">{L("Visit us", "到访地址")}</h2>
        <p>{icon("pin")}<span>{ADDRESS}</span></p>
        <p class="fine">{L("Meetings are by appointment. Please call or message before you visit.", "到访需预约，请先致电或发消息。")}</p>
        <a class="text-link" href="{MAPS}" target="_blank" rel="noopener">{L("Open in Google Maps", "在 Google 地图中打开")} {icon("ext")}</a>
      </div>
    </div>
  </div>
</section>
'''
    page("contact.html", key="contact",
         title=L("Contact | Chapel Law Solicitors", "联系我们 | 盛伦律师事务所"),
         description=L("Call 020 3161 7187, WhatsApp, WeChat or email Chapel Law Solicitors. Free first consultation in Mandarin, Cantonese or English.",
                       "致电 020 3161 7187、WhatsApp、微信或电邮联系盛伦律师事务所。首次咨询免费，提供普通话、粤语及英语服务。"),
         body=body)


# ===================================================================== Complaints

def complaints():
    steps = [
        (L("Within 1 day", "1 天内"), L("We record your complaint in our central register and open a file.", "我们将您的投诉记录在中央登记册并开立档案。")),
        (L("Within 3 working days", "3 个工作日内"), L("We acknowledge your complaint in writing, ask you to confirm the details, and tell you who is dealing with it.", "我们以书面确认收到投诉，请您确认细节，并告知负责处理的人员。")),
        (L("Within 14 days", "14 天内"), L("We investigate. This may include asking the person who acted for you to respond, and inviting you to a meeting. If a meeting is not possible, we send you a detailed reply with our suggestions for resolving the matter.", "我们展开调查，可能包括请负责您案件的同事回应，并邀请您会面。如无法会面，我们会寄出详细回复及解决建议。")),
        (L("If you are still unhappy", "如您仍不满意"), L("Tell us and we will review our decision. Depending on the case, this is done by someone in the firm who was not involved, by our complaints partner, by another firm or the local Law Society, or through independent mediation. Most reviews take up to 14 days.", "请告诉我们，我们会复核决定。视乎情况，复核会由未参与案件的同事、投诉合伙人、其他律所或当地律师会负责，或通过独立调解进行。大部分复核在 14 天内完成。")),
        (L("Within 5 days of the review", "复核后 5 天内"), L("We write to you with our final position and the reasons for it.", "我们以书面形式告知最终决定及理由。")),
    ]
    tl = "".join(f'<li><p class="when">{w}</p><p>{t}</p></li>' for w, t in steps)
    body = page_head(L("Complaints", "投诉"),
                     L("Our complaints procedure", "投诉程序"),
                     L("We want to hear if something has gone wrong. Here is how to raise a complaint and what happens next.",
                       "如果我们的服务未达您的期望，请告诉我们。以下是投诉方式及后续处理流程。"),
                     L("Complaints", "投诉")) + f'''
<section class="section section-tight">
  <div class="container narrow prose">
    <p>{L("We are committed to a high-quality legal service. We also recognise that mistakes can happen. If they do, we will work with you to put things right quickly and fairly, and use what we learn to improve.",
           "我们致力提供高质素的法律服务，但也明白错误有时难免。一旦发生，我们会与您合作，迅速而公平地解决问题，并从中改进。")}</p>
    <p>{L("The solicitor handling your case should be able to answer most concerns straight away. If not, please use this procedure.",
           "大部分疑问可由负责您案件的律师直接解答。如未能解决，请按以下程序投诉。")}</p>

    <div class="callout">
      <h2 class="h-sm">{L("How to complain", "如何投诉")}</h2>
      <p>{L("Write to our Director, Ms Danny Liang:", "请致函本所董事 Danny Liang 女士：")}</p>
      <ul class="plain">
        <li>{icon("mail")}<a href="mailto:{EMAIL}?subject={L("Complaint", "投诉")}">{EMAIL}</a></li>
        <li>{icon("pin")}<span>{ADDRESS}</span></li>
      </ul>
      <p class="fine">{L("If you would rather not write a detailed letter or email, we will arrange a phone call so you can tell us about it.", "如果您不方便撰写详细信件或电邮，我们可以安排电话，让您口头说明。")}</p>
    </div>

    <h2>{L("What happens next", "后续处理")}</h2>
    <p class="fine">{L("These are our target timescales. If we need to change them, we will tell you and explain why.", "以下为目标处理时间。如需更改，我们会通知您并说明原因。")}</p>
    <ol class="timeline">{tl}</ol>
    <p>{L("Our Client Services Manager may contact you within 7 days to check you are satisfied with our response. Your feedback is used in training for our lawyers and staff.",
           "客户服务经理可能会在 7 天内联系您，确认您是否满意我们的回复。您的意见将用于律师及员工培训。")}</p>

    <h2>{L("The Legal Ombudsman", "法律申诉专员（Legal Ombudsman）")}</h2>
    <p>{L("If we cannot resolve your complaint, the Legal Ombudsman may be able to help. They look at complaints independently, and using them will not affect how we handle your case.",
           "如我们未能解决您的投诉，法律申诉专员或可协助。他们会独立审视投诉，而向其投诉不会影响我们处理您的案件。")}</p>
    <ul>
      <li>{L("You normally need to have complained to us first.", "一般须先向本所投诉。")}</li>
      <li>{L("You must contact the Ombudsman within <strong>six months</strong> of our final response.", "须在收到本所最终回复后<strong>六个月内</strong>向申诉专员投诉。")}</li>
      <li>{L("And within <strong>one year</strong> of the problem happening, or of you becoming aware of it.", "并须在问题发生或您知悉问题后<strong>一年内</strong>提出。")}</li>
      <li>{L("Most individual clients can use the scheme; there are restrictions for some larger businesses.", "大部分个人客户均可使用此机制，部分大型企业则有限制。")}</li>
    </ul>
    <div class="callout callout-plain">
      <p><strong>Legal Ombudsman</strong><br>PO Box 6167, Slough SL1 0EH<br>
      {L("Phone", "电话")}: <a href="tel:03005550333">0300 555 0333</a> ({L("9am–5pm", "9:00–17:00")})<br>
      {L("Email", "电邮")}: <a href="mailto:enquiries@legalombudsman.org.uk">enquiries@legalombudsman.org.uk</a><br>
      <a href="https://www.legalombudsman.org.uk/" target="_blank" rel="noopener">www.legalombudsman.org.uk</a></p>
    </div>

    <h2>{L("Concerns about our behaviour", "对我们操守的关注")}</h2>
    <p>{L("The Solicitors Regulation Authority can help if you are concerned about our behaviour, for example dishonesty, taking or losing your money, or treating you unfairly because of your age, a disability or another characteristic.",
           "如您对我们的操守有疑虑，例如不诚实、挪用或遗失您的款项，或因年龄、残疾或其他特征而受到不公平对待，可向英国律师监管局（SRA）反映。")}</p>
    <p><a class="text-link" href="https://www.sra.org.uk/consumers/problems/report-solicitor/" target="_blank" rel="noopener">{L("Raise a concern with the SRA", "向 SRA 反映")} {icon("ext")}</a></p>
  </div>
</section>
'''
    page("complaints.html", key="complaints",
         title=L("Complaints procedure | Chapel Law Solicitors", "投诉程序 | 盛伦律师事务所"),
         description=L("How to make a complaint to Chapel Law Solicitors, our timescales, and how to contact the Legal Ombudsman or the SRA.",
                       "如何向盛伦律师事务所投诉、处理时间，以及如何联系法律申诉专员或 SRA。"),
         body=body)


# ===================================================================== Careers

def careers():
    body = page_head(L("Careers", "招聘"),
                     L("Join our team", "加入我们"),
                     L("We are a forward-thinking firm that values its people. If you put clients and colleagues first, we would like to hear from you.",
                       "我们是一家重视员工、积极进取的律所。如果您以客户和同事为先，欢迎与我们联系。"),
                     L("Careers", "招聘")) + f'''
<section class="section section-tight">
  <div class="container split split-even">
    <div class="prose reveal">
      <h2>{L("Working here", "在盛伦工作")}</h2>
      <p>{L("We want everyone at the firm to feel valued and rewarded. Career development matters to us: we keep the atmosphere relaxed and friendly, and give every team member the chance to learn, develop and lead.",
             "我们希望每位同事都感到受重视、获得回报。我们重视职业发展，营造轻松友善的工作环境，让每位成员都有学习、成长和带领团队的机会。")}</p>
      <p>{L("Speaking Mandarin or Cantonese is a real advantage, as most of our clients are Chinese-speaking.",
             "由于大部分客户使用中文，能说普通话或粤语将是一大优势。")}</p>
    </div>
    <aside class="facts reveal">
      <h2 class="h-sm">{L("Open roles", "现有职位")}</h2>
      <ul class="roles">
        <li><strong>{L("Legal Assistant / Paralegal", "法律助理 / 律师助理")}</strong></li>
        <li><strong>{L("Solicitors", "律师")}</strong></li>
      </ul>
      <p>{L("Email your CV and a cover letter to", "请将简历及求职信发送至")}</p>
      <a class="btn btn-primary btn-block" href="mailto:{EMAIL}?subject={L("Job application", "求职申请")}">{icon("mail")} {EMAIL}</a>
    </aside>
  </div>
</section>
'''
    page("careers.html", key="careers",
         title=L("Careers | Chapel Law Solicitors", "招聘 | 盛伦律师事务所"),
         description=L("Join Chapel Law Solicitors. We are recruiting legal assistants, paralegals and solicitors.",
                       "加入盛伦律师事务所。现招聘法律助理、律师助理及律师。"),
         body=body)


def build():
    for lang in LANGS:
        set_lang(lang)
        home()
        services()
        fees_page()
        about()
        contact()
        complaints()
        careers()
    missing = sorted(set(layout.MISSING))
    if missing:
        sys.exit("Missing Arabic text in _build/ar.py for:\n  " + "\n  ".join(missing))
    print("Built", len(LANGS) * 7, "pages")


if __name__ == "__main__":
    build()

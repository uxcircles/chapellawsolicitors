# Fee schedule, transcribed from the "Price List" image on the current /our-fees/ page.
# Route names are updated to the current Home Office names where there is a direct successor;
# the old name stays in brackets so existing clients still recognise it.
# Each row: (English name, Chinese name, price EN, price ZH)

UPFRONT_EN = "£1,800 (£500 upfront, £1,100 on grant)"
UPFRONT_ZH = "£1,800（预付 £500，获批后付 £1,100）"
RANGE_VISIT = ("£800–£1,000", "£800–£1,000")

GROUPS = [
    {
        "id": "family",
        "en": "Family visas", "zh": "家庭签证",
        "rows": [
            ("Spouse, unmarried partner or civil partner visa", "配偶、未婚伴侣及民事伴侣签证", "£1,300", "£1,300"),
            ("Child dependant visa", "子女受养人签证", "£1,250", "£1,250"),
            ("Family reunion", "家庭团聚签证", "£1,250", "£1,250"),
            ("Other family dependant visa", "其他家庭受养人签证", "£1,250", "£1,250"),
        ],
    },
    {
        "id": "work",
        "en": "Work & sponsorship", "zh": "工作签证及担保",
        "rows": [
            ("Skilled Worker visa (formerly Tier 2)", "技术工人签证（原 Tier 2）", "£1,250", "£1,250"),
            ("Skilled Worker extension and settlement", "技术工人签证续签及定居", "£1,200", "£1,200"),
            ("Skilled Worker indefinite leave to remain", "技术工人路线永居（ILR）", "£1,200", "£1,200"),
            ("Sponsor licence application", "雇主担保执照申请", "£2,000", "£2,000"),
            ("Sponsor advertising and contract", "担保职位招聘广告及合同", "£500", "£500"),
            ("Temporary Work visa (formerly Tier 5)", "临时工作签证（原 Tier 5）", "£1,200", "£1,200"),
        ],
    },
    {
        "id": "investment",
        "en": "Talent, investment & entrepreneur", "zh": "人才、投资及创业签证",
        "note_en": "Some of these routes are closed to new applicants. Fees for the old Tier 1 routes apply to extensions and settlement for people already on them. Ask us which route fits you now.",
        "note_zh": "部分签证类别已停止接受新申请。原 Tier 1 类别的收费适用于已持有该签证人士的续签及定居申请。欢迎咨询目前适合您的签证类别。",
        "rows": [
            ("Global Talent visa", "全球人才签证", "£2,000–£5,000", "£2,000–£5,000"),
            ("Innovator visa", "创新者签证", "£2,000–£5,000", "£2,000–£5,000"),
            ("Start-up visa", "初创签证", "£2,000–£5,000", "£2,000–£5,000"),
            ("Tier 1 (Investor) visa", "Tier 1 投资者签证", "£5,000–£7,000", "£5,000–£7,000"),
            ("Tier 1 Investor extension", "Tier 1 投资者签证续签", "£4,300", "£4,300"),
            ("Tier 1 Investor settlement", "Tier 1 投资者签证定居", "£4,400", "£4,400"),
            ("Tier 1 Entrepreneur extension", "Tier 1 企业家签证续签", "£3,000", "£3,000"),
            ("Tier 1 Entrepreneur settlement", "Tier 1 企业家签证定居", "On request", "请咨询"),
            ("Tier 1 Exceptional Talent", "Tier 1 杰出人才签证", "£4,500", "£4,500"),
        ],
    },
    {
        "id": "study",
        "en": "Study", "zh": "学生签证",
        "rows": [
            ("Student visa (formerly Tier 4), adult", "学生签证（原 Tier 4）— 成人", "£1,050", "£1,050"),
            ("Child Student visa", "儿童学生签证", "£1,000", "£1,000"),
            ("Student visa extension", "学生签证续签", "£1,000", "£1,000"),
        ],
    },
    {
        "id": "visit",
        "en": "Visit", "zh": "访问签证",
        "rows": [
            ("Standard Visitor visa", "标准访问签证", *RANGE_VISIT),
            ("Business visitor", "商务访问", *RANGE_VISIT),
            ("Student visitor", "短期学习访问", *RANGE_VISIT),
            ("Child visitor", "儿童访问", *RANGE_VISIT),
            ("Visitor in transit", "过境签证", *RANGE_VISIT),
        ],
    },
    {
        "id": "settlement",
        "en": "Settlement & citizenship", "zh": "永居及入籍",
        "rows": [
            ("Indefinite leave to remain (ILR)", "永久居留（ILR）", "£1,000", "£1,000"),
            ("British citizenship (registration)", "英国国籍登记", "£1,050", "£1,050"),
            ("British naturalisation", "英国入籍", "£1,050", "£1,050"),
            ("EU Settlement Scheme: pre-settled and settled status", "欧盟定居计划：预定居及定居身份", "£800", "£800"),
        ],
    },
    {
        "id": "human-rights",
        "en": "Human rights & long residence", "zh": "人权及长期居留申请",
        "rows": [
            ("Fresh asylum claim", "新庇护申请", "£1,300", "£1,300"),
            ("Children: 7-year rule", "儿童七年规则申请", "£1,500", "£1,500"),
            ("20 years' unlawful residence", "非法居留满 20 年申请", UPFRONT_EN, UPFRONT_ZH),
            ("Irregular status application", "非法身份申请", UPFRONT_EN, UPFRONT_ZH),
            ("Other applications outside the Immigration Rules", "其他移民条例以外的申请", "£1,500–£1,800", "£1,500–£1,800"),
        ],
    },
    {
        "id": "appeals",
        "en": "Appeals, reviews & enforcement", "zh": "上诉、复审及执法事宜",
        "rows": [
            ("Appeals", "上诉", "£1,350", "£1,350"),
            ("Administrative review", "行政复审", "£600–£800", "£600–£800"),
            ("Judicial review", "司法复核", "£2,600", "£2,600"),
            ("Immigration bail application", "移民保释申请", "£1,500", "£1,500"),
            ("Civil penalties (illegal working)", "非法用工民事罚款", "£1,500", "£1,500"),
        ],
    },
    {
        "id": "residential",
        "en": "Residential conveyancing", "zh": "住宅物业买卖",
        "note_en": "Land Registry fees, searches and other disbursements are extra. We confirm them when you instruct us.",
        "note_zh": "土地注册处费用、查册费及其他代垫费用另计，我们会在您正式委托时列明。",
        "rows": [
            ("Freehold", "永久产权（Freehold）", "£1,400", "£1,400"),
            ("Leasehold", "租赁产权（Leasehold）", "£1,600", "£1,600"),
        ],
    },
    {
        "id": "commercial",
        "en": "Commercial conveyancing", "zh": "商业物业",
        "note_en": "Land Registry fees and other disbursements are extra. We confirm them when you instruct us.",
        "note_zh": "土地注册处费用及其他代垫费用另计，我们会在您正式委托时列明。",
        "rows": [
            ("New lease, assignment or subletting", "新租约、租约转让或转租", "£1,000", "£1,000"),
            ("Lease renewal", "租约续期", "£750", "£750"),
            ("Freehold, or lease over 25 years", "永久产权或 25 年以上租约", "£1,495", "£1,495"),
        ],
    },
]

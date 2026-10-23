# chapellawsolicitors.co.uk — 盛倫律師事務所 改版提案

[Chapel Law Solicitors（盛倫）](https://chapellawsolicitors.co.uk/) 的網站改版：倫敦的華人律師事務所，業務以英國移民為主，另有住宅/商業物業、家事、商業、人身傷害及刑事法。純靜態 HTML / CSS / JS，任何靜態主機都能直接部署。

> **概念設計展示**：這是由 [UX CIRCLES](https://ux-circles.com/web) 設計的改版提案，並非 Chapel Law Solicitors 官方網站。
> 每頁頂端有「Concept」標示列，所有頁面都設為 `noindex`，`robots.txt` 也禁止搜尋引擎收錄，避免和官方網站搶搜尋結果。
> 如果律所正式採用：刪掉 `_build/layout.py` 裡的 `.concept-bar` 和 `<meta name="robots" content="noindex, nofollow">`，重新建置，並把 `robots.txt` 改回 `Allow: /`。

## 語言

| 路徑 | 版本 |
|---|---|
| `/` | English（預設，和原網站一致） |
| `/zh/` | 简体中文（原網站的中文版也是簡體） |

原網站另有阿拉伯文版（機器翻譯），這次沒有做。

## 頁面

| 頁面 | 內容 |
|---|---|
| `index.html` | 首頁：雙語主視覺、聯絡卡（電話 / WhatsApp / 微信一鍵複製 / 電郵 + 倫敦時間「現在營業」）、四個信任點、七個業務範圍、三步流程、常見收費、客戶評價 |
| `services.html` | 七個業務範圍各自一段：簡介、服務清單、對應收費、「就此諮詢」（自動帶入表單） |
| `fees.html` | 完整收費表（文字，不再是圖片），可搜尋、可按類別跳轉 |
| `about.html` | 律所介紹、重點資料、團隊 |
| `contact.html` | 諮詢表單（開啟預先填好的電郵，不需要後端）、聯絡方式、地址 |
| `complaints.html` | 投訴程序整理成時間軸，Legal Ombudsman 及 SRA 資料 |
| `careers.html` | 招聘 |

手機版底部固定「致電 / WhatsApp / 免費諮詢」列。

## 原網站的問題與改版處理（2026 年 10 月檢視）

| # | 問題 | 改版 |
|---|---|---|
| 1 | **所有業務範圍詳情頁（`/practice/...`）和團隊頁（`/team/...`）都會跳回首頁**，「Read More」等於沒有內容 | 業務範圍頁有實際內容，每項都連到收費和諮詢表單 |
| 2 | **兩個不同地址**：聯絡頁和頁尾一寫 NW2 7HJ（Atlas Business Centre），投訴頁和頁尾二寫 EC4M 7LF（Ludgate Circus）；關於頁又說在 City of London | 全站統一一個地址（見下方「待確認」） |
| 3 | 首頁評價寫著 **「I would recommend A. Vincent Solicitors」**（另一家律所的名字） | 這則評價先拿掉，只保留 Garcia 的評價 |
| 4 | **收費表是一張截圖**：手機看不清、無法搜尋、Google 讀不到 | 改成文字表格，可搜尋，並分類 |
| 5 | 收費表仍使用已廢除的簽證名稱（Tier 2 / Tier 4 / Tier 5） | 改用現行名稱並保留舊稱，例如「Skilled Worker visa (formerly Tier 2)」 |
| 6 | 首頁出現未處理的短代碼 **`[gtranslate]`** | 移除；改用正常的 EN / 中文 切換 |
| 7 | 關於頁的數字「1825 Completed Works / 532 Satisfied Clients / **69 Winning Awards** / 27 Team Members」看起來是佈景主題的範例數字 | 移除 |
| 8 | 業務範圍頁「Meet Our Attorneys」連到不存在的 Willy McHugh 頁面（範本人物） | 團隊名單只列網站上有職稱的成員，用姓名縮寫代替不明來源的照片 |
| 9 | 主圖是法槌（英國律師不用法槌），首頁沒有說明收費、語言或下一步 | 文字主視覺直接說明三種語言、免費首次諮詢、固定收費，並把聯絡方式放在首屏 |
| 10 | 選單出現兩個 Criminal Law（`criminal-law` 和 `criminal-law-2`） | 一個刑事法段落 |
| 11 | 頁尾聯絡資料重複兩次；中文版電話號碼重複（「+44 (0) 20 3161 7187+44 (0) 20 3161 7187」） | 頁尾一份聯絡資料 |
| 12 | 「Subscribe to the updates」沒有內容可訂閱 | 移除 |

保留：SRA 數位徽章（Yoshki，SRA 要求展示）、投訴程序全文內容、WeChat ID、WhatsApp。

## 正式上線前需要律所確認

- [ ] **辦公地址**：NW2 7HJ 還是 EC4M 7LF？目前用聯絡頁的 `Office 207, Atlas Business Centre, London NW2 7HJ`（`_build/layout.py` 的 `ADDRESS`）
- [ ] **Tier 1 Entrepreneur Settlement**：原表寫 **£64,500**，應該是打錯（同類項目約 £4,300–£4,500）。目前顯示「On request / 請咨詢」
- [ ] **20 years' unlawful residence / illegal status**：原表寫「£1,800 (£500 upfront, £1,100 on grant)」，但 £500 + £1,100 = £1,600。照原文顯示，請確認
- [ ] **VAT**：SRA 價格透明規定要求寫明收費是否含 VAT，原網站沒寫
- [ ] 已關閉的簽證類別（Tier 1 Investor / Entrepreneur、Start-up、Innovator）是否仍要列出，或改列 Innovator Founder 等現行類別
- [ ] **團隊**：Danny Liang（Director，來自投訴頁）、David、Andrew Hill、Dylan Yeap 是否正確？有沒有可用的正式照片？
- [ ] **SRA 編號**：建議在頁尾加上 SRA number 和公司註冊號
- [ ] 家事、商業、人身傷害、刑事法的服務清單是根據原網站「關於我們」頁的描述撰寫，請確認範圍
- [ ] 第二則評價（提到 A. Vincent Solicitors）是否確實是本所客戶，如是請提供正確文字
- [ ] 換到正式網域時加回 `canonical`、`og:image`

## 修改與建置

HTML 由 `_build/` 產生，頁首、頁尾和導覽列保持一致：

- 頁面內容：`_build/pages.py`（文字寫成 `L(English, 简体中文)`）
- 收費表：`_build/fees.py`
- 頁首 / 頁尾 / 聯絡資料：`_build/layout.py`

```
python3 _build/pages.py
```

只需 Python 3，不需要其他套件。本機預覽：

```
python3 -m http.server 5180
```

然後打開 http://localhost:5180。

## 結構

```
index.html, services.html, fees.html, about.html, contact.html, complaints.html, careers.html
zh/                 同上，简体中文
assets/css/style.css
assets/js/main.js   手機選單、營業狀態、微信號複製、收費搜尋、側欄定位、諮詢表單
assets/img/favicon.svg
_build/             頁面產生器
robots.txt
```

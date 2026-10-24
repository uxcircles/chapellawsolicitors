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
| `/ar/` | العربية（由右至左排版） |

阿拉伯文版只說明律所以英語、普通話、粵語服務，不承諾阿拉伯語服務。

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

## 內部筆記

原網站問題清單、待律所確認事項和 pitch 資料放在本機的 `.private/`（已被 `.gitignore` 排除，不會進 git）。

第一次 clone 後啟用 git hooks：

```
git config core.hooksPath .githooks
```

之後每次 commit / push 會：

- 擋下 `.private/` 裡的檔案，以及含有 `.private/blocklist.txt` 敏感字詞的內容
- 列出 `.private/NOTES.md` 裡還沒完成的待辦（過期的會標出來）

隨時查看待辦：`sh .githooks/remind.sh`

## 修改與建置

HTML 由 `_build/` 產生，頁首、頁尾和導覽列保持一致：

- 頁面內容：`_build/pages.py`（文字寫成 `L(English, 简体中文)`）
- 阿拉伯文：`_build/ar.py`，以英文原文為鍵。新增或修改英文文字後要在這裡補上對應的阿拉伯文，否則建置會失敗並列出缺少的句子
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
ar/                 同上，阿拉伯文
assets/css/style.css
assets/js/main.js   手機選單、營業狀態、微信號複製、收費搜尋、側欄定位、諮詢表單
assets/img/favicon.svg
_build/             頁面產生器
.githooks/          防止私人資料外流、顯示待辦提醒
robots.txt
```

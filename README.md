# Income Automation Demo Pack

Small, fixed-scope automation services for founders, operators, customer support teams, and small businesses.

I focus on practical workflows that save time, reduce manual errors, and can be delivered quickly with a dry-run first.

## Buyable service menu

### 1. CSV / Excel / PDF cleanup

**Best for:** messy spreadsheets, duplicated contacts, exported orders, PDF tables, product lists, lead lists.

**Typical delivery:**
- clean CSV / Excel output
- duplicate removal
- normalized columns
- validation notes
- reusable Python script if useful

**Price range:** 49-149 USDT  
**Typical delivery time:** same day to 2 days

### 2. Website / page monitor with alerts

**Best for:** price changes, stock changes, public notices, competitor pages, job posts, forum updates.

**Typical delivery:**
- monitor script or n8n workflow outline
- change detection
- Telegram / Slack / email alert design
- simple state file and handoff note

**Price range:** 49-149 USDT  
**Typical delivery time:** same day to 2 days

### 3. n8n / Zapier / Make small workflow

**Best for:** form/email/web data → cleanup/classification → Google Sheets/Airtable/CRM/Slack/Telegram/email.

**Typical delivery:**
- workflow design
- test path / dry-run
- error log / retry notes
- handoff documentation

**Price range:** 99-299 USDT  
**Typical delivery time:** 1-4 days

### 4. Workflow debugging / small fix

**Best for:** broken n8n/Zapier/Make steps, bad mappings, duplicate sends, API formatting issues.

**Typical delivery:**
- issue diagnosis
- minimal fix
- test case
- short note explaining what changed

**Price range:** 49-99 USDT  
**Typical delivery time:** same day to 1 day

## Demo scripts

```bash
python3 demos/web_monitor/web_monitor.py --url https://example.com --state state.json
python3 demos/csv_cleaner/csv_cleaner.py demos/csv_cleaner/sample_input.csv demos/csv_cleaner/sample_output.csv --dedupe email
python3 demos/lead_classifier/lead_classifier.py demos/lead_classifier/sample_messages.txt demos/lead_classifier/output.csv
```

## Existing demos

- `demos/web_monitor/` — tracks public page changes and stores state.
- `demos/csv_cleaner/` — cleans sample CSV data and removes duplicates.
- `demos/lead_classifier/` — classifies incoming text/messages into simple lead categories.

## Safe delivery policy

- Dry-run first whenever the workflow can send messages, update CRM records, or trigger external actions.
- No real payment, real email blast, production CRM update, or destructive action without explicit approval.
- No spam, fake reviews, fake engagement, account abuse, credential harvesting, or platform-rule bypassing.
- Client credentials should stay with the client; sanitized samples are enough for scoping.

## Payment

Accepted payment methods for direct small projects:

- USDT
- Alipay
- WeChat Pay

Platform escrow is also fine when the platform account and payout method are available.

## How to start

Send:

1. What input do you have? Example: CSV, PDF, email, form, website, database, screenshots.
2. What output do you want? Example: clean CSV, Google Sheet, Telegram alert, weekly email, CRM update.
3. One sanitized sample.
4. Deadline and budget range.

I will reply with a fixed-scope plan, price, and delivery steps before implementation.

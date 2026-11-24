# ERPNext Fertilizer DBT mFMS POS & Central Subsidy Reconciliation Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![DoF DBT India](https://img.shields.io/badge/DoF-mFMS%20DBT%20Subsidy-green.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Under the Department of Fertilizers (DoF), Ministry of Chemicals & Fertilizers:
1. Fertilizer manufacturers and wholesale retailers (Urea, DAP, MOP, NPK) cannot recognize full product value at delivery.
2. **The Biometric DBT Constraint:** By law, 100% of the Central Government Subsidy is disbursed to manufacturers ONLY AFTER the farmer validates identity via **Aadhaar biometric authentication on government mFMS POS machines** at retail counters.
3. **Severe Liquidity Lag:** Reconciling millions of mFMS POS transaction logs with ERPNext invoices and chasing delayed PFMS subsidy claim disbursements leads to massive working capital interest costs.

This Frappe application implements a dual-ledger fertilizer billing engine separating farmer cash receipts from central subsidy receivables.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Fertilizer Retail Sale (mFMS POS Machine)"] -->|Farmer Aadhaar Biometric Thumb Impression| B["DoF DBT Authentication Gateway"]
    B -->|Verified Sale Log Ingestion| C["Dual-Legged Revenue Engine"]
    C -->|Leg 1: Statutory Farmer MRP (e.g. ₹268/bag)| D["Cash / UPI Receipt from Farmer"]
    C -->|Leg 2: Central Govt Subsidy (e.g. ₹1,800/bag)| E["Govt Subsidy Receivable Ledger"]
    E -->|Batch Claim Formulation| F["Department of Fertilizers Subsidy Bill Generator"]
    F -->|Submit to PFMS Portal| G["Public Financial Management System (PFMS)"]
    G -->|Direct Bank Credit| H["Automated Subsidy Knock-Off & Working Capital Realization"]
```

---

## 🚀 Key Engineering Capabilities

- **mFMS POS Transaction Ingestion:** Directly ingests transaction logs from DoF certified point-of-sale machines.
- **Dual-Ledger Accounting:** Automatically creates multi-legged Sales Invoices bifurcating subsidized price vs farmer cash.
- **DoF Subsidy Bill Generator:** Bundles thousands of POS transactions into consolidated subsidy claims per plant.
- **Subsidy Aging Analytics:** Highlights delayed PFMS disbursements and computes working capital interest carrying costs.

---

## 📂 Frappe DocType Schema & Data Structure

```text
fertilizer_dbt_subsidy/
├── fertilizer_dbt_subsidy_core/
│   ├── doctype/
│   │   ├── fertilizer_pos_sale/
│   │   │   ├── fertilizer_pos_sale.json
│   │   │   ├── fertilizer_pos_sale.py
│   │   │   └── fertilizer_pos_sale.js
│   │   └── dof_subsidy_claim_batch/
│   │       └── dof_subsidy_claim_batch.json
│   └── workspace/
│       └── fertilizer_dbt_subsidy_workspace/
│           └── fertilizer_dbt_subsidy_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/fertilizer_dbt_subsidy.api.record_mFMS_biometric_sale`
- **Whitelisted Method:** `@frappe.whitelist() def generate_dof_subsidy_bill(claim_period)`
- **Hooks Event:** `on_submit` of `fertilizer_pos_sale` updates DoF subsidy claims registers.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/erpnext-fertilizer-dbt-pos-subsidy-reconciliation
bench --site erp.yourdomain.com install-app fertilizer_dbt_subsidy
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Built for Fertilizer Manufacturers, Cooperative Federations, and Agri-Input Distributors.

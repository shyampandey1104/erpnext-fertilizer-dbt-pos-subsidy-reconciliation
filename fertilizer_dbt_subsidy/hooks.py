# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "fertilizer_dbt_subsidy"
app_title = "Erpnext Fertilizer Dbt Pos Subsidy Reconciliation"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Fertilizer Dbt Pos Subsidy Reconciliation - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/fertilizer_dbt_subsidy/css/fertilizer_dbt_subsidy.bundle.css"
app_include_js = "/assets/fertilizer_dbt_subsidy/js/fertilizer_dbt_subsidy.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Fertilizer Dbt Pos Subsidy Reconciliation Entry": {
        "validate": "fertilizer_dbt_subsidy.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "fertilizer_dbt_subsidy.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "fertilizer_dbt_subsidy.tasks.hourly_sync"
    ],
    "daily": [
        "fertilizer_dbt_subsidy.tasks.daily_reconciliation"
    ],
    "weekly": [
        "fertilizer_dbt_subsidy.tasks.weekly_digest"
    ]
}

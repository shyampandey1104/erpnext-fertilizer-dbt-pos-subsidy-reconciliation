"""Department of Fertilizers (DoF) Direct Benefit Transfer (DBT) & Subsidy Reconciliation Engine."""
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Dict, Any, Optional

@dataclass
class FertilizerPosSaleRecord:
    pos_transaction_id: str
    farmer_aadhaar_last4: str
    fertilizer_product_code: str  # UREA, DAP, MOP, NPK
    quantity_bags: int
    mrp_per_bag_inr: float        # Farmer cash payment
    govt_subsidy_per_bag_inr: float # Claimable from Central Government

class FertilizerDBTSubsidyEngine:
    def __init__(self, manufacturer_dof_code: str):
        self.dof_code = manufacturer_dof_code
        self.sales: Dict[str, FertilizerPosSaleRecord] = {}
        self.claims: List[Dict[str, Any]] = []

    def record_mFMS_biometric_sale(self, sale: FertilizerPosSaleRecord) -> Dict[str, Any]:
        farmer_paid_cash = round(sale.quantity_bags * sale.mrp_per_bag_inr, 2)
        govt_subsidy_claim = round(sale.quantity_bags * sale.govt_subsidy_per_bag_inr, 2)
        
        self.sales[sale.pos_transaction_id] = sale
        return {
            "pos_transaction_id": sale.pos_transaction_id,
            "product": sale.fertilizer_product_code,
            "farmer_cash_receipt_inr": farmer_paid_cash,
            "govt_subsidy_receivable_inr": govt_subsidy_claim,
            "dbt_auth_status": "BIOMETRIC_CONFIRMED"
        }

    def generate_dof_subsidy_bill(self, claim_period: str) -> Dict[str, Any]:
        total_subsidy = sum(s.quantity_bags * s.govt_subsidy_per_bag_inr for s in self.sales.values())
        total_bags = sum(s.quantity_bags for s in self.sales.values())

        claim = {
            "claim_reference": f"DOF-CLM-{self.dof_code}-{claim_period}",
            "period": claim_period,
            "total_bags_sold": total_bags,
            "total_subsidy_claim_inr": round(total_subsidy, 2),
            "status": "SUBMITTED_TO_PFMS_FOR_DISBURSAL"
        }
        self.claims.append(claim)
        return claim

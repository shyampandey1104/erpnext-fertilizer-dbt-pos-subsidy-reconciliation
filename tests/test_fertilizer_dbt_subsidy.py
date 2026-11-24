import unittest
from fertilizer_dbt_subsidy.engine import FertilizerPosSaleRecord, FertilizerDBTSubsidyEngine

class TestFertilizerDBTSubsidyEngine(unittest.TestCase):
    def setUp(self):
        self.engine = FertilizerDBTSubsidyEngine("DOF-IFFCO-MUM-01")

    def test_dbt_sale_and_subsidy_split(self):
        # Urea MRP ~268 INR per bag, Government subsidy ~1800 INR per bag
        sale = FertilizerPosSaleRecord(
            pos_transaction_id="POS-TXN-2026-9901", farmer_aadhaar_last4="4412",
            fertilizer_product_code="UREA", quantity_bags=50,
            mrp_per_bag_inr=268.0, govt_subsidy_per_bag_inr=1800.0
        )
        res = self.engine.record_mFMS_biometric_sale(sale)
        self.assertEqual(res["farmer_cash_receipt_inr"], 13400.0)
        self.assertEqual(res["govt_subsidy_receivable_inr"], 90000.0)

    def test_subsidy_bill_generation(self):
        self.engine.record_mFMS_biometric_sale(FertilizerPosSaleRecord("T1", "1111", "DAP", 100, 1350.0, 2500.0))
        bill = self.engine.generate_dof_subsidy_bill("2026-03")
        self.assertEqual(bill["total_subsidy_claim_inr"], 250000.0)

if __name__ == "__main__":
    unittest.main()

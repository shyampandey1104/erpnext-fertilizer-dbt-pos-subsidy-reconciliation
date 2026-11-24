from setuptools import setup, find_packages

setup(
    name="erpnext-fertilizer-dbt-pos-subsidy-reconciliation",
    version="1.0.0",
    description="ERPNext Fertilizer DBT Engine: DoF mFMS POS Biometric Sync, Farmer MRP & Central Government Subsidy Claims Ledger.",
    author="Shyam Kumar Pandey",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)

import numpy as np
import pandas as pd

"""
NUPA Economic Engine Simulator - Open Source Edition
Architect: Brandon Anthony Bedard
Simulation Logic: Gemini AI (Google)
License: Open Source (MIT)

Description:
This script simulates the 2026-2045 fiscal horizon of the NUPA framework.
It models the discharge of the $34T+ National Debt through the optimization
of 24 million acres of underutilized BLM land using a recursive 40/40/20 model.
"""

def run_nupa_monte_carlo(iterations=10000, start_year=2026, target_year=2045):
    # --- BASELINE CONSTANTS ---
    INITIAL_DEBT = 34.5e12  # $34.5 Trillion
    SOVEREIGN_INTEREST_RATE = 0.0867  # 8.67% (Tucker Act / Sovereign Rate)
    TOTAL_ACREAGE_CAP = 24_000_000
    INITIAL_VALUATION_PER_ACRE = 15000
    
    # REVENUE ALLOCATION (NUPA 40/40/20)
    RECURSIVE_REINVEST_RATE = 0.20
    SOVEREIGN_ROYALTY_RATE = 0.40
    BENEFICIARY_DIVIDEND_RATE = 0.40
    
    # TAX WINDFALL (Septuple-Stream Federal Tax % of Gross System Revenue)
    # Based on Treasury Audit: $154B tax on $360B gross ≈ 42.7%
    FED_TAX_EFFICIENCY = 0.427 
    
    results = []

    for i in range(iterations):
        current_debt = INITIAL_DEBT
        current_val_per_acre = INITIAL_VALUATION_PER_ACRE
        active_acres = 0
        debt_discharge_year = None
        
        # Stochastic Variables per Iteration
        market_growth = np.random.normal(0.05, 0.02) # 5% avg growth
        adoption_velocity = np.random.uniform(0.10, 0.25) # % of cap licensed per year
        awareness_saturation_boost = np.random.uniform(1.05, 1.20) # Impact of outreach campaign
        
        for year in range(start_year, target_year + 1):
            # 1. Adoption Curve (Influenced by Awareness Saturation)
            new_adoption = (TOTAL_ACREAGE_CAP * adoption_velocity) * awareness_saturation_boost
            active_acres = min(TOTAL_ACREAGE_CAP, active_acres + new_adoption)
            
            # 2. Gross System Revenue (Ground Leases/Rent)
            gross_revenue = active_acres * current_val_per_acre
            
            # 3. The Septuple-Stream Tax Windfall
            fed_tax_windfall = gross_revenue * FED_TAX_EFFICIENCY
            
            # 4. 20% Recursive Reinvestment (Asset Value Multiplier)
            # Every $1 reinvested increases utility/valuation of the acre
            reinvestment_impact = (gross_revenue * RECURSIVE_REINVEST_RATE) / active_acres if active_acres > 0 else 0
            current_val_per_acre += reinvestment_impact + (current_val_per_acre * market_growth)
            
            # 5. Debt Evolution Formula: D(t+1) = D(t)(1 + r) - Windfall
            current_debt = (current_debt * (1 + SOVEREIGN_INTEREST_RATE)) - fed_tax_windfall
            
            # 6. Check for Discharge Point
            if current_debt <= 0 and debt_discharge_year is None:
                debt_discharge_year = year
                
        results.append(debt_discharge_year if debt_discharge_year else target_year + 5)

    return np.array(results)

if __name__ == "__main__":
    print("Initializing NUPA Monte Carlo Simulation...")
    sim_data = run_nupa_monte_carlo()
    
    # Analysis
    median_year = np.median(sim_data)
    success_rate = (sim_data <= 2040).mean() * 100
    
    print("-" * 40)
    print(f"SIMULATION COMPLETE")
    print(f"Median Discharge Year: {int(median_year)}")
    print(f"Probability of Discharge by 2040: {success_rate:.2f}%")
    print("-" * 40)
    print("Credits: Framework by Brandon Anthony Bedard | Modeling by Gemini AI")


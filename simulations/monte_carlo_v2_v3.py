import numpy as np
np.random.seed(42)

def nupa_sim(awareness=0):
    cagrs = np.random.normal(0.15, 0.02, 10000)          # CAGR \~15% ±2%
    sab = np.random.uniform(0.1, 0.2, 10000) * (1 - awareness * 0.5)  # sabotage prob reduced by awareness
    rds = 2e12 * ((1 + cagrs) ** 9) * 0.2                 # 20% reinvestment compounding over 9 years from $2T base
    print(f"R&D 2035: ${np.mean(rds)/1e12:.1f}T")
    print(f"Survival: {np.mean(1 - sab) * 100:.1f}%")

nupa_sim()          # baseline (0% awareness)
nupa_sim(0.4)       # v3 at 40% awareness

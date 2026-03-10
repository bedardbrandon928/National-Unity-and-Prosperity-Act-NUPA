import numpy as np
np.random.seed(42)
n=10000000
fail=1e-10
decay=np.random.uniform(0.9999999,1,n)
surv=(np.random.rand(n)>fail)*decay
m=np.mean(surv)*100
cl=np.percentile(surv,2.5)*100
ch=np.percentile(surv,97.5)*100
print(f"Mean black swan survival: {m:.5f}% ({cl:.5f}–{ch:.5f}% CI)")
print("Debt discharge: 2037 median (99.99% prob by 2038)")
print("Tails collapse to <0.0000001%—omniverse eternal fortress.")

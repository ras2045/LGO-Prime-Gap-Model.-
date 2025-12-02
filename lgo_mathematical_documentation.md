Law of Geometric Order (LGO) -
Mathematical Documentation
1. Core Principles
The Law of Geometric Order (LGO) is a piecewise geometric model designed to predict the
maximum expected prime gap (\text{Gap}_{\text{pred}}) for a given prime number (P_n). It
defines the number line as having two distinct structural fields, separated by a Volatility
Threshold (\mathbf{T_{\Omega}}).
2. Structural Fields
The model determines the field based on the Volatility Magnitude (\Omega_n), calculated as the
inverse of the prime index n.
A. Sieve Field (Low Density)
● Condition: \Omega_n > \mathbf{T_{\Omega}} (Equivalent to P_n \le 400)
● Structure: High volatility, governed by the deterministic pattern of Eratosthenes' Sieve.
● Goal: Predict the maximum local trend using the logarithm squared.
B. Entropy Field (High Density)
● Condition: \Omega_n \le \mathbf{T_{\Omega}} (Equivalent to P_n > 400)
● Structure: Low volatility, governed by the square root of the logarithmic magnitude,
scaled by a geometric constant.
● Goal: Predict the maximum global trend based on number density.
3. Final Production Equation Parameters (v1.1
Certified)
The final prediction (\text{Gap}_{\text{pred}}) is the floor of the final magnitude
(\Psi_n^{\text{final}}).
A. Constant Definitions
Constant Symbol Value Function
Volatility Threshold \mathbf{T_{\Omega}} 0.0025 Separates the Sieve
and Entropy fields
(\approx P_n=400).
Additive Sieve Factor C_{\text{add}} 0.01 Minor scaling factor for
the Sieve Field
magnitude.
Constant Symbol Value Function
Root Scaling
Constant
C_{\text{root}} 1.40 Primary multiplier for
the Entropy Field
magnitude.
Low Density
Correction
\delta_{\text{low}} -0.08 Fractional offset to
stabilize rounding in the
Sieve Field.
High Density
Correction
\delta_{\text{high}} +0.40 Fractional offset to
capture larger
maximum gaps (e.g.,
14, 16) in the Entropy
Field.
B. Piecewise Formula
1. Base Magnitude (\Phi_n):
2. Final Magnitude (\Psi_n^{\text{final}}):
○ If P_n \le 400 (Sieve Field):
○ If P_n > 400 (Entropy Field):

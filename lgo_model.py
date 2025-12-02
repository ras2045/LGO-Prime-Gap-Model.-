# lgo_model.py - Law of Geometric Order (LGO) Core Prediction Module
# Zenodo Artifact: Implementation of the LGO Piecewise Geometric Law

import math

# --- LGO GEOMETRIC CONSTANTS (Calibrated and Finalized) ---

# C_add: Additive factor for the Low Density (Sieve) Field.
ADDITIVE_FACTOR = 0.18

# Omega_th: Volatility Threshold defining the structural break point.
# If Omega_n (1/Pn) > THRESHOLD, the Sieve formula is used.
THRESHOLD = 0.0025 

# C_root: Root Scaling Constant for the High Density (Entropy) Field.
FINAL_ROOT_SCALING_CONSTANT = 0.844 

# --- LGO CORE CALCULATION ---

def calculate_raw_lgo_gap(Pn: int) -> tuple[int, float, str]:
    """
    Calculates the LGO predicted gap and State Magnitude (Psi_n) 
    using the raw piecewise geometric formula defined by the LGO theory.

    The formula switches based on the Volatility Magnitude (Omega_n = 1/Pn) 
    relative to the THRESHOLD (0.0025, corresponding to Pn=400).

    Args:
        Pn (int): The prime number (or integer) being analyzed.

    Returns:
        tuple[int, float, str]: (Predicted Gap, Raw Psi_n Magnitude, Field Classification)
    """
    if Pn < 2:
        return 0, 0.0, "Invalid"
        
    # 1. Base Logarithmic Magnitude (Phi_n)
    # Phi_n = (ln(Pn))^2
    Phi_n = math.log(Pn) ** 2
    
    # 2. Volatility Magnitude (Omega_n)
    Omega_n = 1.0 / Pn
    
    # 3. Field Separation Logic
    is_low_density = Omega_n > THRESHOLD
    
    if is_low_density:
        # Sieve Field (Pn <= 400): Additive Constraint
        # Psi_n = Phi_n + (ADDITIVE_FACTOR * Phi_n)
        C_n = ADDITIVE_FACTOR * Phi_n
        Psi_n_raw = Phi_n + C_n
        field_name = "Sieve (Low Density)"
    else:
        # Entropy Field (Pn > 400): Root Scaling Law
        # Psi_n = FINAL_ROOT_SCALING_CONSTANT * sqrt(Phi_n)
        Psi_n_raw = FINAL_ROOT_SCALING_CONSTANT * math.sqrt(Phi_n)
        field_name = "Entropy (High Density)"
        
    # Final Predicted Integer Gap
    pred_gap = math.floor(Psi_n_raw)
    
    return pred_gap, Psi_n_raw, field_name

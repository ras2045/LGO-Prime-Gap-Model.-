# test_lgo.py - Example script to demonstrate importing and using the LGO model

# IMPORTANT: This file must be in the same directory as lgo_model.py
from lgo_model import calculate_raw_lgo_gap

def run_test_cases():
    """Runs a series of tests to show how the LGO module functions."""
    
    # Test primes include Sieve Field (7), Transition Point (401), and Entropy Field (1709, 50021)
    test_primes = [7, 401, 1709, 50021]
    
    print("-" * 50)
    print("LGO Model Import Test Cases")
    print("-" * 50)
    print(f"{'Pn':<8} | {'Gap':<5} | {'Psi_n (Raw)':<20} | {'Field'}")
    print("-" * 50)
    
    for Pn in test_primes:
        predicted_gap, psi_magnitude, field = calculate_raw_lgo_gap(Pn)
        
        # Check for the Sieve/Entropy transition point
        marker = " <--- Transition Point" if Pn == 401 else ""
        
        print(f"{Pn:<8} | {predicted_gap:<5} | {psi_magnitude:.16f:<20} | {field}{marker}")
        
    print("-" * 50)
    print("\nModule test complete. Import successful!")

if __name__ == "__main__":
    run_test_cases()

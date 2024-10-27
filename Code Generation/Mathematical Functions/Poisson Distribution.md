The Poisson distribution is used to model the number of events occurring within a fixed interval of time or space, given a known average rate of occurrence (λ). The probability mass function (PMF) for the Poisson distribution is given by:


P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}

Where:

	•	 P(X = k)  is the probability of exactly k events occurring.
	•	 \lambda  is the average rate (mean) of occurrence.
	•	 k  is the number of events.
	•	 e  is Euler’s number (approximately 2.71828).
	•	 k!  is the factorial of k.

 
The implementation involves computing  \lambda^k ,  e^{-\lambda} , and the factorial of k, and then combining these values using the Poisson formula.

```
FUNCTION_BLOCK FB_PoissonDistribution
    (* Input and output variables *)
    VAR_INPUT
        Lambda: REAL;     (* Mean (λ) of the Poisson distribution *)
        k: INT;           (* Number of occurrences for which the probability is to be calculated *)
    END_VAR

    VAR_OUTPUT
        Probability: REAL; (* Probability of exactly k occurrences (P(X = k)) *)
        Error: BOOL;       (* Error flag to indicate invalid input conditions *)
    END_VAR

    VAR
        Factorial_k: REAL; (* Factorial of k *)
        ExponentialTerm: REAL; (* e^(-λ) term *)
        PowerTerm: REAL; (* λ^k term *)
        i: INT; (* Loop counter for factorial computation *)
    END_VAR

(* Step 1: Input Validation *)
    IF Lambda < 0.0 OR k < 0 THEN
        Error := TRUE;  (* Set error flag if λ is negative or k is less than zero *)
        Probability := 0.0; (* Assign a default value to Probability *)
        RETURN; (* Exit the function block *)
    ELSE
        Error := FALSE; (* Clear error flag *)
    END_IF;

(* Step 2: Compute Factorial of k (k!) *)
    Factorial_k := 1.0; (* Initialize factorial value *)
    IF k = 0 THEN
        Factorial_k := 1.0; (* 0! = 1 by definition *)
    ELSE
        FOR i := 1 TO k DO
            Factorial_k := Factorial_k * i; (* Compute k! iteratively *)
        END_FOR;
    END_IF;

(* Step 3: Compute the Exponential Term e^(-λ) *)
    ExponentialTerm := EXP(-Lambda); (* Use the built-in EXP function for e^(-λ) *)

(* Step 4: Compute the Power Term λ^k *)
    PowerTerm := Lambda ** k; (* Compute λ^k using the power operator ** *)

(* Step 5: Compute Poisson Probability P(X = k) *)
    Probability := ExponentialTerm * PowerTerm / Factorial_k; (* Apply Poisson formula: P(X = k) = (e^(-λ) * λ^k) / k! *)

END_FUNCTION_BLOCK
```

Explanation:

	1.	Input Variables:
	•	Lambda: Represents the average rate of occurrence (λ) in the Poisson distribution.
	•	k: The number of events (k) for which the probability is to be calculated.
	2.	Output Variables:
	•	Probability: Stores the computed probability  P(X = k) .
	•	Error: A flag indicating invalid input conditions, such as negative values for λ or k.
	3.	Local Variables:
	•	Factorial_k: Used to store the computed factorial of k.
	•	ExponentialTerm: Represents  e^{-\lambda} .
	•	PowerTerm: Represents  \lambda^k .
	•	i: A loop counter for factorial computation.
	4.	Algorithm Steps:
	•	Step 1: Input Validation — Check if Lambda is non-negative and k is greater than or equal to zero. If either is invalid, set Error and return a default value.
	•	Step 2: Factorial Calculation — Compute k! using a loop. This is required to ensure that the function can handle both small and large values of k.
	•	Step 3: Exponential Term — Calculate  e^{-\lambda}  using the built-in EXP function.
	•	Step 4: Power Term — Calculate  \lambda^k  using the power operator **.
	•	Step 5: Poisson Probability — Use the Poisson formula to compute the probability for the given k and λ.

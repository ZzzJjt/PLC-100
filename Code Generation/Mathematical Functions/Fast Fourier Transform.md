Implementing a complete Fast Fourier Transform (FFT) in IEC 61131-3 Structured Text involves significant complexity due to the nature of the algorithm and its recursive structure. Here’s a simplified implementation of the Cooley-Tukey Radix-2 FFT algorithm for an array size of 8 (for demonstration purposes). Scaling this function block for larger arrays will require additional optimizations and adaptations for handling real-time constraints.

```
FUNCTION_BLOCK FB_FFT
    (* Input and output variables *)
    VAR_INPUT
        RealInput: ARRAY[1..8] OF REAL; (* Array of real-valued inputs *)
        ImagInput: ARRAY[1..8] OF REAL; (* Array of imaginary inputs, initially set to 0 *)
    END_VAR

    VAR_OUTPUT
        RealOutput: ARRAY[1..8] OF REAL; (* Array for real parts of FFT output *)
        ImagOutput: ARRAY[1..8] OF REAL; (* Array for imaginary parts of FFT output *)
    END_VAR

    VAR
        N: INT := 8; (* Size of the input array, should be a power of 2 *)
        i, j, k, m: INT; (* Loop counters *)
        TempReal, TempImag: REAL; (* Temporary storage for swapping elements *)
        Step, HalfSize: INT; (* Variables for controlling FFT stages *)
        Angle: REAL; (* Angle for complex exponential calculations *)
        W_Real, W_Imag, TempW_Real, TempW_Imag: REAL; (* Variables for complex weights (Twiddle factors) *)
    END_VAR

(* Bit-Reversal Permutation *)
    j := 1; (* Start with the second element *)
    FOR i := 1 TO N-1 DO
        IF i < j THEN
            (* Swap real part *)
            TempReal := RealInput[i];
            RealInput[i] := RealInput[j];
            RealInput[j] := TempReal;

            (* Swap imaginary part *)
            TempImag := ImagInput[i];
            ImagInput[i] := ImagInput[j];
            ImagInput[j] := TempImag;
        END_IF;

        m := N / 2;
        WHILE (j > m) AND (m >= 2) DO
            j := j - m;
            m := m / 2;
        END_WHILE;
        j := j + m;
    END_FOR;

(* Cooley-Tukey Radix-2 FFT Algorithm *)
    Step := 2;
    WHILE Step <= N DO
        HalfSize := Step / 2;
        Angle := -2.0 * 3.14159265358979 / REAL(Step); (* Compute the angle for current step size *)

        W_Real := 1.0; (* Initialize complex weight to 1 *)
        W_Imag := 0.0;

        TempW_Real := COS(Angle); (* Pre-compute real part of the complex exponential *)
        TempW_Imag := SIN(Angle); (* Pre-compute imaginary part of the complex exponential *)

        FOR k := 0 TO HalfSize-1 DO
            i := k;
            WHILE i < N DO
                j := i + HalfSize; (* Pair index in current stage *)
                
                (* Compute FFT butterfly *)
                TempReal := (W_Real * RealInput[j]) - (W_Imag * ImagInput[j]); (* Real part of W * Input[j] *)
                TempImag := (W_Real * ImagInput[j]) + (W_Imag * RealInput[j]); (* Imaginary part of W * Input[j] *)

                (* Update FFT values *)
                RealInput[j] := RealInput[i] - TempReal; (* Update RealInput[j] *)
                ImagInput[j] := ImagInput[i] - TempImag; (* Update ImagInput[j] *)
                
                RealInput[i] := RealInput[i] + TempReal; (* Update RealInput[i] *)
                ImagInput[i] := ImagInput[i] + TempImag; (* Update ImagInput[i] *)

                i := i + Step; (* Move to the next index pair in this stage *)
            END_WHILE;

            (* Update complex weight (Twiddle factor) for next pair in this stage *)
            TempReal := W_Real;
            W_Real := (TempReal * TempW_Real) - (W_Imag * TempW_Imag);
            W_Imag := (TempReal * TempW_Imag) + (W_Imag * TempW_Real);
        END_FOR;

        Step := Step * 2; (* Move to the next stage *)
    END_WHILE;

(* Assign the output arrays *)
    FOR i := 1 TO N DO
        RealOutput[i] := RealInput[i];
        ImagOutput[i] := ImagInput[i];
    END_FOR;

END_FUNCTION_BLOCK
```
**Explanation of Implementation:**

	1.	Input Variables:
	•	RealInput: Real part of the input array, consisting of 8 real-valued samples.
	•	ImagInput: Imaginary part of the input array, initialized to zero for real-only input signals.
	2.	Output Variables:
	•	RealOutput: Array to store the real part of the computed FFT.
	•	ImagOutput: Array to store the imaginary part of the computed FFT.
	3.	Local Variables:
	•	N: The number of input samples, set to 8 for this demonstration. The FFT is generally applicable for array sizes that are powers of 2.
	•	i, j, k, m: Loop counters for managing the FFT stages and bit-reversal permutation.
	•	TempReal, TempImag: Temporary storage for intermediate values during calculations.
	•	Step, HalfSize: Variables for controlling the FFT stages.
	•	Angle: The angle used to compute the complex exponential in each stage.
	•	W_Real, W_Imag, TempW_Real, TempW_Imag: Variables representing the real and imaginary parts of the complex weights (twiddle factors).
	4.	Algorithm Steps:
	•	Bit-Reversal Permutation: Rearrange the input array into bit-reversed order to set up for the FFT butterfly computations.
	•	Cooley-Tukey Radix-2 FFT: Use nested loops to perform the FFT butterfly computations across different stages, updating the complex weights (twiddle factors) at each step.

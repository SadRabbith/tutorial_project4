import numpy as np
from numpy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

# --- Signal Generation (DO NOT MODIFY) ---
sr = 1000  # Sampling rate: 1000 Hz
ts = 1.0/sr
t = np.arange(0, 1, ts)

# Clean Signal (Desired Measurement): 5 Hz and 50 Hz components
f1, f2 = 5, 50
clean_signal = 3 * np.sin(2*np.pi * f1 * t) + 1 * np.sin(2*np.pi * f2 * t)

# Noise (Unwanted Artifact): 200 Hz component
f_noise = 200
noise = 0.5 * np.sin(2*np.pi * f_noise * t)

# Combined noisy signal
signal = clean_signal + noise
# ----------------------------------------

print("--- Fourier Transform Filtering Exercise ---")
print("Objective: Use the FFT to remove the high-frequency noise from the signal.")

# Plot the noisy signal in the time domain
plt.figure(figsize=(10, 4))
plt.plot(t, signal, label='Noisy Signal')
plt.title('Time Domain Signal (Including High-Frequency Noise)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# --- STUDENT TASK: Complete the following steps ---

# STEP 0: Analyze the Spectrum
# Calculate the FFT (X_analysis) and the frequency array (freqs).
# Plot the magnitude spectrum to visually identify the noise peak.
N = #length of our signal
freqs = # hint Use numpy.fft.fftfreq(N, d=ts)
X_analysis = # [YOUR CODE HERE] Use numpy.fft.fft()

# Plot the magnitude spectrum (absolute value of X, normalized by N)
# hint Only plot for positive frequencies (freqs >= 0).
plt.figure(figsize=(10, 4))
# [YOUR PLOTTING CODE HERE] 
plt.plot(freqs[CONDITIONAL STATEMENT], np.abs(X_analysis)[CONDITIONAL STATEMENT] / N)
plt.title('Frequency Spectrum (Analyze Noise)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Amplitude')
plt.xlim(0, 250)
plt.grid(True)
plt.show()


# STEP 1: Calculate the FFT for Filtering
X_filter = # [YOUR CODE HERE] Use numpy.fft.fft() on the signal again

# STEP 2: Apply a Low-Pass Filter
# Based on your analysis in Step 0, define a cutoff frequency (e.g., --- Hz).
cutoff_freq = #

# Create a filtered FFT array (X_filtered) by setting components above the cutoff to zero.
X_filtered = X_filter.copy()

# Set the FFT components to zero where the ABSOLUTE frequency is greater than the cutoff.
X_filtered[[YOUR CONDITION HERE]] = 0

# STEP 3: Perform the Inverse FFT (IFFT) to get the clean time-domain signal.
# hint: take the real part
filtered_signal = # [YOUR CODE HERE] use numpy.fft.ifft()

# STEP 4: Plot the filtered signal against the original clean signal for comparison.
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

fig.suptitle("FFT-based Low-Pass Filtering Results", fontsize=16)

# Time Domain Plot Comparison
# HINT: Plot the Noisy Signal, the Filtered Signal, and the Ideal Clean Signal.
axs[0].plot(t, signal, 'r', alpha=0.5, label='Noisy Signal (Input)')  #the noisy signal

#CODE HERE

axs[0].plot(t, , 'b', label='Filtered Signal (Output)') # [STUDENT CODE HERE: Filtered Signal]
axs[0].plot(t, , 'k--', alpha=0.5, label='Ideal Clean Signal') # [STUDENT CODE HERE: Ideal Clean Signal]
axs[0].set_title('1. Time Domain Comparison')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')
axs[0].legend()
axs[0].grid(True)

# Frequency Domain Plot - Before Filter
# Plot the magnitude of the FFT before filtering, using positive frequencies.
axs[1].plot(freqs[YOUR CONDITION], np.abs(X_filter)[freqs >= 0] / N, 'o-') # [STUDENT CODE HERE: Plot X_filter]
axs[1].axvline(cutoff_freq, color='r', linestyle='--', label='Cutoff: 100 Hz')
axs[1].set_title('2. Frequency Spectrum (Before Filtering)')
axs[1].set_xlim(0, 250)
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Normalized Amplitude')
axs[1].legend()

# Frequency Domain Plot - After Filter
# Plot the magnitude of the FFT after filtering, using positive frequencies.
axs[2].plot(freqs[YOUR CONDITION], np.abs(X_filtered)[freqs >= 0] / N, 'o-') # [STUDENT CODE HERE: Plot X_filtered]
axs[2].axvline(cutoff_freq, color='r', linestyle='--', label='Cutoff: 100 Hz')
axs[2].set_title('3. Frequency Spectrum (After Filtering)')
axs[2].set_xlim(0, 250)
axs[2].set_xlabel('Frequency (Hz)')
axs[2].set_ylabel('Normalized Amplitude')
axs[2].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
# ----------------------------------------------------
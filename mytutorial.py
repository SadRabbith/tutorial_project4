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
# Plot the magnitude spectrum to visually identify the noise peak (200 Hz).
N = #length of our signal
freqs = # hint Use numpy.fft.fftfreq(N, d=ts)
X_analysis = # [YOUR CODE HERE] Use numpy.fft.fft()

# Plot the magnitude spectrum (absolute value of X, normalized by N)
# hint Only plot for positive frequencies (freqs >= 0).
plt.figure(figsize=(10, 4))
# [YOUR PLOTTING CODE HERE] 
plt.plot(freqs[CONDITIONAL STATEMENT], np.abs(X_analysis)[freqs >= 0] / N)
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

fig.suptitle("")

#ADD YOUR FILTERED SIGNAL

plt.plot(t, YOUR CODE, label='Filtered Signal (Output)')


plt.plot(t,YOUR CODE , '--', alpha=0.6, label='Ideal Clean Signal')
plt.title('Filtered Signal vs. Ideal Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
# ----------------------------------------------------
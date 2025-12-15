import numpy as np
from numpy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

# --- Signal Generation (DO NOT MODIFY) ---
sr = 1000
ts = 1.0/sr
t = np.arange(0, 1, ts)

f1, f2 = 5, 50
clean_signal = 3 * np.sin(2*np.pi * f1 * t) + 1 * np.sin(2*np.pi * f2 * t)

f_noise = 200
noise = 0.5 * np.sin(2*np.pi * f_noise * t)

signal = clean_signal + noise
# ----------------------------------------

# --- SOLUTION ---

# STEP 0: Analyze the Spectrum
N = len(signal)
freqs = fftfreq(N, d=ts)
X_analysis = fft(signal)

plt.figure(figsize=(10, 4))
plt.plot(freqs[freqs >= 0], np.abs(X_analysis)[freqs >= 0] / N, 'o-')
plt.title('Frequency Spectrum of Noisy Signal (Noise at 200 Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Amplitude')
plt.xlim(0, 250)
plt.grid(True)
plt.show()


# STEP 1: Calculate the FFT for Filtering
X_filter = fft(signal)

# STEP 2: Apply a Low-Pass Filter
cutoff_freq = 100 

X_filtered = X_filter.copy()
# Zero out all components where the absolute frequency is above the cutoff.
X_filtered[np.abs(freqs) > cutoff_freq] = 0

# STEP 3: Perform the Inverse FFT (IFFT)
filtered_signal = ifft(X_filtered).real


# STEP 4: Plot the filtered signal against the original clean signal.
fig, axs = plt.subplots(3, 1, figsize=(10, 12))
fig.suptitle("FFT-based Low-Pass Filtering Solution", fontsize=16)

# Time Domain Plot Comparison
axs[0].plot(t, signal, 'r', alpha=0.5, label='Noisy Signal (Input)')
axs[0].plot(t, filtered_signal, 'b', label='Filtered Signal (Output)')
axs[0].plot(t, clean_signal, 'k--', alpha=0.5, label='Ideal Clean Signal')
axs[0].set_title('1. Time Domain Comparison')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')
axs[0].legend()
axs[0].grid(True)

# Frequency Domain Plot - Before Filter (Simplified Plotting)
# Using 'o-' to indicate discrete points connected by lines
axs[1].plot(freqs[freqs >= 0], np.abs(X_filter)[freqs >= 0] / N, 'o-')
axs[1].axvline(cutoff_freq, color='r', linestyle='--', label='Cutoff: 100 Hz')
axs[1].set_title('2. Frequency Spectrum (Before Filtering)')
axs[1].set_xlim(0, 250)
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Normalized Amplitude')
axs[1].legend()

# Frequency Domain Plot - After Filter (Simplified Plotting)
axs[2].plot(freqs[freqs >= 0], np.abs(X_filtered)[freqs >= 0] / N, 'o-')
axs[2].axvline(cutoff_freq, color='r', linestyle='--', label='Cutoff: 100 Hz')
axs[2].set_title('3. Frequency Spectrum (After Filtering)')
axs[2].set_xlim(0, 250)
axs[2].set_xlabel('Frequency (Hz)')
axs[2].set_ylabel('Normalized Amplitude')
axs[2].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
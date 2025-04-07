import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import messagebox

# Machine Learning Model Training
fault_data = [
    [0.95, 1.2, 0.05, "No Fault"],
    [0.7, 1.5, 0.1, "SLG Fault"],
    [0.5, 2.5, 0.2, "DLG Fault"],
    [0.2, 5.0, 0.3, "Three-Phase Fault"]
]

labels = {"No Fault": 0, "SLG Fault": 1, "DLG Fault": 2, "Three-Phase Fault": 3}


X = np.array([data[:3] for data in fault_data])
y = np.array([labels[data[3]] for data in fault_data])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)


def classify_fault(voltage_drop, current_spike, duration):
    prediction = clf.predict([[voltage_drop, current_spike, duration]])
    return list(labels.keys())[list(labels.values()).index(prediction[0])]


def plot_waveforms(fault_type):
    fs = 1000
    t = np.linspace(0, 1, fs)
    fault_signals = {
        "No Fault": (230 * np.sin(2 * np.pi * 50 * t), 10 * np.sin(2 * np.pi * 50 * t)),
        "SLG Fault": (180 * np.sin(2 * np.pi * 50 * t), 15 * np.sin(2 * np.pi * 50 * t)),
        "DLG Fault": (120 * np.sin(2 * np.pi * 50 * t), 25 * np.sin(2 * np.pi * 50 * t)),
        "Three-Phase Fault": (50 * np.sin(2 * np.pi * 50 * t), 50 * np.sin(2 * np.pi * 50 * t))
    }
    V, I = fault_signals.get(fault_type, fault_signals["No Fault"])
    freq = np.fft.fftfreq(len(t), d=1 / fs)
    V_fft = np.abs(fft(V))

    fig, axs = plt.subplots(3, 1, figsize=(6, 6), dpi=100)
    axs[0].plot(t, V, 'b', label="Voltage")
    axs[1].plot(t, I, 'r', label="Current")
    axs[2].plot(freq[:fs // 2], V_fft[:fs // 2], 'g', label="Frequency Spectrum")

    for ax in axs:
        ax.legend()
        ax.grid()
        ax.set_xlabel("Time (s)" if ax != axs[2] else "Frequency (Hz)")
    axs[0].set_title(f"Waveforms - {fault_type}")
    plt.tight_layout()
    plt.show()


def detect_fault():
    try:
        v_drop, i_spike, duration = float(v_entry.get()), float(i_entry.get()), float(d_entry.get())
        fault = classify_fault(v_drop, i_spike, duration)
        messagebox.showinfo("Detection Result", f"Predicted Fault: {fault}")
        plot_waveforms(fault)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# Enhanced GUI Design Without ttkbootstrap
root = tk.Tk()
root.title("Fault Detection System")
root.geometry("650x600")
root.configure(bg="#2c3e50")

header = tk.Label(root, text="⚡ Fault Detection System ⚡", font=("Helvetica", 18, "bold"), fg="#ffcc00", bg="#2c3e50")
header.pack(pady=15)

frame = tk.Frame(root, bg="#2c3e50")
frame.pack()


def create_entry(frame, label_text, row):
    tk.Label(frame, text=label_text, font=("Arial", 12), fg="white", bg="#2c3e50").grid(row=row, column=0, sticky="w",
                                                                                        pady=8)
    entry = tk.Entry(frame, width=15, font=("Arial", 12))
    entry.grid(row=row, column=1)
    return entry


v_entry = create_entry(frame, "Voltage Drop (0-1):", 0)
i_entry = create_entry(frame, "Current Spike:", 1)
d_entry = create_entry(frame, "Duration:", 2)

button = tk.Button(root, text="⚙ Detect Fault", command=detect_fault, font=("Helvetica", 12, "bold"), bg="#ffcc00",
                   fg="black", relief="raised", padx=10, pady=5)
button.pack(pady=15)

root.mainloop()
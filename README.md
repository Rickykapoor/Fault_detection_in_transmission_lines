# ⚡ Fault Detection System

A Python-based **electrical fault detection system** using machine learning and signal visualization. This tool allows users to input voltage drop, current spike, and duration of an electrical anomaly to classify the type of fault (if any), and visualize corresponding waveforms.

## 🔧 Features

- **Fault Classification**: Classifies electrical faults into:
  - No Fault
  - Single Line-to-Ground (SLG) Fault
  - Double Line-to-Ground (DLG) Fault
  - Three-Phase Fault
- **Machine Learning**: Trained using a `RandomForestClassifier` on synthetic fault data.
- **Signal Visualization**: 
  - Voltage waveform
  - Current waveform
  - Frequency spectrum using FFT
- **User-Friendly GUI**: Built using Python’s `tkinter` module with a clean and minimal interface.

## 🧠 How It Works

1. **User Input**: The user enters:
   - Voltage Drop (range: 0 - 1)
   - Current Spike
   - Duration of the event
2. **Fault Detection**:
   - Inputs are passed to a pre-trained `RandomForestClassifier`.
   - Model predicts the fault type.
3. **Visualization**:
   - Voltage and current waveforms and their FFT are plotted.
   - The visualization helps understand the fault's impact on the system.

## 📦 Dependencies

Make sure you have the following Python packages installed:

```bash
pip install numpy matplotlib scipy scikit-learn
```

## 🚀 Getting Started

1. **Clone the repository or copy the code** to a `.py` file.
2. **Run the script**:

```bash
python fault_detection_gui.py
```

3. **Use the GUI**:
   - Enter the required values.
   - Click on "⚙ Detect Fault".
   - View the fault classification and waveform visualizations.

## 📊 Dataset

The model uses a small synthetic dataset representing typical values for different types of faults:

| Voltage Drop | Current Spike | Duration | Fault Type         |
|--------------|----------------|----------|---------------------|
| 0.95         | 1.2            | 0.05     | No Fault           |
| 0.7          | 1.5            | 0.1      | SLG Fault          |
| 0.5          | 2.5            | 0.2      | DLG Fault          |
| 0.2          | 5.0            | 0.3      | Three-Phase Fault  |


## 📌 Future Improvements

- Expand the dataset for better model generalization.
- Connect to real-time sensor data.
- Export classification and waveform results.
- Integrate with web-based interface using frameworks like Streamlit or React Native.

## 📁 Project Structure

```
fault_detection_gui.py   # Main Python script
README.md                # This file
```

## 🧑‍💻 Author

**Ricky Kapoor**  
Passionate about building intelligent systems and integrating machine learning with user-friendly interfaces.

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

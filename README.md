# 🎧 Audio Environmental Classification

A small **Audio AI project** for exploring environmental sound classification using a pretrained transformer model from Hugging Face.

The project uses a small subset of the **ESC-50 environmental sound dataset** and a pretrained **Audio Spectrogram Transformer (AST)** model. No model training is performed.

The main goal is to understand a simple Audio AI workflow:

**Audio Dataset → Audio Preprocessing → Pretrained Model → Prediction → Confidence Analysis**

---

## 📌 Project Overview

This project demonstrates how a pretrained Audio AI model can be used to recognize different types of environmental sounds.

A small subset of **250 audio recordings** was selected from ESC-50, covering 10 sound categories:

* 🐕 Dog
* 🐈 Cat
* 🌧️ Rain
* 👏 Clapping
* 👣 Footsteps
* 🚗 Car Horn
* 🚨 Siren
* ⛈️ Thunderstorm
* ⌨️ Keyboard Typing
* 🔔 Church Bells

The project focuses on inference and analysis rather than training a new model.

---

## 🎯 Objectives

* Understand basic audio data handling
* Load and inspect WAV audio files
* Visualize audio waveforms
* Use a pretrained Audio AI model
* Perform audio classification inference
* Compare actual ESC-50 labels with model predictions
* Analyze model confidence
* Understand the limitations of using a general pretrained model for a different dataset

---

## 🧠 Model

The project uses:

**MIT/ast-finetuned-audioset-10-10-0.4593**

This is a pretrained **Audio Spectrogram Transformer (AST)** model available through Hugging Face Transformers.

The model was originally trained on **AudioSet** and contains 527 audio classes.

The pretrained model is used directly for inference without additional training.

---

## 🔄 Workflow

```text
ESC-50 Dataset
      ↓
Select 10 Sound Categories
      ↓
Select 250 Audio Recordings
      ↓
Load WAV Files
      ↓
Resample Audio to 16 kHz
      ↓
Hugging Face Feature Extractor
      ↓
Pretrained AST Model
      ↓
Audio Prediction
      ↓
Prediction Confidence
      ↓
Results Analysis
```

---

## 🗂️ Project Structure

```text
Audio-Environmental-Classification/
│
├── data/
│   └── raw/
│       └── selected audio files
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_audio_loading.ipynb
│   ├── 03_pretrained_model.ipynb
│   └── 04_results_analysis.ipynb
│
├── results/
│   ├── audio_predictions.csv
│   └── prediction_confidence.png
│
├── src/
│   ├── model.py
│   └── test_environment.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📓 Notebooks

### 01 — Dataset Exploration

Explores the ESC-50 dataset and selects the sound categories used in the project.

### 02 — Audio Loading

Loads local WAV files and examines:

* Sampling rate
* Number of samples
* Duration
* Waveform

### 03 — Pretrained Model

Loads the pretrained AST model and performs audio classification inference.

The audio is converted to:

```text
16,000 Hz
Mono
```

before being passed to the model.

### 04 — Results Analysis

Compares actual ESC-50 categories with the model's predicted AudioSet labels and analyzes prediction confidence.

---

## 📊 Example Results

Example predictions from the experiment:

| Actual Sound | Model Prediction | Confidence |
| ------------ | ---------------- | ---------: |
| Dog          | Bark             |     18.76% |
| Thunderstorm | Thunder          |     54.91% |
| Clapping     | Clapping         |     79.10% |
| Clapping     | Applause         |     90.14% |
| Thunderstorm | Thunder          |     48.75% |
| Clapping     | Clapping         |     43.92% |
| Church Bells | Church bell      |     71.36% |
| Footsteps    | Clapping         |     19.01% |
| Footsteps    | Fireworks        |     56.32% |
| Footsteps    | Walk, footsteps  |     46.65% |

Mean confidence across these 10 example predictions:

**52.89%**

---

## ⚠️ Important Evaluation Note

The ESC-50 dataset and the pretrained model do not use exactly the same label system.

ESC-50 contains categories such as:

```text
dog
thunderstorm
clapping
footsteps
```

while the pretrained AudioSet model can produce labels such as:

```text
Bark
Thunder
Clapping
Applause
Walk, footsteps
```

Because of this difference, standard accuracy or F1-score should not be calculated directly by comparing the two label names.

Instead, this project focuses on:

* Qualitative prediction analysis
* Prediction confidence
* Similarity between the actual sound and predicted sound category
* Understanding pretrained model limitations

---

## 📈 Confidence Analysis

The prediction confidence varies considerably between audio samples.

The experiment produced confidence values ranging from approximately:

**18.76% → 90.14%**

This demonstrates that a pretrained model can be highly confident for some sounds while being uncertain or incorrect for others.

The confidence visualization is available in:

```text
results/prediction_confidence.png
```

---

## 🛠️ Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* Librosa
* SoundFile
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Jupyter Notebook

---

## 💻 Hardware-Friendly Approach

This project was intentionally designed as a **small Audio AI learning project**.

It does not include:

* Training a large neural network
* Fine-tuning
* GPU requirements
* Large-scale audio processing
* Web application/UI
* Model deployment

The pretrained model is downloaded from Hugging Face and used only for inference.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Audio-Environmental-Classification
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the notebooks

Open the project in VS Code or Jupyter Notebook and run the notebooks in order:

```text
01_dataset_exploration.ipynb
02_audio_loading.ipynb
03_pretrained_model.ipynb
04_results_analysis.ipynb
```

---

## 📚 Dataset

The project uses **ESC-50**, a dataset of environmental sounds.

Only a small subset of the dataset was used for this project.

The original dataset is not included in the repository.

---

## 🤗 Pretrained Model

The pretrained model is available through Hugging Face:

`MIT/ast-finetuned-audioset-10-10-0.4593`

The model is downloaded automatically when the inference notebook is executed.

---

## 🔮 Possible Future Improvements

If this project is extended in the future, possible improvements include:

* Mapping ESC-50 labels to AudioSet labels
* Testing more audio samples
* Comparing multiple pretrained audio models
* Fine-tuning a lightweight model on ESC-50
* Adding more detailed evaluation metrics
* Exploring speech and sound-event classification

---

## 👩‍💻 Author

**Hirushi Fernando**

Computer Science Graduate | AI & Machine Learning Enthusiast

---

## ⭐ Project Purpose

This project was created as a practical introduction to **Audio AI**, focusing on how pretrained models can be used for audio classification without requiring expensive training infrastructure.

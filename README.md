# Run DH_live on Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuralFalconYT/DH_Live_Colab/blob/main/DH_live-Colab.ipynb)<br>
![a](https://github.com/user-attachments/assets/aa310fd4-4e30-4112-9443-3dd6ac4ce284)


### **1. Installation with Virtual Environment**

#### **Step 1: Clone the repository**
```bash
git clone https://github.com/NeuralFalconYT/DH_live.git
```

#### **Step 2: Change directory to the project folder**
```bash
cd DH_live
```

#### **Step 3: Create a virtual environment**
```bash
python -m venv myenv
```

#### **Step 4: Activate the virtual environment**

**For Windows:**
```bash
myenv\Scripts\activate
```

**For Linux:**
```bash
source myenv/bin/activate
```

#### **Step 5: Install the dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 6: Find your CUDA version**

- For Example CUDA 11.8, run:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```
(You can adjust the version if you have a different CUDA version)

#### **Step 7: Run the app in debug mode**
```bash
python app.py --debug
```

---

### **2. Installation without Using a Virtual Environment**

#### **Step 1: Clone the repository**
```bash
git clone https://github.com/NeuralFalconYT/DH_live.git
```

#### **Step 2: Change directory to the project folder**
```bash
cd DH_live
```

#### **Step 3: Install the dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 4: Find your CUDA version**
[If you already have PyTorch installed, skip Step 4.]
- For Example CUDA 11.8, run:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```
(You can adjust the version based on your CUDA setup)

#### **Step 5: Run the app in debug mode**
```bash
python app.py --debug
```
## Credit:
[DH_live](https://github.com/kleinlee/DH_live)

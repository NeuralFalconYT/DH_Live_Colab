# Run DH_live on Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuralFalconYT/DH_Live_Colab/blob/main/DH_live_Colab.ipynb)<br>
![a](https://github.com/user-attachments/assets/aa310fd4-4e30-4112-9443-3dd6ac4ce284)

# Windows Installation
```
git clone https://github.com/NeuralFalconYT/DH_live.git
```
or git clone https://github.com/kleinlee/DH_live.git

```
cd DH_live
```
```
curl -L -o app.py https://raw.githubusercontent.com/NeuralFalconYT/DH_Live_Colab/refs/heads/main/app.py
```
```
curl -L -o make_model.py https://raw.githubusercontent.com/NeuralFalconYT/DH_Live_Colab/refs/heads/main/make_model.py
```
```
curl -L -o colab_requirements.txt https://raw.githubusercontent.com/NeuralFalconYT/DH_Live_Colab/refs/heads/main/colab_requirements.txt
```

```
python make_model.py
```
```
pip install -r colab_requirements.txt
```
```
python app.py --debug
```

## Credit:
[DH_live](https://github.com/kleinlee/DH_live)

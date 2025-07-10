# séparateur_voix 🎵

Un petit script Python pour séparer la voix d’une piste audio, basé sur la librairie [Spleeter](https://github.com/deezer/spleeter).

---

## 🛠️ Installation

### 1. Installer [Anaconda](https://www.anaconda.com/) (si ce n’est pas déjà fait)

### 2. Créer ou activer l’environnement `spleeter_env`

```bash
conda activate spleeter_env
```

### 3. Installer les dépendances (si ce n’est pas déjà fait)

```bash
pip install spleeter
```

---

## ▶️ Utilisation

Placez votre fichier `.mp3` ou `.wav` dans le même dossier que `isoler_voix.py`, puis exécutez :

```bash
python isoler_voix.py
```

Les fichiers audio séparés (voix et instrumental) seront générés dans un sous-dossier.

---

## 📄 Fichier principal

- `isoler_voix.py` : script principal utilisant la librairie Spleeter pour isoler les pistes vocales.

---

## 📦 Dépendances

- `spleeter`

Si nécessaire, installez toutes les dépendances via :

```bash
pip install -r requirements.txt
```

---

## 📁 Exemple d’arborescence

```
separateur_voix/
├── isoler_voix.py
├── requirements.txt
├── README.md
├── chanson.mp3
└── audio_separated/
    └── chanson/
        ├── vocals.wav
        └── accompaniment.wav
```

---

## 📬 Contact

Développé dans le cadre d’un projet personnel d'exploration audio avec Spleeter.

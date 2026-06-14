<div align="center">

# 🩺 Sanjivani — Diabetes Predictor

### *Early Detection. Smarter Health.*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://sanjivani-diabetes-predictor-an6yfh5zfnx55h9rqybtjx.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-surajrajput999-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/surajrajput999)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Suraj_Bhan_Pratap_Singh-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/suraj-bhan-pratap-singh-891727293/)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)

</div>

---

## 📌 About The Project

**Sanjivani** is an AI-powered Diabetes Prediction Web App built using Machine Learning and deployed via Streamlit. The name *Sanjivani* — inspired by the legendary life-saving herb from Hindu mythology — reflects the project's mission: **early detection to save lives**.

Users can input key health parameters and get an instant prediction on whether they are at risk of diabetes — helping in proactive health management.

> 🎯 Goal: Make early diabetes screening accessible, fast, and accurate for everyone.

---

## 🌐 Live Demo

🔗 **[Click here to try the app](https://sanjivani-diabetes-predictor-an6yfh5zfnx55h9rqybtjx.streamlit.app/)**

---

## ✨ Features

- 🔮 **Instant Prediction** — Get diabetes risk result in seconds
- 📊 **Interactive UI** — Clean, user-friendly Streamlit interface
- 🧠 **ML-Powered** — Trained on the Pima Indians Diabetes Dataset (Kaggle)
- 📱 **Responsive Design** — Works on desktop and mobile browsers
- ⚡ **Fast & Lightweight** — No heavy setup required — runs directly in browser

---

## 🧪 Input Parameters

The model takes the following health indicators as input:

| Parameter | Description |
|---|---|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skin fold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body mass index (weight in kg/(height in m)²) |
| Diabetes Pedigree Function | Genetic diabetes likelihood score |
| Age | Age in years |

---
screenshots/Screenshot 2026-06-14 143530.png

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.x |
| **ML Library** | Scikit-Learn |
| **Data Processing** | Pandas, NumPy |
| **Web Framework** | Streamlit |
| **Deployment** | Streamlit Cloud |
| **Dataset** | Pima Indians Diabetes Dataset (Kaggle / UCI) |

---

## 🚀 Run Locally

### Prerequisites
- Python 3.7+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/surajrajput999/Sanjivani-Diabetes-Predictor.git

# 2. Navigate into the project directory
cd Sanjivani-Diabetes-Predictor

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser. 🎉

---

## 📂 Project Structure

```
Sanjivani-Diabetes-Predictor/
│
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained ML model (pickled)
├── diabetes.csv            # Dataset (Pima Indians Diabetes)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| Algorithm | (e.g., Logistic Regression / SVM / Random Forest) |
| Accuracy | ~78–85% |
| Dataset | Pima Indians Diabetes Dataset |
| Train/Test Split | 80% / 20% |

> ℹ️ Update the exact accuracy and algorithm based on your actual model results.

---

## 📊 Dataset

- **Source:** [Kaggle — Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Records:** 768 samples
- **Features:** 8 health indicators + 1 target column (Outcome: 0 or 1)
- **Origin:** National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK), USA

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the repo
2. Create your branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📬 Connect With Me

<div align="center">

| Platform | Link |
|---|---|
| 💼 LinkedIn | [Suraj Bhan Pratap Singh](https://www.linkedin.com/in/suraj-bhan-pratap-singh-891727293/) |
| 🐙 GitHub | [surajrajput999](https://github.com/surajrajput999) |
| 🚀 Live App | [Sanjivani on Streamlit](https://sanjivani-diabetes-predictor-an6yfh5zfnx55h9rqybtjx.streamlit.app/) |

</div>

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ by **Suraj Bhan Pratap Singh**

*"Prevention is better than cure — Sanjivani helps you stay ahead."*

⭐ **If you found this helpful, please give a star to the repo!** ⭐

</div>

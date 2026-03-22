**House Price Prediction System**

**Overview**

This project is a **Machine Learning-based House Price Prediction System** built using **FastAPI (backend)** and **Streamlit (frontend)**.
It allows users to input property details and get predicted house prices in real-time.

---

##  Key Features

* 📊 Predict house prices using trained ML model
* ⚡ FastAPI for high-performance backend API
* 🎨 Streamlit for interactive user interface
* 🔗 API integration between frontend & backend
* 🐳 Docker support for easy deployment

---

##  Tech Stack

* **Programming Language:** Python
* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Machine Learning:** Scikit-learn / Pandas / NumPy
* **Deployment:** Docker
* **Version Control:** Git & GitHub

---

##  Project Structure

```
Project/
│── api.py              # FastAPI backend
│── rent.py             # Streamlit frontend
│── house_rent.pkl      # Trained ML model
│── Dockerfile          # Container setup
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

---

##  How It Works

1. User enters house details in Streamlit UI
2. Streamlit sends request to FastAPI
3. FastAPI loads ML model and predicts price
4. Result is returned and displayed on UI

---

## Run Locally

### 1️ Clone Repository

```bash
git clone https://github.com/Deepaksaini40044/House-Price-Prediction.git
cd House-Price-Prediction
```

---

### 2️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️ Run FastAPI Server

```bash
uvicorn api:app --reload
```

---

### 4️ Run Streamlit App

```bash
streamlit run rent.py
```

---

## Run with Docker

### Build Image

```bash
docker build -t house-price-app .
```

### Run Container

```bash
docker run -p 8000:8000 house-price-app
```

---

##  Screenshots (Add Yours)

* UI Screenshot
* Prediction Output
* API Response

---

##  Future Improvements

* Add more features for better prediction accuracy
* Deploy on cloud (AWS / Render / Streamlit Cloud)
* Add user authentication
* Improve UI/UX

---

##  Author

**Deepak Saini**

* Data Analyst | ML Enthusiast
* Skilled in Python, SQL, Power BI, Machine Learning, Docker, FastAPI,AdvanceExcel, PowerBI, Statistics

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

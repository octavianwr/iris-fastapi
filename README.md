# Iris Prediction API

A simple FastAPI-based application for predicting Iris species using a trained Random Forest model. This project demonstrates how to train a machine learning model and deploy it as an API.

## Features
- Predict Iris species (`setosa`, `versicolor`, `virginica`) based on sepal and petal dimensions.
- FastAPI framework for API endpoints.
- Dockerized for deployment.

---

## File Structure
- `app/main.py`: FastAPI application with endpoints.
- `app/iris_model.pkl`: Pre-trained Iris model (Random Forest).
- `notebooks/train_model.ipynb`: Jupyter Notebook for training the model.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker configuration.

---

## Installation and Usage

### Prerequisites
- Python 3.8+
- pip
- Docker (optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/iris-fastapi.git
   cd iris-fastapi
   ```

2. Install dependencies:
    ```bash
    pip install -r app/requirements.txt
    ```

3. Run the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```

4. Run the FastAPI application:
- Open http://127.0.0.1:8000/docs

## Docker Deployment
1. Build the Docker image
    ```bash
    docker build -t iris-fastapi .
    ```

2. Run the Docker container
    ```bash
    docker run -d -p 8000:8000 iris-fastapi
    ```

## Endpoints
- `GET /`
    - Health check for the API
- `POST /predict/`
    - Input: JSON object with sepal and petal dimensions.
    - Output: Predicted Iris species.

### Example input:

```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

### Example output:

```json
{
    "species": "setosa"
}
```

## Contact

For questions, contact octavian.wr@gmail.com.
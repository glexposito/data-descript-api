# Data Descript API

The **Data Descript API** allows users to calculate basic descriptive statistics such as mean, median, variance, standard deviation, minimum and maximum values, range, and quartiles. This is primarily a proof of concept to experiment with FastAPI.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Endpoints](#endpoints)
5. [Usage Examples](#usage-examples)

## Requirements

The **Data Descript API** is built using Python and the FastAPI framework. Ensure you have Python 3.7 or higher installed on your system.

### Common requirements:

- **Programming languages and runtimes:**
  - [Python 3](https://www.python.org/downloads/) (&ge; 3.7)
- **Python packages:**
  - FastAPI
  - uvicorn
  - pydantic
  - numpy

You can install these packages using the `requirements.txt` file provided in the repository.

## Installation

You can install the **Data Descript API** by cloning the repository or downloading the latest release.

**Cloning the Repository:**

```bash
git clone https://github.com/glexposito/data-descript-api
cd data-descript-api
```

**Installing Dependencies:**

```bash
pip install -r requirements.txt
```

## Configuration

To configure the **Data Descript API** on your local system, follow these steps:

1. Clone the repository as shown in the [Installation](#installation) section.
2. Install the necessary dependencies.
3. Run the API:

```bash
fastapi dev main.py   
```

This will start the API on `http://127.0.0.1:8000`.

## Endpoints

The **Data Descript API** provides the following endpoint:

### Descriptive Statistics

Calculate basic descriptive statistics for your data set:

- **Endpoint:** `/descriptive`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
      "data": [1.0, 2.0, 3.0, 4.0, 5.0]
  }
  ```

- **Response:**

  ```json
  {
      "mean": 3.0,
      "median": 3.0,
      "variance": 2.5,
      "standard_deviation": 1.5811388300841898,
      "min": 1.0,
      "max": 5.0,
      "range": 4.0,
      "q1": 2.0,
      "q2": 3.0,
      "q3": 4.0
  }
  ```

## Usage Examples

Below are some examples of how to use the **Data Descript API**.

### Example 1: Using `curl`

You can use `curl` to send a POST request to the `/descriptive` endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/descriptive" -H "Content-Type: application/json" -d '{"data": [1.0, 2.0, 3.0, 4.0, 5.0]}'
```

### Example 2: Using Python `requests` library

Here's an example of how to use the Python `requests` library to interact with the API:

```python
import requests

url = "http://127.0.0.1:8000/descriptive"
data = {
    "data": [1.0, 2.0, 3.0, 4.0, 5.0]
}

response = requests.post(url, json=data)
print(response.json())
```

### Example 3: Using JavaScript `fetch` API

You can also use the `fetch` API in JavaScript to send data to the endpoint:

```javascript
fetch('http://127.0.0.1:8000/descriptive', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({data: [1.0, 2.0, 3.0, 4.0, 5.0]})
})
.then(response => response.json())
.then(data => console.log(data));
```

# Weather App

A simple, user-friendly weather application that fetches real-time weather data from an API and displays it in a clean and intuitive interface.

## Project Overview

The Weather App is built to provide real-time weather updates for cities worldwide. Users can search for their desired location and view details like temperature, weather condition, and other relevant information.

---

## Project Structure

The project is organized as follows:

```plaintext
weather_app/
├── static/
│   └── styles.css           # Styling for the web pages        
├── templates/      
│   └── index.html           # Homepage template and display weather results
├── .gitignore               # Preventing files or folders from being tracked in a repository.                 
├── app.py                   # Main Python application file
├── requirements.txt         # Dependencies for the project
└── README.md                # Project documentation
```


### Key Components:
- **`static/`**: Contains static assets like CSS for styling.
- **`templates/`**: Holds HTML files used for rendering web pages.
- **`app.py`**: Implements the backend logic, API calls, and web routing.
- **`requirements.txt`**: Specifies the Python dependencies required to run the app.
- **`README.md`**: Provides an overview, usage, and setup instructions for the project.

---

## Features

- **Real-Time Weather Data**: Fetches up-to-date weather details for any location.
- **Search Functionality**: Users can search by city name.
- **Minimal and Responsive UI**: Simple design for an easy user experience.

---

## Technologies Used

### Backend:
- **Python**: Core logic and server-side operations.
- **Flask**: Web framework for routing and API handling.

### Frontend:
- **HTML/CSS**: Provides structure and styling to the user interface.

---

## Setup and Installation

Follow these steps to set up and run the Weather App on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abuawaish/weather_app.git
   cd weather_app
   ```

2. **Install Python Dependencies: Ensure you have Python installed. Then, install the dependencies using:**
    ```bash
    pip install -r requirements.txt
   ```
   
3. **Run the Application: Start the Flask server by running:**
    ```bash
   python app.py
    ```
### License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
# Stock Options Data Viewer

## Introduction
This is a python tool designed to help users analyze and visualize stock options data efficiently. This application integrates with the Alpha Vantage API to provide real-time financial data.

I chose to submit this project to demonstrate good object-oriented programming practices, as well as my skills in data scraping, ingestion, and visualization. For the first iteration of the project, I focused on displaying the data in a tabular format, which is implemented in views/stock_table_view.py. This approach allowed me to lay a strong foundation for presenting the data effectively and incrementally build toward more advanced visualizations, such as a line chart.

## Future Improvements
I would implement a database such as postgres or mongodb to store all of the queried stock data to improve the performance. Another future upgrade would be implementing a web application using flask and dash frameworks.



## Features
- View detailed stock options data.
- Easy-to-use interface for financial analysis.
- Integration with Alpha Vantage API for real-time data.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/duderrick/StockOptions.git
   ```

2. Install Python

Ensure Python 3.11.9 or later is installed on your system.

3. Go into cloned repository

   ```bash
   cd StockOptions
   ```

4. Create a python virtual environment

Replace <YOUR VIRTUAL ENV NAME> with your desired virtual environment name:
    ```bash
    python -m venv <YOUR VIRTUAL ENV NAME>
    ```
   
5. Activate the Virtual Environment

   If your virtual environment is installed at /home/users/user1/venvs/my_qt_env, activate it using:
   ```bash 
   source /home/users/user1/venvs/my_qt_env/bin/activate
   ```

6. Install Dependencies

    a. Navigate to the cloned repository:
    ```bash
    cd <REPO_DIRECTORY>
    ```
   
    b. Install the required Python packages
    ```bash
    pip install -r requirements.txt
    ```

7. Register for an API key

    a. Register for an API key here: https://www.alphavantage.co/support/#api-key

    b. Replace the variable API_KEY in /util/commons.py with the API key you just got

8. Run the application

    a. Configure your PYTHONPATH to include the root of the cloned source code.

    b. Run the application:
    ```bash
    python main.py
    ```
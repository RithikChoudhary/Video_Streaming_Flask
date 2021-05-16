# Video Streaming Flask

## Introduction

This is a simple script to livestream a feed onto localhost using simple, easily installable and freely available modules.

The Tech Stack is very simple. It is as below. 

| Modules | MIN | MAX | USAGE |
| -------------- | :------: | :------: | :------------: |
| Python | 3.5 | 3.9 | base - code | 
| flask | 2.0.0 | + | web server |
| opencv-python | 4.5.1.45 | 4.5.1.48 | capture video  |
| pyautogui | 0.9.52 | + | capture screen |

## How To Run

### ( I ) Create a Virtual Environment
1. We use python's builting venv functionality:
    ```bash
    python -m venv myenv
    ```

2. Activate the Environment:
    * On Windows
        ```powershell
        $ .\myenv\Scripts\activate
        ```
    * On Linux
        ```bash
        $ source venv/bin/activate
        ```

3. Then install the dependencies:
    ```bash
    (myenv) $ pip install -r requirements.txt
    ```

### ( II ) Run the app
The app can be run by simply running te app.py file using python interpreter:

```bash
(myenv) $ python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
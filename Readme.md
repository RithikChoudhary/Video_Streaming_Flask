# FlaskIntroduction

This repo has been updated to work with `Python v3.8` and up.

### How To Run
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

4. Finally start the web server:
    ```bash
    (myenv) $ python app.py
    ```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

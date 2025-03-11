# End TO END MACHINE LEARNING PROJECT #

### Creating environment using terminal
conda create -p venv-project python==3.8 -y
conda activate venv-project

### Create setup.py & requirement.txt
setup.py is the configuration file for packaging a Python project.

Why is it needed?
 1> Without setup.py, you cannot install your project as a package.
 2> If you're creating a machine learning or software project that others will install, setup.py is necessary.

What Does setup.py Do?
 1> Defines package name, version, and author.
 2> Includes dependencies (install_requires).
 3> Finds all sub-packages (find_packages()).  packages >> sub-packages >> collection of modules >> module >> sinlge python file >> functions, classes, variables.
 4> Makes the project pip-installable.

❌ Without setup.py, You Must:
 1. Copy files manually to use them in another project.
 2. Set PYTHONPATH manually to access packages.
 3. Install dependencies manually using pip install -r requirements.txt.
 4. Remember all dependencies when sharing the project.

📌 What Do You Mean by "Manually Importing the Module"?
 1. By default, Python only looks for modules in certain directories (like the current folder, installed packages, and system paths).
 2. If your custom module (Python script or package) is outside these directories, Python won’t find it, and you will get an ImportError or ModuleNotFoundError.

### Create exception.py
1. The Python sys module is imported to access sys.exc_info(), which retrieves details about the most recent exception.
2. When an exception occurs, sys.exc_info() provides three pieces of information:
   _: Exception type (not used here).
   _: Exception value (not used here).
   exc_tb: A traceback object containing details about where the exception occurred.
3. The exc_tb traceback object helps extract:
   The filename where the error occurred.
   The line number where the error occurred.
   The actual error message.
4. The CustomExecption class is used to raise a structured exception message, making debugging easier.

### Create logger.py
❓Why Configure Logging?

😲By default, Python logs only to the console (stdout). We use logging.basicConfig() to: 
   1. ✅ Save logs to a file instead of just printing to the console.
   2. ✅ Define a clear log format for better debugging.
   3. ✅ Set the log level (INFO, WARNING, ERROR, etc.). If you want both WARNING and INFO logs, you need to set level=logging.INFO instead of level=logging.WARNING. INFO logs INFO, WARNING, ERROR, and CRITICAL messages.

### 




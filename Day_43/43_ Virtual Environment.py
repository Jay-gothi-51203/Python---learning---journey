# Topic: Virtual Environment 

# Virtual Environment: A virtual environment is a safe space for each Python project to use its own tools without breaking other projects.

# Imagine This:
# You are working on two school projects:
# Project A needs a pencil.
# Project B needs a pen.
# But if you put both tools in the same box, it gets messy. You might lose the pen or mix them up.


# So What Do You Do?
# You create two boxes:
# One box only for Project A (with pencil).
# One box only for Project B (with pen).
# Now each project is safe and has only what it needs.


# In Python:
# A project is your Python app or script.
# A box is a virtual environment.
# The tools (pen/pencil) are Python packages (like numpy, pandas, etc).


# Why Use Virtual Environments?
# Because different projects often need different tools (or versions of tools). If you mix them all up, Python gets confused.


# Very Simple Steps (How to Use It):
# Let’s say you’re starting a new Python project:
# 1.) Open your terminal (Command Prompt or PowerShell or Terminal).
# 2.) Go to the folder of your project.

# 3.) Type this command:
# python -m venv myenv (This creates a virtual environment called myenv.)

# 4.) Turn it on (activate it):
# source myenv/bin/activate (✅ Now you’re inside the virtual environment!)

# 5.) Install any packages you want just for this project:
#  pip install pandas

# 6.) When you're done, just type:
# deactivate (You’re back to your normal system.)




# Load modules
module load gcc python

# Create the virtual environment
virtualenv --system-site-packages /opt/`hostname`/venv-gcc

# Activate the virtual environment
source /opt/`hostname`/venv-gcc/bin/activate

# Install scipy
pip install scipy

# Deactivate the environment when done
deactivate

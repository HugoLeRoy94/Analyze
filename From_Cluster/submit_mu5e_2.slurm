#!/bin/bash
#SBATCH --job-name=Mu5E_2_job
#SBATCH --output=Mu5E_2_output_%j.txt
#SBATCH --error=Mu5E_2_error_%j.txt
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=1G

# Load the module
module load gcc python

# Activate the virtual environment
source /home/hcleroy/venvs/base/bin/activate

# Run your Python script
srun python mu5e_2.py

deactivate

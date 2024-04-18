#!/bin/bash
#SBATCH --job-name=Mu5E_2_job
#SBATCH --output=Mu5E_2_output_%j.txt
#SBATCH --error=Mu5E_2_error_%j.txt
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=1G

module load python3 

srun python Mu5E_2.py


# Auto Multiple-Choice Grading System

This project is an automated grading system for multiple-choice exams using images, utilizing OpenCV for image processing. This guide will walk you through setting up and running the project within a Conda environment.

## Setup Instructions

### 1. Clone the Repository
First, clone the repository (or download the code) to your local machine:
```bash
git clone (https://github.com/LongB260/Auto-Multiple-Choice-Grading)
cd auto-multiple-choice-grading
```

### 2. Create and Activate Conda Environment
Create a Conda environment for the project with the necessary dependencies:

```bash
conda create -n grading_env python=3.10
conda activate grading_env
```

### 3. Install Dependencies
Install the required Python libraries within the environment:

```bash
conda install -c conda-forge opencv
conda install -c conda-forge imutils numpy
```

### 4. Configure the Image Directory
Update the `folder_path` variable in the code to point to the directory containing your test images:
```python
folder_path = r'path_to_your_image_folder'
```

### 5. Run the Code
With the environment activated and `folder_path` configured, you can now run the grading code:

```bash
python main.py
```

This will process each image in the specified directory, grade it, and save the results.

## Viewing Results

- **Score Output**: A CSV file named `score.csv` will be generated in the project directory, recording scores for each graded image.
- **Graded Images**: Each graded image will be saved in the specified folder with the prefix `images`.
  
## Closing Notes

To deactivate the environment once you’re finished:
```bash
conda deactivate
```

### Additional Tips
- Ensure that your images are correctly formatted and of sufficient quality for accurate grading.
- Run `conda env list` to verify that `grading_env` is available after setup.

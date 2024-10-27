Summary: The process from finding contours to determining answer positions in the code begins with detecting contours in the edge-processed image and filtering for the contour with four points to identify the test area. Next, the image is transformed to a bird's eye view for easier processing. The image is then thresholded to create a binary image, allowing for the identification and storage of contours corresponding to appropriately sized answer choices. These contours are sorted top to bottom and analyzed to find which bubble is marked the most. Finally, the code compares the selected bubble to the correct answer and calculates the score based on the accuracy of the responses.
1. Create a New Environment (Optional)
While not mandatory, it's a good practice to create a new environment to keep dependencies isolated:
conda create -n grading-env python=3.8
Then activate the environment:
conda activate grading-env

2. Install Required Packages
Install the necessary libraries using pip or conda:
conda install -c conda-forge opencv imutils numpy pandas
pip install pytesseract

3. Install Tesseract OCR
If you’re using pytesseract, you also need to install Tesseract OCR. Download and install it from the Tesseract GitHub page and add the path to your system's PATH environment variable.

4. Create a Python File
Open a code editor (such as VSCode or Jupyter Notebook) and paste the code into a Python file (e.g., grading.py).

5. Run the Code
Execute the script using the following command in your terminal:
python main.py

6. Check Results
After running the code, check the folder containing the images to see if the results have been saved.

# image_2_pdf
Convert a list of numbered images (jpg and png tested) into a PDF(s).

This will group images by number prefix 001-009 into one pdf suffixed with 00. e.g. numbers 090-099 into name_09.pdf 

Prerequisite: run setup.sh to create virtual environment with pillow installed

1. Set dir variable to be the path to the directory containing images
  1a. Images must be numbered e.g. 001.jpg, 002-01.jpg, 002-02.jpg, or 909-01-01-filename.jpg (also works with png)
  1b. Numbers must be at least double digits. e.g. 01.jpg. -- 1.jpg will not work without amending the code
  
2. Set the pdf_name variable. e.g. "comic_" this will create PDFs named "comic_01.pdf", "comic_02.pdf"
3. Set the low_power_variable to True or False. I had some issues with my machine locking up when ran on a loop. 
  3a. low_power_mode will limit the process to 1 pdf. Just run it again to do the next one and so on.    

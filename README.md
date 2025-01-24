# Survey-Feedback-Analysis-Tool-

This project provides a tool for analyzing sentiment in survey feedback. It uses Natural Language Processing (NLP) to process and evaluate the sentiment of textual feedback from surveys. The tool generates a sentiment report, including the sentiment breakdown (positive, neutral, negative) and an overall sentiment score.

Features
Sentiment Analysis: Analyzes text to identify positive, neutral, and negative sentiments.
Word Cloud: Visualizes the most common words in the feedback.
Feedback Data Handling: Supports CSV and Excel formats for survey data.
Save Results: Saves the sentiment analysis results to a new Excel file.
Requirements
Python 3.x
nltk library for sentiment analysis
wordcloud for generating a word cloud
pandas for data manipulation
matplotlib for plotting the word cloud
openpyxl for reading Excel files
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/survey-sentiment-analysis.git
Navigate to the project folder:

bash
Copy
Edit
cd survey-sentiment-analysis
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Or manually install the required packages:

bash
Copy
Edit
pip install nltk wordcloud pandas matplotlib openpyxl
Usage
Download Survey Feedback: Prepare your survey feedback data in CSV or Excel format. Ensure the feedback is in a column with textual responses.

Run the Tool: After installing the dependencies, run the script:

bash
Copy
Edit
python survey_feedback_tool.py
Input File Path: Enter the path to your survey data when prompted. Ensure that the file is either in CSV or Excel format.

Column Name for Feedback: Specify the column name containing the feedback text.

View Results: The tool will:

Perform sentiment analysis on the feedback.
Generate a word cloud of common words in the feedback.
Output the sentiment results as a new Excel file.
Save the Results: Enter the desired name for the output file, and it will be saved with the sentiment analysis results.

Example Output
After running the script, the tool will analyze each feedback entry and output the following sentiment scores:

pos: Positive sentiment score (0 to 1)
neu: Neutral sentiment score (0 to 1)
neg: Negative sentiment score (0 to 1)
compound: Overall sentiment score (-1 to 1)
Example:
Feedback	Positive	Neutral	Negative	Compound
"I love this product!"	0.8	0.2	0.0	0.8
"It's okay, not great."	0.3	0.7	0.0	0.0
"I hate this!"	0.0	0.0	1.0	-0.8
Contributing
Feel free to fork this repository, submit pull requests, or open issues for any improvements or bugs.

How to Contribute:
Fork the repository
Clone your fork:
bash
Copy
Edit
git clone https://github.com/your-username/survey-sentiment-analysis.git
Make your changes in a branch.
Push to your fork and create a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.


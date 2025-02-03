# Survey-Feedback-Analysis-Tool-

This project incorporates a tool into analyzing sentiment for survey feedback using Natural Language Processing to process the textual feedback obtained from surveys by evaluating the feelings of the users. The sentiments are then mapped into a sentiment report, stating the breakdown by sentiment-positive, neutral, or negative-along with an average sentiment score for the overall content.

Features
Sentiment Analysis: It assesses text as positive, negative, and neutral sentiments.
Word Cloud: visualizes the frequently occurring words from the feedback.
Feedback Data Handling: It accepts the survey data in CSV or Excel format.
Save Results: Saves the sentiment analysis result into a new Excel file.
Prerequisites
Python 3.x
nltk library for Sentiment Analysis
wordcloud for word cloud
pandas for data manipulation
matplotlib for plotting word cloud
openpyxl to read excel files
Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/survey-sentiment-analysis.git
Move into project folder:

bash
Copy
Edit
cd survey-sentiment-analysis
Then install the needed dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Alternatively, install the required packages by manually:

bash
Copy
Edit
pip install nltk wordcloud pandas matplotlib openpyxl
Usage
Download Survey Feedback: Prepare your survey feedback data in CSV or Excel format. Ensure the feedback is in a column with textual responses.

Run the Tool: Run the script after installing dependencies:

bash
Copy
Edit
python survey-feedback-tool.py
Input File Path: Provide the path to your survey data when asked, making sure it's either in CSV or Excel format.

Column Name for Feedback: Identify column name that includes the feedback text.

View Results: The tool will:

Analyze the sentiment of the feedback
Create word cloud of common words in feedback
Output the results of sentiment as a new Excel file
Save the Results: Name the desired output file, and it will save with the sentiment analysis results.

Example Output
After execution, this tool will result in the sentiment scores of each feedback entry as shown below:

pos: Positive sentiment score (0 to 1)
neu: Neutral sentiment score (0 to 1)
neg: Negative sentiment score (0 to 1)
compound: Overall sentiment score (-1 to 1)
Example:
Feedback.Positive Neutral Negative Compound
"I love this product!" 0.8 0.2 0.0 0.8
"It's okay, not great." 0.3 0.7 0.0 0.0
"I hate this!" 0.0 0.0 1.0 -0.8
Contributing
Feel free to fork this repository, submit pull requests or open issues for any improvements or bugs.

How to Contribute:
Fork the repository
Clone your fork:
bash
Copy
Edit
git clone https://github.com/your-username/survey-sentiment-analysis.git
Create your changes in a branch.
Push to your fork and make a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.


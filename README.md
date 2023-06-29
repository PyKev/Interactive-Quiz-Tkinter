# Interactive Quiz with Tkinter

This project is a desktop application developed in Python using the Tkinter library. This program presents a series of questions to users and allows them to select the correct answer. Users also have the option to customize the questions, answer options, and images used in the quiz.

## Usage
- Run the Python code in a compatible development environment.

- A main window titled "Cuestionario" (Quiz) will appear with a welcome message.

- Click the "Empecemos!" (Let's Start!) button to begin the quiz.

- A new window will open with the first question and answer options.

- Select the answer option you believe is correct by clicking the corresponding button.

- If the answer is correct, an informative message will be displayed. Otherwise, an error message will be shown.

- Click the "Siguiente" (Next) button to advance to the next question.

- The process of presenting questions, selecting answers, and advancing continues until the quiz is completed.

- When the last question has been answered, the quiz windows and the main window will close.

## Customization
- To customize the questions, answer options, and images used in the quiz, you can modify the lists in the code.

- The questions are stored in the "questions" list. You can change the text of the questions by adding or modifying elements in this list.

- The answer options are stored in the "answer1", "answer2", and "answer3" lists. You can change the text of the answer options by adding or modifying elements in these lists.

- The images used in the quiz are stored in the "questions_images" list. You can replace the existing images with your own images by adding or modifying elements in this list. Make sure the images are located in the "images" folder or specify the path to the image folder as needed.

- By default, the correct answer is considered as the second answer option. If you want to change the correct answer to a different option, you can modify the code to reflect your preference.

## System Requirements
- Python 3.x
- Tkinter library
- PIL (Python Imaging Library) library

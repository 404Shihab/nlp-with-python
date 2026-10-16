from textblob import TextBlob

incorrect_text = 'Yesterday, I recieved an important mesage from my freind about our upcoming university examp. He told me that we should prepare carefuly because the questions might be dificult, and we need to submit our assingment before the deadline. I definately want to improve my writting skills and acheive good results in the final examination.'

textBlb = TextBlob(incorrect_text)

print(textBlb.correct().string)
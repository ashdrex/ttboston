// code by webdevtrick (https://webdevtrick.com)
function Quiz(questions) {
    this.score = 0;
    this.questions = questions;
    this.questionIndex = 0;
}
 
Quiz.prototype.getQuestionIndex = function() {
    return this.questions[this.questionIndex];
}
 
Quiz.prototype.guess = function(answer) {
    this.score = this.score + this.getQuestionIndex().isCorrectAnswer(answer)
    this.questionIndex++;
}
 
Quiz.prototype.isEnded = function() {
    return this.questionIndex === this.questions.length;
}
 
 
function Question(text, choices, answer) {
    this.text = text;
    this.choices = choices;
    this.answer = answer;
}
 
Question.prototype.isCorrectAnswer = function(choice) {
    if(this.answer[0] === choice) {
        return 3
    }
    if(this.answer[1] === choice) {
        return 2
    }
    if(this.answer[2] === choice) {
        return 1
    }
    if(this.answer[3] === choice) {
        return 0
    }
}
 
 
function populate() {
    if(quiz.isEnded()) {
        showScores();
    }
    else {
        // show question
        var element = document.getElementById("question");
        element.innerHTML = quiz.getQuestionIndex().text;
 
        // show options
        var choices = quiz.getQuestionIndex().choices;
        for(var i = 0; i < choices.length; i++) {
            var element = document.getElementById("choice" + i);
            element.innerHTML = choices[i];
            guess("btn" + i, choices[i]);
        }
 
        showProgress();
    }
};
 
function guess(id, guess) {
    var button = document.getElementById(id);
    button.onclick = function() {
        quiz.guess(guess);
        populate();
    }
};
 
 
function showProgress() {
    var currentQuestionNumber = quiz.questionIndex + 1;
    var element = document.getElementById("progress");
    element.innerHTML = "Question " + currentQuestionNumber + " of " + quiz.questions.length;
};
 
function showScores() {
    var gameOverHTML = "<h1>Result</h1>";
    gameOverHTML += "<h2 id='score'> Your scores: " + quiz.score + "</h2>";
    var element = document.getElementById("quiz");
    element.innerHTML = gameOverHTML;
};
 
// create questions here
var questions = [
    new Question("How many days a week do you eat meat?", ["Never", "1-2 times a week", "3-5 times a week", "Daily"], ["Never", "1-2 times a week", "3-5 times a week", "Daily"]),
    new Question("How often do you eat chicken?", ["Never", "1-2 times a week", "3-5 times a week", "Daily"], ["Never", "1-2 times a week", "3-5 times a week", "Daily"]),
    new Question("How often do you eat pork?", ["Never", "1-2 times a week", "3-5 times a week", "Daily"], ["Never", "1-2 times a week", "3-5 times a week", "Daily"]),
    new Question("How often do you eat lamb?", ["Never", "1-2 times a week", "3-5 times a week", "Daily"], ["Never", "1-2 times a week", "3-5 times a week", "Daily"]),
    new Question("How often do you eat fish?", ["Never", "1-2 times a week", "3-5 times a week", "Daily"], ["Never", "1-2 times a week", "3-5 times a week", "Daily"])
];
 
// create quiz
var quiz = new Quiz(questions);
 
// display quiz
populate();
def cheat(exercise_number):
    if exercise_number == 3.1.1:
        return "exam_grades <- rnorm(50, 7.5, 0.8)hist(exam_grades)"
    elif exercise_number == 3.1.2:
        return 
        "schipol_data<- read.csv('https://bit.ly/3GLVQ86')head(schipol_data)plot(schipol_data$DATE, schipol_data$TMAX)"
    elif exercise_number == 3.1.3:
        return "library(ggplot2)library(titanic)head(titanic_train)titanic_train$survival_factor <- factor(titanic_train$Survived, levels = c(0, 1), labels = c("Dead", "Alive"))ggplot(titanic_train, aes(x = Sex, y = 1, fill = survival_factor)) + geom_bar(stat = "identity") + labs(x = "Sex", y = "Count", fill = "How did it go?") +theme(legend.title = element_text(size = 12)) + theme_grey()"
    elif exercise_number == 3.1.9:
        return "library('ggstatsplot')?ggstatsplot ggbetweenstats(ToothGrowth, supp, len)"
    else:
        return "Sorry, I don't have a solution for that exercise"


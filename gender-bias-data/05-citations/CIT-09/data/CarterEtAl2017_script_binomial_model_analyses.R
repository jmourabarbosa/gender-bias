#detach(data)
data <- read.table("gender_questions_group.txt", header = T)
head(data)
attach(data)

library(lme4)

# create variable proportion of audience that is female:
data$propFemale_audience <- data$N_female/data$N_attendees
# centre at 0.50 (half audience is female):
data$propFemale_audience <- data$propFemale_audience - 0.5

# create variable proportion of department teaching staff that is female:
data$propDepartment <- data$F_faculty / (data$F_faculty + data$M_faculty)
# centre at 0.50 (half department is female):
data$propDepartment <- data$propDepartment - 0.5

# create variable proportion of questions asked by female audience members:
data$propQ <- data$F_question / (data$F_question + data$M_question)
# centre at 0.50 (half questions are from females female):
data$propQ <- data$propQ - 0.5

# create variable of the difference in the proportion of questions asked by women and the proportion of the audience that was women:
# (USED ONLY IN FIGURE 1)
data$Qbias <- data$propQ - data$propFemale

# create variable total number of questions asked:
data$totQ <- data$F_question + data$M_question
# remove talks with no questions:
data <- data[-which(data$totQ == 0),]
# is total number of questions correlated with the duration given to questions?
summary(glm(totQ ~ Q_dur, family = "poisson", data = data))
# centre total questions at median number of questions asked :
data$totQ <- data$totQ - median(data$totQ)

# create a non-centred duration variable for Q3 analyses:
data$Q_dur <- data$Q_duration
# centre time for questions at median duration :
data$Q_duration <- data$Q_duration - median(na.omit(data$Q_duration))

# create variable proportion of audience that is female (no longer used):
data$QFacBias <- data$propQ - data$propDepartment

# make speakerInternal variable numeric:
data$speakerInternal <- as.numeric(data$speakerInternal)

# DESCRIPTIVE STATISTICS:
# CURRENT CULTURE
# is there an effect of time of day on numbers of attendees?
quantile(N_attendees)
# will the log-link work for a Poisson glm?
hist(log(data$N_attendees))
# model the effect:
summary(glmer(data$N_attendees ~ data$startHour + (1|department/university), family = "poisson", data = data))

# GENDER DIFFERENCES
# is there a difference in men's and women's attendance?
data$propAudience <- data$N_female / data$N_attendees
t.test(data$propAudience, mu = 0.5)

# is there an imbalance in the gender of the speakers?
binom.test(table(data$speakerSex), 0.5)

# is there an effect of the time of day on the proportion of women attendees?
# are the proportion data normally-ish distributed?
hist(data$propFemale_audience)
summary(lmer(data$propFemale_audience ~ data$startHour + (1|department/university), data = data))


# test whether there is a bias i.e. is the audience proportion of women different to the proportion of questions asked by women:
t.test(data$propFemale_audience-data$propQ)

# Q2: why is there a bias? Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2
# FULL MODEL -- NOT USED
#summary(glmer(cbind(F_question, M_question) ~ propFemale_audience + First_question + Q_duration + N_attendees + speakerSex + propDepartment + speakerInternal + field + First_question:Q_duration + First_question:N_attendees + First_question:speakerSex + Q_duration:speakerSex + N_attendees:speakerSex + propFemale_audience:speakerSex + (1|country) + (1|department/university), data = data, family = "binomial"))

# MODEL: ALL DATA
# binomial model without predictor "first question" and its interactions:
# starting model:
summary(glmer(cbind(F_question, M_question) ~ propFemale_audience + totQ + N_attendees + speakerSex + propDepartment + speakerInternal + field + startHour + totQ:speakerSex + N_attendees:speakerSex + propFemale_audience:speakerSex + (1|country) + (1|department/university), data = data, family = "binomial"))

# final model
summary(glmer(cbind(F_question, M_question) ~ propFemale_audience + totQ + speakerSex + propDepartment + speakerInternal + (1|country) + (1|department/university), data = data, family = "binomial"))

# same with duration for questions? starting model:
summary(glmer(cbind(F_question, M_question) ~ propFemale_audience + Q_duration + N_attendees + speakerSex + propDepartment + speakerInternal + field + Q_duration:speakerSex + N_attendees:speakerSex + propFemale_audience:speakerSex + (1|country) + (1|department/university), data = data, family = "binomial"))

# final model
summary(glmer(cbind(F_question, M_question) ~ propFemale_audience + speakerSex + propDepartment + speakerInternal + (1|country) + (1|department/university), data = data, family = "binomial"))
# model with Q_duration
summary(glmer(cbind(F_question, M_question) ~ propFemale_audience + Q_duration + speakerSex + propDepartment + speakerInternal + (1|country) + (1|department/university), data = data, family = "binomial"))
# No. The duration of questions does not predict the proportion of questions asked by women as the number of questions does.

# what is the effect of speaker sex on the probability of a female question:
# final model (with total numbers of questions) named final.full
final.full <- glmer(cbind(F_question, M_question) ~ propFemale_audience + totQ + speakerSex + propDepartment + speakerInternal + (1|country) + (1|department/university), data = data, family = "binomial")

#------------------------------------------------------------------
# playing around with predicted values:
# the "best case" includes a 50% female audience, 10 questions, a male internal speaker and 50% of the faculty is female.
bestcase <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propFemale_audience"]*0 + fixef(final.full)["totQ"]*4 + fixef(final.full)["speakerSexM"]*1 + fixef(final.full)["propDepartment"]*0 + fixef(final.full)["speakerInternal"]*1
bestProp <- exp(bestcase) / (1 + exp(bestcase))
bestProp

# a more typical case, where the audience is 51% female, there are 6 questions, the speaker is male but external and the proportion of women factulty is 40%
typicalcase <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propFemale_audience"]*0.01 + fixef(final.full)["totQ"]*0 + fixef(final.full)["speakerSexM"]*1 + fixef(final.full)["propDepartment"]*-0.10 + fixef(final.full)["speakerInternal"]*0
typicalProp <- exp(typicalcase) / (1 + exp(typicalcase))
typicalProp
# 34% of questions are from women (which, unsurprisingly, matches the proportion of overall questions asked):
sum(data$F_question) / sum(data$F_question + data$M_question)
#------------------------------------------------------------------

# odds of a female question:
oddsR <- exp(fixef(final.full)["(Intercept)"])
# OR = 0.410581 => a question by a female is 59% less likely than a male question (when there are 6 questions)
# convert to a probability of a female question (when there are 0 questions)
Yhat <- exp(fixef(final.full)["(Intercept)"]) / (1 + exp(fixef(final.full)["(Intercept)"]))
Yhat
# (Intercept) 
# 0.2910722
# This is different to the proportion of overall questions asked by women (34%)--because of how the random effects are handled?

#create function inverse logit:
inverseLogit <- function(x){
	exp(x) / (1+exp(x))
}

# calculate the predicted values of the main effects in the base model
# EFFECT OF SPEAKER GENDER
# calculate the predicted value when the speaker is male:
YhatMaleSpeaker <- fixef(final.full)["(Intercept)"] + fixef(final.full)["speakerSexM"]*1
# predicted value when the speaker is female. NB: this is the base proportion and equals Yhat
YhatFemaleSpeaker <- fixef(final.full)["(Intercept)"] + fixef(final.full)["speakerSexM"]*0
# calculate the odds ratio:
oddsR <- exp(YhatMaleSpeaker)
# convert the predicted value into a percentage:
predPropM <- exp(YhatMaleSpeaker) / (1 + exp(YhatMaleSpeaker))
# convert the predicted value into a percentage using inverseLogit function defined earlier:
predPropM <- inverseLogit(YhatMaleSpeaker)
predPropF <- inverseLogit(YhatFemaleSpeaker)

# compare these predicted values to those from the "effects" package:
library(effects)

eff_speakerSex <- as.data.frame(effect("speakerSex", final.full))
eff_speakerSex
# NOT THE SAME as predPropM and predPropF (?) but similar difference between predicted values:
predPropM - predPropF
eff_speakerSex$fit[1] - eff_speakerSex$fit[2]

# EFFECT OF INTERNAL SPEAKER
# calculate the predicted value when the speaker is internal:
YhatInternalSpeaker <- fixef(final.full)["(Intercept)"] + fixef(final.full)["speakerInternal"]
oddsR <- exp(YhatInternalSpeaker)
# convert the predicted value into a percentage:
predProp <- inverseLogit(YhatInternalSpeaker)

# using effects package:
eff_speakerInt <- as.data.frame(effect("speakerInternal", final.full, xlevels = 2))
eff_speakerInt
# check the difference using the different methods:
predProp-Yhat
eff_speakerInt$fit[1] - eff_speakerInt$fit[2]

# EFFECT OF PROPORTION OF AUDIENCE
# calculate the predicted value when the audience is 50%, 55%, 60%, 45% and 40% female:
YhatAudience <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propFemale_audience"]*0.00
YhatAudience55 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propFemale_audience"]*0.05
YhatAudience60 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propFemale_audience"]*0.10
YhatAudience45 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propFemale_audience"]*-0.05
YhatAudience40 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propFemale_audience"]*-0.10

# convert the predicted value into a percentage and explore over a range:
predProp40 <- inverseLogit(YhatAudience40)
predProp45 <- inverseLogit(YhatAudience45)
predProp <- inverseLogit(YhatAudience)
predProp55 <- inverseLogit(YhatAudience55)
predProp60 <- inverseLogit(YhatAudience60)

# print values
predProp40
predProp45
predProp # equivalent to Yhat
predProp55
predProp60

# investigate "average" difference over middle range of values
predProp45-predProp40
predProp-predProp45
predProp55-predProp
predProp60-predProp55


# EFFECT OF PROPORTION OF FACULTY
# calculate the predicted value when the faculty is 50%, 55%, 60%, 45% and 40% female:
YhatFaculty <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propDepartment"]*0.00
YhatFaculty55 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propDepartment"]*0.05
YhatFaculty60 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propDepartment"]*0.10
YhatFaculty45 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propDepartment"]*-0.05
YhatFaculty40 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["propDepartment"]*-0.10

# convert the predicted value into a percentage over a range:
predFac40 <- inverseLogit(YhatFaculty40)
predFac45 <- inverseLogit(YhatFaculty45)
predFac <- inverseLogit(YhatFaculty)
predFac55 <- inverseLogit(YhatFaculty55)
predFac60 <- inverseLogit(YhatFaculty60)

# print the values:
predFac40
predFac45
predFac # equivalent to Yhat
predFac55
predFac60

# investigate "average" difference over middle range of values
predFac45-predFac40
predFac-predFac45
predFac55-predFac
predFac60-predFac55


# EFFECT OF NUMBER OF QUESTIONS
# calculate the predicted value when there are 2, 6, 10, and 15 questions:
YhatQuestions6 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["totQ"]*0
YhatQuestions2 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["totQ"]*-4
YhatQuestions10 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["totQ"]*4
YhatQuestions15 <- fixef(final.full)["(Intercept)"] + fixef(final.full)["totQ"]*9

# convert the predicted value into a percentage:
pred2Q <- inverseLogit(YhatQuestions2)
pred6Q <- inverseLogit(YhatQuestions6)
pred10Q <- inverseLogit(YhatQuestions10)
pred15Q <- inverseLogit(YhatQuestions15)

# print the values:
pred2Q
pred6Q
pred10Q
pred15Q

# what's the difference with more questions asked?
pred10Q-pred6Q
pred15Q-pred6Q


#___________________________________________________________________
# to avoid the predictor being confounded with the response
# remove first question from the analyses with first question
# first, get data where the first question is known
#data.1 <- data[-which(is.na(data$First_question)),]
data.1 <- data
head(data.1)

# remove a question from total M_questions if male first question:
data.1$M_q <- NA

for (i in 1:length(data.1[,1])){
	if (data.1$First_question[i] == "M") {
		data.1$M_q[i] <- data.1$M_question[i] - 1
	} else {
		data.1$M_q[i] <- data.1$M_question[i]
	}
}

# remove a question from total F_questions if female first question:
data.1$F_q <- NA

for (i in 1:length(data.1[,1])){
	if (data.1$First_question[i] == "F") {
		data.1$F_q[i] <- data.1$F_question[i] - 1
	} else {
		data.1$F_q[i] <- data.1$F_question[i]
	}
}

# check the data:
#data.1[,c("First_question", "M_question", "M_q")]
#data.1[,c("First_question", "F_question", "F_q")]

# create variable proportion of (subsequent) questions asked by female audience members less first question:
data.1$propQ <- data.1$F_q / (data.1$F_q + data.1$M_q)

# remove instances where there was only one question asked (the first question):
data.1$tot.Q <- data.1$F_q + data.1$M_q
data.1 <- data.1[which(data.1$tot.Q > 0),]
head(data.1)
#___________________________________________________________________

# re-run model with "reduced" data set:
# model WITHOUT first Q included in totals, but removing "first question" variable and it's interactions
summary(glmer(cbind(F_q, M_q) ~ propFemale_audience + First_question + totQ + N_attendees + speakerSex + propDepartment + speakerInternal + field + First_question:totQ + First_question:speakerSex + propFemale_audience:First_question + (1|country) + (1|department/university), data = data.1, family = "binomial"))

# minimal model
summary(glmer(cbind(F_q, M_q) ~ propFemale_audience + First_question + totQ + speakerSex + propDepartment + speakerInternal + (1|country) + (1|department/university), data = data.1, family = "binomial"))

summary(glmer(cbind(F_q, M_q) ~ propFemale_audience + First_question + totQ + speakerSex + propDepartment + speakerInternal + First_question:speakerSex + (1|country) + (1|department/university), data = data.1, family = "binomial"))

# similar results with total time for questions?
# starting model:
summary(glmer(cbind(F_q, M_q) ~ propFemale_audience + First_question + Q_duration + N_attendees + speakerSex + propDepartment + speakerInternal + field + First_question:Q_duration + First_question:speakerSex + propFemale_audience:First_question + (1|country) + (1|department/university), data = data.1, family = "binomial"))

summary(glmer(cbind(F_q, M_q) ~ propFemale_audience + First_question + Q_duration  + speakerSex + propDepartment + speakerInternal + (1|country) + (1|department/university), data = data.1, family = "binomial"))

final.reduced <- glmer(cbind(F_q, M_q) ~ propFemale_audience + First_question + totQ  + speakerSex + propDepartment + speakerInternal + (1|country) + (1|department/university), data = data.1, family = "binomial")

# EFFECT OF FIRST QUESTION
Yhat_reduced <- exp(fixef(final.reduced)["(Intercept)"]) / (1 + exp(fixef(final.reduced)["(Intercept)"]))

# calculate the predicted value when the first question is from a male:
YhatFirstQuestion <- fixef(final.reduced)["(Intercept)"] + fixef(final.reduced)["First_questionM"]
#YhatFirstQuestion <- fixef(final.reduced)["(Intercept)"] + fixef(final.reduced)["First_questionM"]*0
# convert the predicted value into a percentage:
predProp <- inverseLogit(YhatFirstQuestion)
predProp-Yhat_reduced



# Q3: what can be done?  Q3 Q3 Q3 Q3 Q3 Q3 Q3 Q3 Q3 Q3 Q3 Q3 Q3

# does the manipulation work?
experiment <- subset(data, experiment != "NaN")
experiment <- droplevels(experiment)

count <- rep(1,length(experiment[,1]))

# DID THE EXPERIMENT WORK?
summary(glm(Q_duration ~ as.factor(experiment) * department, data = experiment, family = "poisson"))

length(experiment[,1])
aggregate(Q_duration ~ experiment + department, data = experiment, FUN = "median")
aggregate(Q_duration ~ experiment + department, data = experiment, FUN = "mean")
aggregate(count ~ experiment + department, data = experiment, FUN = "sum")

# test whether phychology data worked...
psychology <- subset(experiment, department == "Psychology")
head(experiment)
# DID THE EXPERIMENT HAVE THE DESIRED OUTCOME?
summary(glm(cbind(F_question, M_question) ~ as.factor(experiment) * department, family = "binomial", data = experiment))
summary(glm(cbind(F_question, M_question) ~ as.factor(experiment), family = "binomial", data = experiment))


points(Qbias ~ jitter(experiment,1.2), data = experiment, pch = 16, col = Qcols)
summary(lm(Qbias ~ as.factor(experiment), data = psychology))
summary(lm(Q_duration ~ as.factor(experiment), data = psychology))


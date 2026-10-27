survey_data <- read.table("survey_data.txt", header = T)
names(survey_data)

# summary values:
table(survey_data$seminar_Attendance)
table(survey_data$freq_Ask_Questions)
table(survey_data$not_asked)
table(survey_data$time_for_questions)
table(survey_data$estimated_attendance)
table(survey_data$meet_speaker)
table(survey_data$culture_meeting_speaker)
table(survey_data$percentage_faculty_women)
table(survey_data$grad_students_women)
table(survey_data$gender)
table(survey_data$subject)
table(survey_data$career_stage)
table(survey_data$duration_career_stage)
table(survey_data$country)

# make a subset of the data that includes only people who identified as male or female
survey_data_gender <- droplevels(survey_data[ which(survey_data$gender == "Male" | survey_data$gender == "Female"),])
length(survey_data_gender[,1])

###
# do men and women differ in their attendance of seminars?
###
tbl.3 <- table(survey_data_gender$seminar_Attendance, survey_data_gender$gender)
chisq.test(tbl.3)

###
# is it easy to meet the speaker -- difference between men and women?
###
tbl.4 <- table(survey_data_gender$culture_meeting_speaker, survey_data_gender$gender)
chisq.test(tbl.4)



#####
## Q1: is there a perceived difference in males' and females' participation?
####
# do men and women differ in whether they always ask a question?
###
tbl.1 <- table(survey_data_gender$not_asked, survey_data_gender$gender)
chisq.test(tbl.1)

###
# do men and women differ in whether they think men ask more questions?
###
tbl.2 <- table(survey_data_gender$WHO_ASKS_gender, survey_data_gender$gender)
chisq.test(tbl.2)


# data set of people who sometimes don't ask questions when they have one:
stopped <- subset(survey_data_gender, not_asked == "yes")

#####
## Q2: why do respondents think there is a difference in males' and females' participation?
####
# do men and women differ in stopping asking questions because of...
tbl.20 <- table(stopped$DONT_ASK_not_enough_time, stopped$gender)
timeTest <- kruskal.test(stopped$DONT_ASK_not_enough_time, stopped$gender)

tbl.21 <- table(stopped$DONT_ASK_misunderstood, stopped$gender)
misunderstoodTest <- kruskal.test(stopped$DONT_ASK_misunderstood, stopped$gender)

tbl.22 <- table(stopped$DONT_ASK_work_up_nerve, stopped$gender)
nerveTest <- kruskal.test(stopped$DONT_ASK_work_up_nerve, stopped$gender)

tbl.23 <- table(stopped$DONT_ASK_appropriate, stopped$gender)
appropriateTest <- kruskal.test(stopped$DONT_ASK_appropriate, stopped$gender)

tbl.24 <- table(stopped$DONT_ASK_not_my_field, stopped$gender)
fieldTest <- kruskal.test(stopped$DONT_ASK_not_my_field, stopped$gender)

tbl.25 <- table(stopped$DONT_ASK_speaker_eminence, stopped$gender)
eminenceTest <- kruskal.test(stopped$DONT_ASK_speaker_eminence, stopped$gender)

tbl.26 <- table(stopped$DONT_ASK_not_clever_enough, stopped$gender)
cleverTest <- kruskal.test(stopped$DONT_ASK_not_clever_enough, stopped$gender)

tbl.27 <- table(stopped$DONT_ASK_meet_later, stopped$gender)
laterTest <- kruskal.test(stopped$DONT_ASK_meet_later, stopped$gender)

# respondents who indicated that men ask more questions:
# subset of individuals who believe men ask more questions:
men_ask_more <- subset(survey_data_gender, WHO_ASKS_gender == "men")

# do respondents believe this is because of...
tbl.31 <- table(men_ask_more$Q34_misunderstood, men_ask_more$gender)
kruskal.test(men_ask_more$Q34_misunderstood, men_ask_more$gender)

tbl.32 <- table(men_ask_more$Q34_nerve, men_ask_more$gender)
kruskal.test(men_ask_more$Q34_nerve, men_ask_more$gender)

tbl.33 <- table(men_ask_more$Q34_appropriate, men_ask_more$gender)
kruskal.test(men_ask_more$Q34_appropriate, men_ask_more$gender)

tbl.34 <- table(men_ask_more$Q34_expertise, men_ask_more$gender)
kruskal.test(men_ask_more$Q34_expertise, men_ask_more$gender)

tbl.35 <- table(men_ask_more$Q34_intimidated_by_speaker, men_ask_more$gender)
kruskal.test(men_ask_more$Q34_intimidated_by_speaker, men_ask_more$gender)

tbl.36 <- table(men_ask_more$Q34_not_clever_enough, men_ask_more$gender)
kruskal.test(men_ask_more$Q34_not_clever_enough, men_ask_more$gender)

tbl.37 <- table(men_ask_more$Q34_after_seminar, men_ask_more$gender)
kruskal.test(men_ask_more$Q34_after_seminar, men_ask_more$gender)

####
# Q3: Is there a way to address the gender disparity in question-asking behaviour?
###

kruskal.test(survey_data_gender$ASK_MORE_longer_time ~ survey_data_gender$gender)
kruskal.test(survey_data_gender$ASK_MORE_ask_in_person ~ survey_data_gender$gender)
kruskal.test(survey_data_gender$ASK_MORE_nicer_speakers ~ survey_data_gender$gender)
kruskal.test(survey_data_gender$ASK_MORE_more_welcoming_host ~ survey_data_gender$gender)
kruskal.test(survey_data_gender$ASK_MORE_condifence ~ survey_data_gender$gender)
kruskal.test(survey_data_gender$ASK_MORE_seniority ~ survey_data_gender$gender)
kruskal.test(survey_data_gender$ASK_MORE_having_a_moderator ~ survey_data_gender$gender)
kruskal.test(survey_data_gender$ASK_MORE_moderator_engaging_audience, survey_data_gender$gender)


№1.  
a) Система, работающая на правилах, работает точнее HMM-теггера в той области, для которой составлены правила (по крайней мере, так было в 2005 году) [1]. Кроме того, система, работающая на правилах, может достаточно эффективно работать с языком, корпус текстов на котором мал.   
b) Система, работающая с помощью разметки корпуса и обучения марковских моделей, показывает более высокий уровень полноты при снятии неоднозначности [1]. Также не нужно прописывать длинные списки исключений и анализировать максимально возможное число правил вручную.   

На мой взгляд, для языков с большим корпусом текстов удобнее использовать HMM, а для, например, малых языков -- основанную на правилах систему. 

№2.  
Да, можно использовать гибридные модели, которые, например, включают в себя основные правила частеречной разметки, а при спорных случаях используют данные корпуса и марковские модели. 

№3.  
Предложение: "Хрупкое стекло не подходит для этой работы."

стекло (VERB) и стекло (NOUN) можно различить, поскольку существительное с большей вероятностью находится после прилагательного.
стекло (SG.NOM) и стекло (SG.ACC) можно различить, поскольку существительное в именительном падеже с большей вероятностью находится в начале предложения. 

№4.  
false positive (fp) -- число не-присуждения слову верных тегов  
false negative (fn) -- число присуждения слову верных тегов  
precision = tp/(tp + fp) -- число присуждения слову верных тегов/(число присуждения слову верных тегов + число не-присуждения слову верных тегов)

Кажется, что для полного снятия неоднозначности случаи fp и fn симметричны (если слову не приписали верный  тег, значит, ему приписали какой-либо из неверных)

Если снятие неоднозначности неполное, то:  
-- если  количество fp у одного теггера больше, чем у другого, это означает, что среди присужденных слову тегов отсутствуют верные  
-- если количество fn у одного теггера больше, чем у другого, это означает, что среди присужденных слову тегов присутствуют ложные (в том числе, например, может быть неснятая неоднозначность и два варианта тега для слова)  

Если у одного теггера выше точность (precision), то соотношение найденных им верных тегов будет выше, чем количество вообще всех верных тегов.

№5.  
Unigram теггер присваивает слову самый частый тег, не глядя на контекст, в отличие от n-gram теггера.  
Например, в предложении "Молоко стекло на пол" unigram tagger может выбрать вариант "существительное" для слова "стекло", а n-gram tagger -- "глагол", так как вероятность глагола после существительного выше, чем существительного в именительном падеже.   

Ссылки: 
1. Сравнение  эффективности двух методик снятия лексической и морфологической неоднозначности для русского языка (скрытая модель Маркова и синтаксический  анализатор именных групп) (http://www.aot.ru/docs/RusCorporaHMM.htm)
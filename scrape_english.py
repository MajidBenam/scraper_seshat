# this file scrapes the texts from sprachbar dw and saves a latex file 
# simply put the latex source into overleaf and get the pdf file.

# next step, get everything from sprachbar:
# go to file: scrape_3.py
# 
# <div class="group">
# <h4>Sprachbar</h4>
# <ul class="smallList">
# <li><a href="/de/am-aschermittwoch-ist-alles-vorbei/l-39902505">Am Aschermittwoch ist alles vorbei</a></li>

from types import new_class
from lxml import etree, html
from bs4 import BeautifulSoup
import requests
import re
import bs4


source_url = 'http://www.manythings.org/voa/health/4062.html'

# cool trick
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
#source = requests.get(source_url, headers=headers).text
source = requests.get(source_url, headers=headers)

#soup = html.fromstring(source)
soup = BeautifulSoup(source.content.decode('utf-8'), 'lxml')
texttext = ["""
Today, we will talk about diet and weight loss. Exercise is important if you want to get in good shape. But experts say exercise alone is not enough if your goal is to lose weight.

It is that time of year again. Warm weather has returned to earth’s northern hemisphere. Summer is a time when people of all ages feel like getting their swimwear and going to the nearest swimming pool or seashore.

But first, there is that troublesome little thing called winter weight gain. Many of us gain weight because of inactivity during the winter.

Some people go to extremes to lose that extra weight before going to the beach. In the weight loss industry, there is never a lack of ideas about how to lose weight. Consider the "Sleeping Beauty diet," where you sleep your way to weight loss. You cannot eat if you are sleeping, or so the theory goes.

Then there is the tapeworm diet. The tapeworm is said to help people lose weight by eating the food that is stored in their stomach. But first you have to be willing to swallow the little creature. This may be more trouble than many people want.

Strange, new diets, treatments and exercise programs arrive on the market every day. Each one promises to help people lose weight and get a beach beautiful body. The weight loss industry takes in billions of dollars each year, and it is growing.

One research company says the weight loss business will be worth more than five hundred eighty billion dollars worldwide by the year twenty fourteen. MarketsandMarkets also says the food and drink market represents the largest part of that growth. It is expected to reach more than three hundred fifty five billion dollars by twenty fourteen.

There is a seemingly endless supply of ideas about how to lose weight. There are low-carbohydrate diets and low-fat diets, diets that limit calories and ones that let you eat as much as you want. And, there are thousands of different kinds of diet pills and programs. So where does one begin? Which one is best?

Experts say there is no single diet plan that works best for everyone. Many experts agree on one thing: that to lose weight, you must use or burn off more calories than you take in. When you eat more calories than your body needs, it stores that extra energy as fat.

Calories are a measure of energy in food. A pound of fat is equal to about four hundred fifty three grams or three thousand five hundred calories. To lose that fat in a week, you have to burn off at least that amount in calories or eat that much less. The best thing to do is to combine both ideas. Eat fewer calories and increase physical activity so that you burn off more.

America’s National Institutes of Health has suggested that women limit calories to no less than one thousand two hundred calories a day without medical supervision. It also says men should have no less than one thousand five hundred calories. Debate continues about the best way to fill those calorie requirements.

For years, eating a diet low in fat was said to be the best way to lose weight. A low-fat diet is one in which less than thirty percent of a person’s daily calorie intake comes from fat.

Dean Ornish developed one of the most popular low fat diets after years of research on ways to control heart disease. His dietary ideas were first published in the medical journal The Lancet in nineteen ninety. The Ornish diet plan became more popular in nineteen ninety-three with the release of his book “Eat More, Weigh Less.”

Dr. Ornish studied the effects of carbohydrates – one of the most important sources of energy for the body. He found that carbohydrates were not to blame for making people fat. Instead, he said, fat makes people fat. He noted that a baked potato is not high in fat, but it becomes fatty when people add sour cream and butter to it.

Dr. Ornish’s diet plan limits daily calories from fat to less than ten percent, with little to no saturated fat or cholesterol. He also suggested that people get seventy to seventy-five percent of their calories from complex carbohydrates, and fifteen to twenty percent from proteins.

Like other low-fat diets, the Ornish plan suggests that people eat diets high in whole grains, fruits, vegetables, beans and other legumes. The plan advises people to avoid all meat and meat products, and to stay away from oils, nuts and seeds. It does not limit the number of calories people eat. But, eating the foods suggested by the diet plan would reduce the number of calories.

The Ornish diet has proved to be effective for many people. However, critics say it lets dieters eat too many carbohydrates while setting restrictions on calories from fat. They also say the changes required in eating habits may be too extreme for many people to follow.

Unlike the Ornish diet, low carbohydrate diets limit foods that are high in carbohydrates. These diets advise people to avoid things like white flour, pasta, rice, potatoes and foods high in sugar. Instead they suggest that people eat foods that are high in proteins and fats. These include foods like meat, fish, chicken, eggs, cheese and nuts.

The Atkins diet is one of the most popular of these diets. It suggests that people eat fewer than twenty grams of carbohydrates a day. This amount is slowly increased to  between forty and one hundred grams of carbohydrates a day to keep the weight off.

Both weight loss plans have been carefully studied over the years. But no one plan has come out as a clear winner. Three years ago, a study in the New England Journal of Medicine found low-carb diets to be the best at providing the most weight loss. The study was led by researchers at the Brigham and Women’s Hospital in Boston and Ben Gurion University in Israel.

The researchers studied more than three hundred obese patients who followed one of three diet plans. These included a low-fat diet, a low-carb diet and a Mediterranean diet, which is made up of fruits, vegetables, lean proteins, olive oil and nuts.

A similar study published a year later looked at more than eight hundred dieters. The study found that low fat diets and high fat diets were equally successful at providing and maintaining weight loss over a two year period.

The researchers concluded that the most important thing for any diet is that people stick with it. And you must burn more calories than you take in no matter what you eat.

Some people are unable to lose weight through diet and exercise, no matter how hard they try. Others are just not willing to put in the effort. Many of these people choose to have surgical operations to reach their weight loss goals.

One kind of weight loss surgery reduces the size of the stomach. This is done by separating the stomach into two parts, including a very small section at the top. People who have had this operation are forced to eat smaller amounts of food because their top stomach fills up much faster.

Research suggests that most people lose about half of their overweight pounds in the first year after surgery. However, a large number of people regain the weight in three to five years.

A new report suggests similar results for another popular weight loss surgery. Liposuction has been widely used since the nineteen seventies to improve the body’s appearance. It improves body shape by removing fat from certain parts of the body. The most common areas are the stomach, waist, hips, thighs, neck and arms. The International Society of Aesthetic Plastic Surgery says liposuction is the most popular form of cosmetic surgery worldwide.

Recently, researchers at the University of Colorado School of Medicine found that the effects of the surgery may not be long-lasting. They said people who have liposuction usually experience weight gain within one year after the surgery. And the fat that comes back reappears in a new area of the body, most noticeably the shoulders, arms and upper abdomen. The researchers say this is one more reason to try to prevent obesity before it happens.
""",]

block_words = [' in ', ' the ', ' a ', ' to ', ' off ', ' on ', ' with ', ' by ', ' across ', ' along ',
                        ' more ', ' its ', ' them ', ' at ', ' about ', ' that ', ' this ', ' it ',
                        ' of ', ' get ', ' take ', ' from ', ' as ', ' while ', ' when ',
                        ' out ', ' under ', ' about ', ' for ', ' been ', ' was ', ' had ',
                        ' have ', ' whether ', ' or ', ' his ', ' her ', ' most ', ' less ',
                        ' over ', ' like ', ' up ', ' towards ', ' near ', ' nearly ', ' despite ',
                        ' though ', ' except ', ' against ', ' between ']

# selects the main text
main_text = soup.find_all('p')
print(main_text)
# puts each paragraph into a separate element of a list.
majid_text= []
for goodie in main_text:
    majid_text.append(goodie.text)
    #print(goodie.text)
    #print()
#

# replace the blocked words
# new_majid=[]
# for par in majid_text:
#     for word in block_words:
#         insensitive_word = re.compile(re.escape(word), re.IGNORECASE)
#         new_par = insensitive_word.sub(' (---) ', par)
#         # new_par=par.replace(word, ' (---) ')
#         par = new_par
#     new_majid.append(par)


# fror pure texts to escape the apostrophe problem
new_majid=[]
for par in texttext:
    for word in block_words:
        insensitive_word = re.compile(re.escape(word), re.IGNORECASE)
        new_par = insensitive_word.sub(' (---) ', par)
        # new_par=par.replace(word, ' (---) ')
        par = new_par
    new_majid.append(par)

with open('lat_text_eng.tex', 'w') as my_file:
    my_file.write('\\documentclass[14pt,a4paper]{extarticle}\n')
    my_file.write('\\usepackage[english]{babel}\n')
    my_file.write('\\usepackage[letterpaper,top=1.5cm,bottom=1.5cm,left=1.5cm,right=1.5cm,marginparwidth=1.5cm]{geometry}\n')
    my_file.write('\\begin{document}\n')
    my_file.write('\\section{Text with Blanks}')

    for par in new_majid:
        my_file.write(par)
        my_file.write('\\newline\\newline ')
    
    my_file.write('\\newline\\newline ')
    my_file.write('\\section{Text without Blanks}')

    for par in texttext:
        my_file.write(par)
        my_file.write('\\newline\\newline ')
    
    my_file.write('\\newline\\newline ')

    my_file.write('\\end{document}')



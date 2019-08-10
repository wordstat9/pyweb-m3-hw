

def make_prediction():
	from horoscope import generate_prophecies
	fp = generate_prophecies(3,4)
	i = 0
	prediction = ""
	while i < len(fp):		
		a = fp[i]
		prediction = prediction + " <p> " + str(a) + " </p> "		
		i +=1
	prediction = prediction + " <hr> " + '<p>  <a href = "/about.html"> О реализации </a>'
	
	return (prediction)


import datetime



dt_now = datetime.date.today()  


main = open("index.html", "w")
print ("<html>", file = main)
print (f"<head>  <title>  Гороскоп на {dt_now} </title> </head>", file=main)
pr = make_prediction()
header = "<body> <h1> Ваши предсказания на " +  str(dt_now) + " </h1>"
print (header + pr, file=main)
print ("</body> </html>", file = main)
main.close()
# 


#def make_body()
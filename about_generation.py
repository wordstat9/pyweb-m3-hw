times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


printed_times =""
i = 0 
while i != len(times):
	printed_times = printed_times + " <li>" + times[i]
	i+=1


i = 0
printed_advices = ""
while i!= len(advices):
	printed_advices = printed_advices + " <li>" + advices[i]
	i +=1


i = 0
printed_promises = ""
while i != len(promises):
	printed_promises = printed_promises + " <li>" + promises[i]
	i +=1

about = open("about.html","w")
print("""<html>
	<head>
	<title> О чем все это </title>
	</head>""", file =about)
print ("""<body>
	<h1> «О чём все это» </h1> """, file =about)
print('<p><img src="images/telec.png" width="100" height="100" alt="тельцы"></p>', file =about)    # ДОБАВИТЬ КАКУЮ НИБУДЬ КАРТИНКУ ЗНАКА ЗОДИАКА
print (f""" <p> Параметры генерации: </p> <p>
		 <ol>
	<li> Времена дня:
		<ul>
		{printed_times}
		</ul>
	<li> Глаголы:
		<ul>
		{printed_advices}
		</ul>
	<li> Ожидания:
		<ul>
		{printed_promises}
		</ul>
	</ol>
	</p>
	<hr>
	<p><a href= "/index.html"> Основная страница </a></p>
	</body>
	</html>""", file =about)
about.close()

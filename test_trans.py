from googletrans import Translator
t = Translator()
res = t.translate('<p>안녕하세요. <b>강조</b> <i>기울임</i> <img src="test.jpg"></p>', src='ko', dest='en')
print(res.text)

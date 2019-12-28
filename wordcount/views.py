from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')


def count(request):
	data = request.GET["fulltextarea"]
	wordlist = data.split()
	list_length = len(wordlist)

	worddictionary = {}                  #Creating empty dictionary to add new words

	for word in wordlist:                #Accessing every words from wordlist
		if word in worddictionary:       #Checking presence of word in worddictionary
		    #Increse words value by 1
		    worddictionary[word] += 1

		else:
			#add word to worddictionary and assin value to 1
			worddictionary[word] = 1

	sorted_list = sorted(worddictionary.items(),key= operator.itemgetter(1),reverse=True)



	
	return render(request,'count.html',{'fulltext':data,'words':list_length,'worddictionary':sorted_list})

def about(request):
	return render(request, 'about.html')



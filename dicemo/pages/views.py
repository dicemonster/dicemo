from django.shortcuts import render_to_response
from django.template import RequestContext
from pages.models import HomePage 
import twitter

# c_key = 'cnzwR9fEeUNfhSl746bJAg'
# c_secret = 'b0KYKHhQ5zDYJWdy0bjsYdcAXOal1RFVC1zOaKLO9gw'
# at_key = '1866370867-b6lVdZAIDOGsJ40LHW1urV0hwhsaQ6eOil2sxdI'
# at_secret = 'kNnxOABe1J8DMhYReB98ba4FOLaFEmbyFpbFexTKAPE'
# twitter_acct = 'thedicemonster'

def MainHomeCopy(request):
        homepage 	= HomePage.objects.get(pk=1)
	car1 		= HomePage.objects.get(pk=2)
	car2	 	= HomePage.objects.get(pk=3)
	car3	 	= HomePage.objects.get(pk=4)
	car4	 	= HomePage.objects.get(pk=5)
	footer		= HomePage.objects.get(pk=6)
	col1 		= HomePage.objects.get(pk=7)
	col2 		= HomePage.objects.get(pk=8)
	col3 		= HomePage.objects.get(pk=9)

	context = {'homepage': homepage, 'car1' : car1, 'car2' : car2, 'car3' : car3, 'car4' : car4, 'footer' : footer, 'col1' : col1,'col2' : col2,'col3' : col3,  'tweets' : getTweets()}
        return render_to_response('index.html', context, context_instance=RequestContext(request))


def getTweets():
        tweets = []
	tweets_short = []
        try:
                import twitter
                api = twitter.Api(consumer_key='cnzwR9fEeUNfhSl746bJAg',consumer_secret='b0KYKHhQ5zDYJWdy0bjsYdcAXOal1RFVC1zOaKLO9gw',access_token_key='1866370867-b6lVdZAIDOGsJ40LHW1urV0hwhsaQ6eOil2sxdI',access_token_secret='kNnxOABe1J8DMhYReB98ba4FOLaFEmbyFpbFexTKAPE')
                latest = api.GetUserTimeline('tentacledoldone')
                for tweet in latest:
                        status 		= tweet.text
                        tweet_date 	= tweet.relative_created_at
                        tweets.append({'status': status, 'date': tweet_date})
		tweets_short = tweets[:5]
        except:
                tweets.append({'status': '@thedicemonster', 'date': 'about 6.66 minutes ago'})
        return {'tweets': tweets_short}



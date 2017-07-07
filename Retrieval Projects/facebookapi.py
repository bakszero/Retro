import facebook
import simplejson
import urllib2
import json

#create the api key dictionary 
api_key = {
        'api_key': '2193158430910784'
        'api_secret': 'a7350f3728623c3605aa7378a32768b7'
        'access_token': 'EAAfKqn016UABANkNZCZAWoNg1xmM3HBA7pqB0fZCqbYtKub0MeuJiCcEEeKEM84yYbd0Fyun1piXlfWhwQRn8iXYgvYRuHn7DR2LCNy5iodZA2u5GTkH8YdruvZCeaqv03rfOlaJ2xCy2MHQIt2aiM2FYBMDmZBlbSbfZBEoAmfRQZDZD'
}  


def search_user(api_key, search_phrase, paginate_newer_attribute, paginate_older_attribute):
    graph =facebook.GraphAPI(access_token = api_key['access_token'])

    #post = graph.get_object('narendramodi'+'/feed', fields='caption','description')

    if no_new_posts == False:
        if paginate_older_attribute == '0':
            post = graph.get_object(search_phrase+'/feed', fields = 'caption,description, from,message,created_time, full_picture')


        else:
            post_pre = urllib2.urlopen(paginate_older_attribute, timeout=30)
            post = simplejson.load(post_pre)
            post_pre.close()

    else:
        post_pre = urllib2.urlopen(paginate_newer_attribute, timeout=30)
        post = simplejson.load(post_pre)
        post_pre.close()

    print (post)
    return post



def start_data_collection(search_phrase):
    paginate_newer_attribute= '0'
    paginate_older_attribute= '0'
    no_new_posts = False

    count = 0

    while count < 2000:
        post = search_user(api_key, search_phrase, paginate_newer_attribute,paginate_older_attribute, no_new_posts)

        if (len(post['data']==0)):
            if no_new_posts == False and paginate_older_attribute == '0':
                if 'paging' in post and 'previous' in post['paging']:
                    paginate_newer_attribute = post['paging']['previous']
                
            elif no_new_posts ==True:
                paginate_newer_attribute= post['paging']['previous']

        
        if no_new_posts == False:
            if 'paging' in post and 'next' in post['paging']:
                paginate_older_attribute = post['paging']['next']
        

        for status in post['data']:
            count+=1
            insert_data(status)

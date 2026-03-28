# import urllib
# use urllib.req to get the data from the url
# write aa func that takes a url
# returms a res

import urllib.request as urllib_req

def main(url):
    print("Checking Connectivity of", url)
    
    res = urllib_req.urlopen(url)
    print("Connected to", url, "succesfully")
    print("The res code was:", res.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site: ")

main(input_url)
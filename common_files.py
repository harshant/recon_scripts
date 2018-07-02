green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
end = '\033[0m'
info = '\033[93m[!]\033[0m'
bad = '\033[91m[-]\033[0m'
run = '\033[97m[~]\033[0m'


import requests
import argparse
files = ["phpinfo.php",".htaccess",".git",".git/HEAD","robots.txt","ws_ftp.ini",".git/config","coredump","filezilla.xml","server-status",".htpasswd",
".DS_Store",".swp",".idea",".svn","package.json","gulpfile.js","Gruntfile.js",".travis.yml",".ssh/id_rsa","sitemap.xml","post-sitemap.xml",".gitignore"]
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain",help="Input a domain to recursively parse all javascript located in a page",action="store_true")
parser.add_argument("-i", "--input", help="Input a: URL, file or folder. For folders a wildcard can be used (e.g. '/*.js').",required="True", action="store")
parser.add_argument("-o", "--output",help="Where to save the file, including file name. Default: output.html",action="store", default="output.html")
parser.add_argument("-b", "--burp",help="",action="store_true")
parser.add_argument("-c", "--cookies",help="Add cookies for authenticated JS files",action="store", default="")
parser.add_argument("-a","--header",help="Add authorization header",action="store",default="")
args = parser.parse_args()

he=args.header.split(":")
with open('links.txt',"r") as f:
    lines = f.read().splitlines()

for dir in files:
    if args.header:
        r=requests.get(args.input+'/'+dir,headers={he[0]:he[1]})
    else:
        r=requests.get(args.input+'/'+dir,timeout=10)
    if r.status_code == 200:
        print '%s'%green + dir 
        print str(r.status_code) + '%s'%end ; 
        print r.text
        print '===================================================='
    else:
        print '%s'%red + dir + '%s'%end ; 
        print r.status_code
        print '===================================================='


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


import dns.resolver 
import argparse    #import module argparse
parser = argparse.ArgumentParser() #create a new instance named 'parser'
parser.add_argument("-i", "--input", help="Input a: URL, file or folder. For folders a wildcard can be used (e.g. '/*.js').",required="True", action="store")
args = parser.parse_args()
host=args.input
record_type=['A','AAAA','MX','TXT']  # create a list of accepted dns records type
myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'
for record in record_type:
	
    try:
        print '{.OKBLUE}==================================={.ENDC}'.format(bcolors, bcolors); print record
        myAnswers = myResolver.query(host, record) #Lookup the 'A','AAAA','MX','TXT' record(s) for provided domain
        for rdata in myAnswers: #for each response
            print rdata #print the data
    except:
        print 'no record found for %s' %record


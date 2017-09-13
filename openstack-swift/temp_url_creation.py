#!/usr/bin/python

import hmac, sys, getopt, os
from hashlib import sha1
from time import time
from optparse import OptionParser


def main():

    # create command line option parser
    parser = OptionParser(add_help_option=False)
    # configure command line options
    parser.add_option("-h", "--help", action="help")
    parser.add_option("-p", "--uri-path", action="store", type="string", dest="uri_path", help="\t CloudFiles URI Path, ex: /v1/AUTH_account/container/my_cat.jpg")
    parser.add_option("-k", "--tempurl-key", action="store", type="string", dest="temp_url_key", help="\t Your CloudFiles Private Account-Meta-Temp-URL-Key")
    parser.add_option("-e", "--expiration", action="store", type="int", dest="expiration", default=3600, help="\t Expiration time in seconds")
    parser.add_option("-m", "--method", action="store", type="string", dest="method", default="GET", help="\t Expiration time in seconds")

    # parse command line options
    (options, args) = parser.parse_args()

    if options.uri_path is None:
        print ("\nError: -p, --uri-path : CloudFiles URI Path is required\n")
        parser.print_help()
        sys.exit(1)

    if options.temp_url_key is None:
        print ("\nError: -k, --tempurl-key : CloudFiles Private Account-Meta-Temp-URL-Key is required\n")
        parser.print_help()
        sys.exit(1)


    expires = int(time() + options.expiration)
    hmac_body = '%s\n%s\n%s' % (options.method, expires, options.uri_path)
    sig = hmac.new(options.temp_url_key, hmac_body, sha1).hexdigest()

    print "\nCloudFiles Temporary URL:"
    print "  Temporary URL = htts://<your_endpoint>%s?temp_url_sig=%s&temp_url_expires=%s \n" % (options.uri_path, sig, expires)


if __name__ == "__main__":
    main()

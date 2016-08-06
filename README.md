Intro:

I created this python script to generate Dahua hashes, which are found in a lot of security cam DVR units. The hash is easily cracked using John the Ripper, but I wanted to be able to edit the contents of the password file on the system. There is also a metasploit module available, but I have not confirmed whether it works on my unit or not.


Requirements:

Written with python3, but should work on earlier versions as well.

Running:

python DahuaHash.py [-v -h] [-p <password>] [-i <input file> -o <output file>]

Arguments:

  -v  verbose output, no effect when using single password mode
  -h  display help information
  -p  | --password  single password mode; prints hash to terminal
  -i  | --infile    input file; one password per line
  -o  | --outfile   output file; format is <password>,<hash>

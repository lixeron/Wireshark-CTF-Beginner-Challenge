This is my first ever wireshark program and it was made so I can understand networking, noise, and trafficking.
The code may not be great, but I am still learning.
Essentially here is what it does:
Say I have a secret message (in this case the flag being named, well the_flag)
I essentially break said message apart into fragments using ICMP and to send it through a network.
Now this is extremely easy to find and to make it more challenging I just decided to add a bunch of random noise mixed in.
The packets will be done running after the print statement has been executed 
When running the code, one must use wireshark and capture the packets according to the network they are on.
Then stop capturing and then analyze the packets and their data. Eventually you'll notice the noise is useless and process eliminate to it being ICMP packets.
Filter it, analyze the packets and find a pattern.
To pattern is to look at the data in the ICMP packets and notice how different the data is compared to other ICMP packets. (e.g. Data: 5a6d78685a)
Record the data in a notepad and then see if the numbers mean anything. If you'll notice, it is encoded using hex, when you will then need to decode to ASCII
After decoding and recoding the encoded hex to ASCII, you can then decode it furhter using a Base64 decoder and input all the data you found to find the flag!

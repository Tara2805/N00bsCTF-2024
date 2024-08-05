# Disk Golf
457
Let's play some disk golf! Author: NoobMaster

# Attachments
disk.img.tar.gz

# Walkthrough:

Unzip contents of zip file
Use the sleuthkit to analyze file
list files with fls disk.img
Navigate to the Home Directory of the disk image - fls disk.img 1723
Identify the johnhackerdoe directory in the home directory
view files with ls 
read contents - icat disk.img 262249
Decode the Octal Encoded Flag with awk

# Flag
n00bz{7h3_l0ng_4w41t3d_d15k_f0r3ns1c5}

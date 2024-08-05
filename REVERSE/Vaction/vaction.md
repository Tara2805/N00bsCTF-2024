# Vacation
100
My friend told me they were going on vacation, but they sent me this weird PowerShell script instead of a postcard! Author: 0xBlue

# Attachments
run.ps1
output.txt

# Walkthrough
From n00bz Official Writeup

 Understanding challenge
This challenge involves understanding how XOR encryption works and reversing it to retrieve the original message (the flag). The provided run.ps1 PowerShell script shows how a text file is encrypted using XOR with a key. The challenge is to decrypt the given output using the same key.

 How the Encryption Works
Reading the flag: The script reads the contents of flag.txt and converts it into an array of ASCII bytes.
XOR Operation: Each byte is XORed with the key 3 (-bxor 3).
Generating Output: The resulting bytes are converted back to a string and saved to output.txt.

 Reversing the XOR Operation
To decrypt the message, we need to perform the XOR operation again with the same key on the encrypted message. XOR encryption is symmetric, meaning:
Original Byte = Encrypted Byte ⊕ Key

If you replace the flag.txt part in the first line of the script to output.txt, it'll xor the output with the key instead, giving you back the original flag.

# Flag
Flag: n00bz{from_paris_wth_xor}

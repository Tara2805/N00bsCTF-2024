# Read the WAV file
with open('/attachments/chall.wav', 'rb') as file:
    data = bytearray(file.read())

# Fix the header
data[0:4] = b'RIFF'
data[8:16] = b'WAVEfmt '
data[36:40] = b'data'

# Write the fixed file
with open('/attachments/fixed_chall.wav', 'wb') as file:
    file.write(data)

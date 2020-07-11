# F33dback App

Will has been tasked with collecting feedbacks for the CTF. Instead of using online form he made this app as he wanted to get his hands dirty with App dev and S3.

**Tip**: Being a first time S3 user, he may have messed up the permissions.


**Obs (ctf crew)**: Give the `feedback.apk` file to contestants

**Flag**: `mlh{s3_i5_c0mpl1cat3d}`

**Solution**: Decompile the apk -> Get S3 and Cognito Creds and then use boto3 to download `flag.txt` from S3.

# Custom password manager

The goal is to have a non-synchronized password file for secondary websites needing an account:

- the script `sAddPassword.sh` adds a password to the list and the script `sRetrievePassword.sh` retrieves the passwords matching the website name
- a copy is made to the clipboard with `xclip` under Xorg and `wl-copy` under Wayland
- in the case several logins match the site, the password in the clipboard is always the first one found
- both scripts assume the username is `user` which you would need to change, for `openssl` needs an absolute path.

## Usage

1. Make a directory `~/passwords`
2. Create a `passwords_encrypted` file in the later directory:
```
$ cd ~/passwords
$ echo "site:login:password" >> passwords_decipher.txt
$ openssl enc -aes-256-cbc -pbkdf2 -e -in passwords_decipher.txt -out passwords_encrypted
```
3. When you need to add a password for a new site `newsite` with login `newlogin`, call `sAddPassword.sh`:
```
$ ./sAddPassword.sh newsite newlogin
```
4. To retrive login and password for the site `newsite`, call `sRetrievePassword.sh`
```
$ ./sRetrievePassword.sh newsite
```
A copy is made to the clipboard via `xclip` under X or `wl-copy` under Wayland

5. To force the decryption of the encrypted password file and clean it up, you can call `openssl` directly:
```
$ openssl enc -aes-256-cbc -pbkdf2 -d -in ~/passwords/passwords_encrypted  -out passwords_decipher.txt
```
Don't forget to remove `passwords_decipher.txt` afterwards
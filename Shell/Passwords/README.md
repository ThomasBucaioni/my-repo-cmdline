# Custom password manager

The goal is to have a non-synchronized password file for secondary websites needing an account

## Usage

1. Make a directory `~/passwords`
2. Create a `passwords_encrypted` file in the later directory:
```
$ cd ~/passwords
$ echo "site:login:password" >> password_decipher.txt
$ openssl enc -aes-256-cbc -pbkdf2 -e -in password_decipher.txt -out password_encrypted
```
3. When you need to add a password for a new site `newsite` with login `newlogin`, you call `sAddPassword.sh`:
```
$ ./sAddPassword.sh newsite newlogin
```
4. To retrive a password for the site `newsite`, you call `sRetrievePassword.sh`
```
$ ./sRetrievePassword.sh newsite
```
A copy is made to the clipboard via `xclip` under X or `wl-copy` under Wayland
5. To force the decryption of the encrypted password file, you can call `openssl` directly:
```
$ openssl enc -aes-256-cbc -pbkdf2 -d -in ~/passwords/passwords_encrypted  -out passwords_decipher.txt
```
Don't forget te remove it afterwards
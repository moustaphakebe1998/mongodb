# mongodb

## initialisation 
```bash
echo "# mongodb" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:moustaphakebe1998/mongodb.git
git remote set-url origin https://github.com/..mongodb.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin git@github.com:..mongodb.git
git branch -M main
git push -u origin main

..sshkey
ssh-keygen -t rsa -b 4096 -C "votre_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
# tester la connection 
ssh -T git@github.com
```



 

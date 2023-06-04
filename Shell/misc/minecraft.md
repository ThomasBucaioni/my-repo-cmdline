# Create a Minecraft server

## User account

```
java --version
sudo useradd minecraft
```

## Deploy

```
sudo mkdir /opt/minecraft
ll /opt/minecraft
sudo chown minecraft:minecraft /opt/minecraft
sudo su - minecraft
cd /opt/minecraft
curl -O https://www.minecraft.net/download/.../server.jar
java -jar server.jar

vim eula.txt
    eula=TRUE
```

## Grant operator status

```
vim server.properties
    white-list=true

java -jar server.jar
op myminecraftusername
whitelist add myminecraftusername
```

## Make a systemd service

```
sudo vim /etc/systemd/system/minecraft.service

[Unit]
Description=Vanilla Minecraft Java Edition Server
After=network.target

[Service]
User=minecraft
WorkingDirectory=/opt/minecraft
ExecStart=/bin/java -Xmx2G -Xms2G -jar server.jar
Restart=on-failure
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
systemctl status minecraft
sudo systemctl enable minecraft
sudo systemctl start minecraft
journalctl -u minecraft -f
```

## Join the server

Buy a client...


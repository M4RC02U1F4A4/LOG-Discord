# LOG-Discord

Bot per avere un file log del proprio server di Discord

### Features
* Connessione e disconnessione
* Creazione di inviti
* Join e leave del server
* Mute del microfono
* Cambio regione
* Cambio livello di sicurezza
* Ban e Unban
* Cambio nickname
* Status
* Chat
* Messaggi modificati

## Intallation
```
touch <path-to-your-output-folder>/out.txt
touch <path-to-your-output-folder>/chat.txt
docker load -i discord-<release>
docker run -d --name discord -e TZ=Europe/Amsterdam -e "DISCORD_TOKEN=<bot-token>" -e "DISCORD_GUILD_NAME=<discord-server-name>" -v <path-to-your-output-folder>:/app/out discord-<release>
```
Dopo il comando ``` docker run ``` il container è già avviato
### Start
```docker start discord```
### Stop
```docker stop discord```
### Logs
```docker logs -f discord```

## discord.py documentation
https://discordpy.readthedocs.io/en/latest/index.html

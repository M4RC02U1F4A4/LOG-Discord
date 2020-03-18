# LOG-Discord

Bot per avere un file log del proprio server di Discord

### Features
* Connessione e disconnessione
* Creazione di inviti
* Join e leave del server
* Mute del microfono

## Intallation
```
docker load -i discord-<release>
docker run -d --name discord -e TZ=Europe/Amsterdam -v <path-to-your-output-folder>:/app/out discord-<release>
```

## Documentation
https://discordpy.readthedocs.io/en/latest/index.html

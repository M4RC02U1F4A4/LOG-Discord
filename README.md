# LOG-Discord <img align="right" src="https://img.shields.io/badge/Status-WORKING-blue">

Bot per avere un file log del proprio server di Discord

### Features
* [LOG del server](https://github.com/Marco1097/LOG-Discord/wiki/LOG)
* Log della chat
* Activities log
* [Prometheus stats](https://github.com/Marco1097/LOG-Discord/wiki/Prometheus)

## Grafana

![Immagine 2021-05-14 003338 - Copia](https://user-images.githubusercontent.com/23193188/118196199-e6f0ff80-b44c-11eb-8e5a-255f91686b90.jpg)
![Immagine 2021-05-14 003421 - Copia](https://user-images.githubusercontent.com/23193188/118196202-e8222c80-b44c-11eb-9845-edcbcbcf7815.png)


## Intallation

### Build

```console
$ git clone https://github.com/M4RC02U1F4A4/LOG-Discord.git
$ cd LOG-Discord
$ chmod +x start_discord
$ docker build -t discord .
```

### Run

#### Creazione dei file necessari
```console
$ touch <path-to-your-output-folder>/log.txt
$ touch <path-to-your-output-folder>/chat.txt
$ touch <path-to-your-output-folder>/activities.txt
```
#### Avvio del container
```console
$ docker run -d --name discord -p 9324:9324 -e TZ=Europe/Amsterdam -e "DISCORD_TOKEN=<bot-token>" -e "DISCORD_GUILD_NAME=<discord-server-name>" -v <path-to-your-output-folder>:/app/out discord
```
Dopo il comando ``` docker run ``` il container è già avviato
### Start
```docker start discord```
### Stop
```docker stop discord```
### Logs
```docker logs -f discord```

## [Prometheus](https://hub.docker.com/r/prom/prometheus)
```
docker run --name prometheus -d -p 9090:9090 -v <path-to-config>/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```
```
  - job_name: 'discord'
    scrape_interval: 500ms
    static_configs:
      - targets: ['<IP>:9324']
```

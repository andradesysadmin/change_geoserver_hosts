O script foi criado com o intuito de atualizar hosts de workspaces de projetos cartograficos no GeoServer. Isso possibilita transferir o GeoServer para múltiplas plataformas sem a necessidade de alterar os hosts manualmente.


## easy setup with docker

```bash
docker build -t script_hosts_geoserver .
docker run -it script_hosts_geoserver /bin/bash
```

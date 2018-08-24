修改自 cas-bigdatalab
地址 https://github.com/cas-bigdatalab/ambari-kylin-service.git
## To download the Kylin service folder, run below    

```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo git clone https://github.com/TiestoRay/ambari-kylin.git /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/KYLIN
```
## Restart Ambari
service ambari restart

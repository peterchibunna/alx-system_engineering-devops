# 0x10-https_ssl


# To generate ssl certificate
```shell
sudo apt install python3-certbot -y
sudo certbot certonly --manual --preferred-challenges dns
```
Certificate was saved at `/etc/letsencrypt/live/www.peterchibunna.tech/fullchain.pem`.
Your key file has been saved at: `/etc/letsencrypt/live/www.peterchibunna.tech/privkey.pem`


Then copy the `privkey.pem` to `/etc/letsencrypt/live/www.peterchibunna.tech/fullchain.pem.key`

Add the `A` records for the subdomains: `www`, `web-01`, `web-02`, and `lb-01` with the required ip addresses of your servers.

In generating the SSL certificate, you will be required to add a `TXT` record to your zone file, because we chose the `dns` challenge


# Debugging HAProxy configuration file

```shell
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```

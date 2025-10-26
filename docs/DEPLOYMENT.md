# Deployment Guide

This guide covers deploying Quarks to various hosting platforms.

## Table of Contents
- [Railway](#railway)
- [Heroku](#heroku)
- [Render](#render)
- [AWS](#aws)
- [Docker](#docker)
- [DigitalOcean](#digitalocean)

---

## Railway

**Difficulty:** ⭐ Easy  
**Cost:** Free tier available  
**Best for:** Quick deployments, hobby projects

### Steps

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/quarks-backtester.git
git push -u origin main
```

2. **Connect to Railway**
- Go to [railway.app](https://railway.app)
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose your Quarks repository

3. **Configure**
Railway auto-detects Python and installs dependencies. No additional configuration needed!

4. **Deploy**
Railway automatically deploys. Your app will be live at: `https://your-app.railway.app`

---

## Heroku

**Difficulty:** ⭐⭐ Moderate  
**Cost:** Free tier available  
**Best for:** Scalable applications

### Steps

1. **Install Heroku CLI**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

2. **Login**
```bash
heroku login
```

3. **Create Procfile**
```bash
echo "web: python app.py" > Procfile
```

4. **Update app.py**
Change the last line to use Heroku's port:
```python
port = int(os.environ.get('PORT', 5000))
app.run(debug=False, host='0.0.0.0', port=port)
```

5. **Deploy**
```bash
heroku create your-app-name
git push heroku main
heroku open
```

### Custom Domain
```bash
heroku domains:add www.yourdomain.com
```

---

## Render

**Difficulty:** ⭐ Easy  
**Cost:** Free tier available  
**Best for:** Modern deployments

### Steps

1. **Push to GitHub** (if not already done)

2. **Create New Web Service**
- Go to [render.com](https://render.com)
- Click "New +" → "Web Service"
- Connect your GitHub repository

3. **Configure**
- **Environment:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`

4. **Deploy**
Click "Create Web Service" and Render deploys automatically!

---

## AWS (EC2)

**Difficulty:** ⭐⭐⭐ Advanced  
**Cost:** Paid (free tier available for 12 months)  
**Best for:** Production applications

### Steps

1. **Launch EC2 Instance**
- Amazon Linux 2 or Ubuntu
- t2.micro (free tier eligible)
- Configure security group: Allow ports 22 (SSH) and 80 (HTTP)

2. **Connect via SSH**
```bash
ssh -i your-key.pem ec2-user@your-instance-ip
```

3. **Install Dependencies**
```bash
sudo yum update -y
sudo yum install python3 python3-pip git -y
```

4. **Clone Repository**
```bash
git clone https://github.com/yourusername/quarks-backtester.git
cd quarks-backtester
pip3 install -r requirements.txt
```

5. **Run with Gunicorn**
```bash
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:80 app:app
```

6. **Setup as Service** (optional)
Create `/etc/systemd/system/quarks.service`:
```ini
[Unit]
Description=Quarks Backtester
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/quarks-backtester
ExecStart=/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:80 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable quarks
sudo systemctl start quarks
```

---

## Docker

**Difficulty:** ⭐⭐ Moderate  
**Cost:** Depends on hosting  
**Best for:** Containerized deployments

### Dockerfile

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build and Run

```bash
# Build
docker build -t quarks-backtester .

# Run
docker run -p 5000:5000 quarks-backtester
```

### Docker Compose

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---

## DigitalOcean

**Difficulty:** ⭐⭐ Moderate  
**Cost:** $5/month minimum  
**Best for:** Simple VPS hosting

### Steps

1. **Create Droplet**
- Choose Ubuntu 20.04
- Basic plan ($5/month)
- Select datacenter region

2. **SSH into Droplet**
```bash
ssh root@your-droplet-ip
```

3. **Setup**
```bash
apt update
apt install python3 python3-pip git nginx -y

git clone https://github.com/yourusername/quarks-backtester.git
cd quarks-backtester
pip3 install -r requirements.txt
pip3 install gunicorn
```

4. **Configure Nginx**
Create `/etc/nginx/sites-available/quarks`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable site:
```bash
ln -s /etc/nginx/sites-available/quarks /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

5. **Run Application**
```bash
gunicorn -w 4 -b 127.0.0.1:5000 app:app --daemon
```

---

## Environment Variables

For production deployments, use environment variables:

```python
# app.py
import os

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
PORT = int(os.environ.get('PORT', 5000))
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')

app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
```

Set variables:
```bash
export DEBUG=False
export PORT=5000
export SECRET_KEY=your-secret-key
```

---

## Production Checklist

Before going to production:

- [ ] Set `debug=False` in app.py
- [ ] Use environment variables for sensitive data
- [ ] Implement rate limiting
- [ ] Add authentication if needed
- [ ] Setup HTTPS/SSL
- [ ] Configure CORS properly
- [ ] Setup monitoring/logging
- [ ] Configure backups
- [ ] Test error handling
- [ ] Load test the application

---

## HTTPS/SSL

### Using Let's Encrypt (Free)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d yourdomain.com

# Auto-renewal is configured automatically
```

---

## Scaling

### Horizontal Scaling
- Use load balancer (AWS ELB, Nginx)
- Run multiple instances
- Use Redis for session storage

### Vertical Scaling
- Increase server resources
- Optimize database queries
- Use caching (Redis/Memcached)

---

## Monitoring

### Application Monitoring
```python
# Install
pip install flask-monitoring-dashboard

# Add to app.py
import flask_monitoring_dashboard
flask_monitoring_dashboard.bind(app)
```

### Server Monitoring
- [Datadog](https://www.datadoghq.com/)
- [New Relic](https://newrelic.com/)
- [Prometheus](https://prometheus.io/)

---

## Backup Strategy

1. **Database Backups**
   - Automated daily backups
   - Keep 7-30 days of history
   - Test restore procedure

2. **Code Backups**
   - Use Git for version control
   - Push to GitHub/GitLab
   - Tag releases

3. **Configuration Backups**
   - Store configs in version control
   - Document environment variables
   - Keep secrets secure

---

## Troubleshooting

### App Won't Start
```bash
# Check logs
heroku logs --tail  # Heroku
docker logs container-name  # Docker
journalctl -u quarks  # Systemd
```

### Port Already in Use
```bash
# Find process
lsof -i :5000

# Kill process
kill -9 PID
```

### Out of Memory
- Increase server resources
- Optimize code
- Add swap space

---

## Support

For deployment issues:
- Check application logs
- Review platform documentation
- Open GitHub issue
- Contact platform support

---

## Cost Comparison

| Platform | Free Tier | Paid (Starter) | Best For |
|----------|-----------|----------------|----------|
| Railway | ✅ $5 free | $5+/month | Quick deploys |
| Heroku | ✅ Limited | $7/month | Scalability |
| Render | ✅ Limited | $7/month | Modern apps |
| AWS | ✅ 12 months | $10+/month | Enterprise |
| DigitalOcean | ❌ | $5/month | VPS control |

---

Happy Deploying! 🚀

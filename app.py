from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello Folks 🚀💻</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #000;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #fff;
            overflow: hidden;
        }
        header {
            background-color: #111;
            padding: 15px 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #333;
        }
        header h1 {
            color: #e50914;
            margin: 0;
            font-size: 1.8em;
            letter-spacing: 1px;
        }
        nav a {
            color: #ccc;
            margin-left: 15px;
            text-decoration: none;
            font-weight: 500;
        }
        nav a:hover {
            color: #e50914;
        }
        .hero {
            text-align: center;
            padding: 40px 20px 10px;
        }
        .hero h2 {
            font-size: 2.5em;
            margin-bottom: 5px;
            color: #fff;
        }
        .hero h3 {
            font-size: 1.8em;
            margin-bottom: 10px;
            color: #e50914;
        }
        .hero p {
            font-size: 1.1em;
            color: #bbb;
            margin-bottom: 15px;
        }
        .hero a {
            background-color: #e50914;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            color: #fff;
            font-weight: bold;
            font-size: 0.9em;
        }
        .section {
            padding: 10px 20px 15px;
            text-align: center;
        }
        .section h3 {
            font-size: 1.6em;
            margin-bottom: 10px;
            color: #fff;
        }
        .row {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .card {
            background-color: #1b1b1b;
            border-radius: 10px;
            padding: 8px;
            width: 80px;
            height: 100px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.6);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s;
        }
        .card img {
            width: 36px;
            height: 36px;
            margin-bottom: 6px;
        }
        .card p {
            font-size: 0.7em;
            color: #fff;
            margin: 0;
        }
        .card:hover {
            transform: scale(1.05);
        }
        .workflow {
            margin-top: 10px;
            display: flex;
            justify-content: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        .workflow-step {
            background-color: #1b1b1b;
            padding: 8px 12px;
            border-radius: 8px;
            color: #fff;
            font-size: 0.75em;
            box-shadow: 0 2px 5px rgba(0,0,0,0.4);
        }
        footer {
            padding: 8px;
            font-size: 0.7em;
            color: #777;
            border-top: 1px solid #222;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Hello GCP</h1>
        <nav>
            <a href="#">Home</a>
            <a href="#">Docs</a>
            <a href="#">Contact</a>
        </nav>
    </header>

    <div class="hero">
        <h2>Hello Folks 🚀</h2>
        <h3>GKE Deployment with Cloud Build</h3>
        <p>DevOps Lifecycle: Plan → Build → Test → Deploy → Monitor</p>
        <a href="https://cloud.google.com/kubernetes-engine" target="_blank">Explore GKE</a>
    </div>

    <div class="section">
        <h3>Trending Tech</h3>
        <div class="row">
            <div class="card">
                <img src="https://cdn.iconscout.com/icon/free/png-256/linux-19-226519.png" alt="Linux">
                <p>Linux</p>
            </div>
            <div class="card">
                <img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" alt="Docker">
                <p>Docker</p>
            </div>
            <div class="card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg" alt="Kubernetes">
                <p>Kubernetes</p>
            </div>
            <div class="card">
                <img src="https://cdn-icons-png.flaticon.com/512/2103/2103665.png" alt="CI/CD">
                <p>CI/CD</p>
            </div>
            <div class="card">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
                <p>GitHub</p>
            </div>
            <div class="card">
                <img src="https://www.vectorlogo.zone/logos/terraformio/terraformio-icon.svg" alt="Terraform">
                <p>Terraform</p>
            </div>
            <div class="card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Ansible_logo.svg" alt="Ansible">
                <p>Ansible</p>
            </div>
            <div class="card">
                <img src="https://cdn.worldvectorlogo.com/logos/prometheus.svg" alt="Prometheus">
                <p>Prometheus</p>
            </div>
            <div class="card">
                <img src="https://cdn.worldvectorlogo.com/logos/grafana.svg" alt="Grafana">
                <p>Grafana</p>
            </div>
            <div class="card">
                <img src="https://cdn.worldvectorlogo.com/logos/jenkins-1.svg" alt="Jenkins">
                <p>Jenkins</p>
            </div>
        </div>
    </div>

    <div class="workflow">
        <div class="workflow-step">Plan</div>
        <div class="workflow-step">Code</div>
        <div class="workflow-step">Build</div>
        <div class="workflow-step">Test</div>
        <div class="workflow-step">Deploy</div>
        <div class="workflow-step">Monitor</div>
    </div>
    
    <footer>
        Built with 💙 by Sandi — GKE + Cloud Build CI/CD
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t backend-app backend'
            }
        }

        stage('Deploy Backend Containers') {
            steps {
                sh '''
                    docker network create lab-network || true
                    docker rm -f backend1 backend2 || true
                    docker run -d --name backend1 --network lab-network backend-app
                    sleep 3
                    docker run -d --name backend2 --network lab-network backend-app
                '''
            }
        }

        stage('Deploy NGINX Load Balancer') {
            steps {
                sh '''
                    docker rm -f nginx-lb || true
                    sleep 2
                    docker run -d --name nginx-lb -p 80:80 \
                        --network lab-network \
                        -v $(pwd)/nginx:/etc/nginx/conf.d \
                        nginx
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully. NGINX load balancer is running.'
        }
        failure {
            echo 'Pipeline failed. Check console logs for errors.'
        }
    }
}

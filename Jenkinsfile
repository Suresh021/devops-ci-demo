pipeline {
agent any

```
environment {
    IMAGE_NAME = "devops-ci-demo-app"
    CONTAINER_NAME = "devops-ci-demo-container"
    APP_PORT = "5000"
}

stages {

    stage('Checkout') {
        steps {
            checkout scm
        }
    }

    stage('Build Docker Image') {
        steps {
            script {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
    }

    stage('Stop Old Container') {
        steps {
            script {
                sh '''
                    if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
                      docker stop ${CONTAINER_NAME}
                    fi
                    if [ "$(docker ps -a -q -f name=${CONTAINER_NAME})" ]; then
                      docker rm ${CONTAINER_NAME}
                    fi
                '''
            }
        }
    }

    stage('Run Container') {
        steps {
            script {
                sh "docker run -d --name ${CONTAINER_NAME} -p 80:${APP_PORT} ${IMAGE_NAME}:latest"
            }
        }
    }

    stage('Smoke Test') {
        steps {
            script {
                sh 'sleep 3'
                sh 'curl -f http://localhost || (echo "Smoke test failed" && exit 1)'
            }
        }
    }

}

post {
    success {
        echo "Build & deploy succeeded"
    }
    failure {
        echo "Build failed"
    }
}
```

}

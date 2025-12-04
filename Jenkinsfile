pipeline {
  agent any

  environment {
    IMAGE_NAME = "devops-ci-demo-app"
    CONTAINER_NAME = "devops-ci-demo-container"
    APP_PORT = "5000"
  }

  stage('Checkout') {
  steps {
    cleanWs()
    checkout scm
  }
}

stage('Build Docker Image') {
  steps {
    script {
      sh '''
        GIT_COMMIT=$(git rev-parse --short HEAD)
        docker build --no-cache -t ${IMAGE_NAME}:${GIT_COMMIT} -t ${IMAGE_NAME}:latest .
      '''
    }
  }
}

stage('Stop Old Container') {
  steps {
    script {
      sh '''
        docker stop ${CONTAINER_NAME} || true
        docker rm ${CONTAINER_NAME} || true
      '''
    }
  }
}

stage('Run Container') {
  steps {
    script {
      sh "docker run -d --name ${CONTAINER_NAME} -p 80:${APP_PORT} ${IMAGE_NAME}:${GIT_COMMIT}"
    }
  }
}

    stage('Smoke Test') {
      steps { script { sh 'sleep 3'; sh 'curl -f http://localhost || (echo "Smoke test failed" && exit 1)' } }
    }
  }

  post {
    success { echo "Build & deploy succeeded" }
    failure { echo "Build failed" }
  }
}

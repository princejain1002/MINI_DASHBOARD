pipeline {
    agent any

    environment {
        IMAGE_NAME = "streamlit-app"
        CONTAINER_NAME = "streamlit-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run -d \
                        --name $CONTAINER_NAME \
                        -p 8501:8501 \
                        $IMAGE_NAME:latest
                '''
            }
        }
    }
}

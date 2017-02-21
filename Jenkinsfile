pipeline {
  agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'pwd'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'ls -lh'
            }
        }
    }
}

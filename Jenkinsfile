pipeline {
    agent { label 'master' }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'figlet Build'
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'figlet Test'
                sh 'pwd'
            }
        }
        stage('Deploy') {
          steps {
                echo 'Deploying....'
                sh 'figlet Deploy'
                sh 'ls -lh'
            }
        }
    }
}

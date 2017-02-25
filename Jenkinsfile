pipeline {
    agent { label 'master' }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'figlet Build'
                checkout scm
                sh 'docker build -t jenkins/countdown2cure:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'figlet Test'
                sh 'pwd'
                echo 'starting container'
                sh 'docker run -d --name jenkins-test -p 1492:80 jenkins/countdown2cure:latest'
                sh 'sleep 15'
                echo 'connecting to container'
                sh 'curl http://localhost:1492'
                echo 'stopping and removing container'
                sh 'docker stop jenkins-test && docker rm jenkins-test'
            }
        }
        stage('Deploy') {
          steps {
                echo 'Deploying....'
                sh 'figlet Deploy'
                sh 'ls -lh'
                sh 'docker images'
            }
        }
    }
    post {
        always {
          deleteDir()
        }
        success {
            mail to:"rmcdermo@fredhutch.org", subject:"SUCCESS: ${currentBuild.fullDisplayName}", body: "Yay, we passed."
        }
        failure {
            mail to:"rmcdermo@fredhutch.org", subject:"FAILURE: ${currentBuild.fullDisplayName}", body: "Boo, we failed."
        }
    }
}

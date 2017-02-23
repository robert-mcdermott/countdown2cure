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

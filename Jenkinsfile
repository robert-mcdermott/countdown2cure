pipeline {
    agent { label 'master' }
    
    environment {
        FHDOCKERHUB = credentials('ee28d6e6-9965-43c2-9863-1164f2c534ed')
        RANCHERAPI = credentials('rancher-hdc-dev')
    }
    stages {
        stage('Build') {
            steps {
                checkout scm                
                sh '''
                figlet Build
                docker build -t dockerhub.fhcrc.org/countdown2cure:latest .
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                figlet Test
                pwd
                echo 'starting container'
                docker run -d --name countdown2cure-$BUILD_TAG -p 8889:80 dockerhub.fhcrc.org/countdown2cure:latest
                sleep 15
                echo 'connecting to container'
                curl http://localhost:8889
                echo 'stopping and removing container'
                docker stop countdown2cure-$BUILD_TAG && docker rm countdown2cure-$BUILD_TAG
                '''
            }
        }
        stage('Push') {
          steps {
                sh '''
                figlet Push
                ls -lh
                docker login --username $FHDOCKERHUB_USR --password $FHDOCKERHUB_PSW https://dockerhub.fhcrc.org
                docker push dockerhub.fhcrc.org/countdown2cure:latest
                sleep 15
                '''
            }
        }
        stage('Deploy') {
          steps {
                sh '''
                figlet Deploy
                rancher-compose --project-name countdown2cure --url https://containers.fhcrc.org/v1/projects/1a7  --access-key $RANCHERAPI_USR --secret-key $RANCHERAPI_PSW up -d --pull --force-upgrade --confirm-upgrade
                '''
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

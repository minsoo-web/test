pipeline {
    agent any
    options {
        ansiColor('xterm')
    }
    stages {
        stage ('CSW') {
            agent {
                dockerfile true
            }
            steps {
                sh "make install"
                sh "make lint"
                recordIssues enabledForFailure: true, tools: [
                    checkStyle(pattern: '**/checkstyle-result.xml', reportEncoding: 'UTF-8')
                ]
                archiveArtifacts artifacts: 'checkstyle-result.xml', fingerprint: true
            }
        }
        stage ('TIMO') {
            agent {
                docker{
                    image "timo-mobigen:latest"
                }
            }
            steps {
                copyArtifacts fingerprintArtifacts: true, projectName: "/${JOB_NAME}", selector: specific("${BUILD_NUMBER}")
                sh "timo setting yaml"
                sh "timo get name"
                sh "timo get version"
                sh "timo parse CSW"
                sh "timo get score"
            }
        }
    }
}
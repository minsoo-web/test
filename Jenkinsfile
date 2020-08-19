// def MASTER_BUILD_NUMBER = Jenkins.instance.getItem('minsoo-test').lastSuccessfulBuild.number

pipeline {
    agent any
    
    options {
        ansiColor('xterm')
    }

    // triggers {
    //     // 10분마다 8~18시까지 월~목 동안
    //     cron('*/10 8-18 * * 1-5')
    // }
    
    stages {
        stage('AUTO BUILD') {
            // when {
            //     triggeredBy "TimerTrigger"
            // }
            steps {
                build(
                    job: 'minsoo-test',
                    wait: true,
                    parameters: [
                        string(name: 'ID', value: 'root'), 
                        string(name: 'build_target', value: 'IRIS-E2E-SAAS'),
                        string(name: 'menu_target', value: 'All'),
                        string(name: 'user', value: 'All'),
                        string(name: 'container_number', value: "$BUILD_NUMBER")
                    ]
                )
                echo "it is auto build 😃"
            }
        }
        stage('PARAMS-E2E-TEST') {
            steps {
                sh"""
                docker exec -t -w /root/IRIS-E2E-SAAS new-iris-e2e-${BUILD_NUMBER} qa-script/run-e2e-headless-side.sh
                """
            }    
        }
    }
    
}
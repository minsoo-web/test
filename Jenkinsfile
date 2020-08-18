def MASTER_BUILD_NUMBER = Jenkins.instance.getItem('minsoo-test').lastSuccessfulBuild.number

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
                        string(name: 'build_target', value: 'SAMPLE-E2E'),
                        string(name: 'menu_target', value: 'ALL'),
                    ]
                )
                echo "it is auto build 😃"
            }
        }
        stage('PARAMS-E2E-TEST') {
            steps {
                sh"""
                docker exec -t new-iris-e2e-saas-${MASTER_BUILD_NUMBER} qa-script/run-e2e-headless-side.sh;
                """
            }    
        }
    }
    
}
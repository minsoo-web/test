pipeline {
    agent any
    
    options {
        ansiColor('xterm')
    }

    stages {
        stage('AUTO BUILD') {
            when {
                triggeredBy "TimerTrigger"
            }
            steps {
                echo "⏰ It is auto build"
                build(
                    job: 'minsoo-test',
                    wait: true,
                    parameters: [
                        string(name: 'build_target', value: 'IRIS-E2E-SAAS'),
                        string(name: 'menu_target', value: 'All'),
                        string(name: 'user', value: 'All'),
                        string(name: 'AUTO', value: 'TRUE')
                    ]
                )
            }
        }

        stage('PARAMS-E2E-TEST') {
            steps {
                echo "🔥 RUN PARAMETER E2E TEST"
                sh"""
                # 테스트 진행
                # docker exec -t -w /root/IRIS-E2E-SAAS new-iris-e2e qa-script/initialize.sh;
                docker exec -t -w /root/IRIS-E2E-SAAS new-iris-e2e python script/modules/side_runner/run_side.py
                docker exec -t -w /root/IRIS-E2E-SAAS new-iris-e2e script/modules/side_runner/run_side.sh
                """
                echo "END STAGE"
            }    
        }
    }
    
}